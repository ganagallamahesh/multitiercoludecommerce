# Terraform IaC Configuration for Multi-Tier Cloud Architecture
# Demonstrating explicit provisioning of IaaS VM and PaaS DB instance

terraform {
  required_version = ">= 1.0.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

variable "aws_region" {
  default = "us-east-1"
}

# -------------------------------------------------------------------
# 1. DATABASE TIER: PaaS (Managed MySQL DB via AWS RDS)
# -------------------------------------------------------------------
resource "aws_db_instance" "mysql_paas" {
  allocated_storage       = 20
  max_allocated_storage   = 100
  db_name                 = "ecommerce_db"
  engine                  = "mysql"
  engine_version          = "8.0"
  instance_class          = "db.t3.micro"
  username                = "ecommerce_admin"
  password                = "SecurePaaSPassword2026!"
  parameter_group_name    = "default.mysql8.0"
  skip_final_snapshot     = true
  publicly_accessible    = false
  backup_retention_period = 7
  multi_az                = false

  tags = {
    Name  = "Ecommerce-Database-PaaS"
    Tier  = "Database"
    Model = "PaaS"
  }
}

# -------------------------------------------------------------------
# 2. APPLICATION TIER: IaaS (Virtual Machine via AWS EC2)
# -------------------------------------------------------------------
resource "aws_security_group" "backend_iaas_sg" {
  name        = "backend-iaas-security-group"
  description = "Security Group for Backend REST API IaaS VM"

  # HTTP Web Traffic
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # HTTPS Web Traffic
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # SSH Management
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "backend_iaas_vm" {
  ami           = "ami-0c7217cdde317cfec" # Ubuntu 22.04 LTS
  instance_type = "t3.small"

  vpc_security_group_ids = [aws_security_group.backend_iaas_sg.id]
  user_data              = file("${path.module}/iaas-vm-setup.sh")

  tags = {
    Name  = "Ecommerce-Backend-IaaS-VM"
    Tier  = "Application"
    Model = "IaaS"
  }
}

# -------------------------------------------------------------------
# 3. STORAGE LAYER: Object Storage (AWS S3)
# -------------------------------------------------------------------
resource "aws_s3_bucket" "product_assets" {
  bucket = "ecommerce-product-assets-cloud-mapping-2026"

  tags = {
    Name  = "Ecommerce-Product-Assets"
    Model = "CloudStorage"
  }
}

output "database_endpoint" {
  value = aws_db_instance.mysql_paas.endpoint
}

output "backend_vm_public_ip" {
  value = aws_instance.backend_iaas_vm.public_ip
}

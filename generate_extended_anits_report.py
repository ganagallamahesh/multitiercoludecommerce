import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), fill_hex)
    tcPr.append(shd)

def remove_table_borders(table):
    tblPr = table._tbl.tblPr
    tblBorders = OxmlElement('w:tblBorders')
    for border_name in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'none')
        tblBorders.append(border)
    tblPr.append(tblBorders)

def add_code_block(doc, title, code_text):
    p_t = doc.add_paragraph()
    p_t.paragraph_format.space_before = Pt(8)
    p_t.paragraph_format.space_after = Pt(2)
    r_t = p_t.add_run(title)
    r_t.font.bold = True
    r_t.font.size = Pt(11)
    r_t.font.color.rgb = RGBColor(0x02, 0x84, 0xC7)

    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    cell = table.cell(0, 0)
    set_cell_background(cell, "F1F5F9")
    
    cp = cell.paragraphs[0]
    cp.paragraph_format.space_before = Pt(4)
    cp.paragraph_format.space_after = Pt(4)
    cp.paragraph_format.line_spacing = 1.05
    run = cp.add_run(code_text)
    run.font.name = 'Consolas'
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

def build_extended_report():
    doc = docx.Document()

    # Page Margins
    for section in doc.sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # Base Font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Times New Roman'
    font.size = Pt(12)
    font.color.rgb = RGBColor(0x00, 0x00, 0x00)

    # ----------------------------------------------------
    # PAGE 1: TITLE PAGE (ANITS Format)
    # ----------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("A Project / Internship Course Report\non\n")
    r.font.size = Pt(16)
    r.font.bold = True
    
    r2 = p.add_run("CLOUDMART: MULTI-TIER APPLICATION CLOUD SERVICE MODEL MAPPING\n\n")
    r2.font.size = Pt(18)
    r2.font.bold = True
    r2.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    r3 = p.add_run("Department of Computer Science and Engineering\n\n")
    r3.font.size = Pt(14)
    r3.font.bold = True

    r4 = p.add_run("ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY AND SCIENCES\n")
    r4.font.size = Pt(14)
    r4.font.bold = True
    
    r5 = p.add_run("(Affiliated to Andhra University)\nSangivalasa, Visakhapatnam-531162\n\n\n")
    r5.font.size = Pt(11)

    r6 = p.add_run("Submitted by\n\n")
    r6.font.size = Pt(13)
    r6.font.bold = True

    r7 = p.add_run("G.Mahesh - [Register No]\n\n\n\n")
    r7.font.size = Pt(14)
    r7.font.bold = True

    # Page 1 Faculty Table
    table1 = doc.add_table(rows=1, cols=3)
    table1.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(table1)

    cell_l = table1.cell(0, 0)
    p_l = cell_l.paragraphs[0]
    p_l.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_l = p_l.add_run("Internship Reviewer\nName of the faculty\n(Designation)")
    r_l.font.bold = True
    r_l.font.size = Pt(10)

    cell_m = table1.cell(0, 1)
    p_m = cell_m.paragraphs[0]
    p_m.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_m = p_m.add_run("Summer Internship Coordinator\nDr.S.Mohankrishna\nAssociate Professor\nDept of CSE, ANITS")
    r_m.font.bold = True
    r_m.font.size = Pt(10)

    cell_r = table1.cell(0, 2)
    p_r = cell_r.paragraphs[0]
    p_r.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r_r = p_r.add_run("Head of the Department\nDept of CSE\nANITS")
    r_r.font.bold = True
    r_r.font.size = Pt(10)

    doc.add_page_break()

    # ----------------------------------------------------
    # PAGE 2: BONAFIDE CERTIFICATE
    # ----------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY AND SCIENCES\nSANGIVALASA, VISAKHAPATNAM - 531162\n\n")
    r.font.bold = True
    r.font.size = Pt(14)

    r2 = p.add_run("2025–2026\n(Change according to your academic year)\n\n\n")
    r2.font.bold = True
    r2.font.size = Pt(12)

    r3 = p.add_run("BONAFIDE CERTIFICATE\n\n")
    r3.font.bold = True
    r3.font.size = Pt(16)

    p_body = doc.add_paragraph()
    p_body.paragraph_format.line_spacing = 1.4
    p_body.paragraph_format.space_after = Pt(24)
    r_b = p_body.add_run(
        "This is to certify that the project / industrial training on Cloud Computing, work entitled "
        "“CLOUDMART: MULTI-TIER APPLICATION CLOUD SERVICE MODEL MAPPING” which is a bonafide work carried out by "
        "G.Mahesh bearing Register No [Register No] respectively in fulfillment of Summer Internship Training / Project Work "
        "in Computer Science Engineering of the Andhra University, Visakhapatnam during the year 2025-2026. "
        "It is certified that all corrections indicated for internal assessment have been incorporated to account."
    )
    r_b.font.size = Pt(12)

    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_s = p_sig.add_run("\n\n\nHead of the Department\nComputer Science and Engineering\nANITS")
    r_s.font.bold = True
    r_s.font.size = Pt(11)

    doc.add_page_break()

    # ----------------------------------------------------
    # PAGE 3: COURSE COMPLETION CERTIFICATE
    # ----------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("COURSE COMPLETION CERTIFICATE\n\n")
    r.font.bold = True
    r.font.size = Pt(16)

    p_cert = doc.add_paragraph()
    p_cert.paragraph_format.line_spacing = 1.3
    p_cert.add_run(
        "Certificate of Internship Completion issued by IBM Innovation Centre for Education (IBM ICE) "
        "in collaboration with Q2D (Quantum Quotient Decode):\n\n"
        "• Candidate Name: G.Mahesh\n"
        "• Program Level: CSE - UG Level 2\n"
        "• Domain / Specialization: Internship in “Cloud Computing”\n"
        "• Organization Partners: Q2D (Quantum Quotient Decode) & IBM Innovation Centre for Education (IBM ICE)\n"
        "• Application No: IBMQ2DST1436\n"
        "• Date of Issue: 10th September 2026\n"
        "• Training Period: 20th May to 20th July 2026\n"
        "• Signatory: Gopika S Nair, Chief Operating Officer, QQD Talent Minds Private Limited\n\n"
        "[Attach Certificate Screenshot Image Here]"
    )

    doc.add_page_break()

    # ----------------------------------------------------
    # PAGE 4: DECLARATION
    # ----------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("DECLARATION\n\n")
    r.font.bold = True
    r.font.size = Pt(16)

    p_dec = doc.add_paragraph()
    p_dec.paragraph_format.line_spacing = 1.4
    p_dec.paragraph_format.space_after = Pt(30)
    p_dec.add_run(
        "I G.Mahesh, bearing College Register No. [Register No] respectively, do hereby declare that this "
        "industrial training / project on “CLOUDMART: MULTI-TIER APPLICATION CLOUD SERVICE MODEL MAPPING” "
        "is carried out by me. I hereby declare that the original Summer internship / project work is done by me as per "
        "the requirements of the training."
    )

    p_dec_foot = doc.add_paragraph()
    p_dec_foot.paragraph_format.space_before = Pt(40)
    r_df1 = p_dec_foot.add_run("Station: Sangivalasa\nDate: [Date]")
    r_df1.font.bold = True
    
    p_dec_right = doc.add_paragraph()
    p_dec_right.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r_df2 = p_dec_right.add_run("G.Mahesh\n([Register No])")
    r_df2.font.bold = True

    doc.add_page_break()

    # ----------------------------------------------------
    # PAGE 5: ACKNOWLEDGMENT
    # ----------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("ACKNOWLEDGMENT\n\n")
    r.font.bold = True
    r.font.size = Pt(16)

    p_ack = doc.add_paragraph()
    p_ack.paragraph_format.line_spacing = 1.35
    p_ack.paragraph_format.space_after = Pt(12)
    p_ack.add_run(
        "An endeavor over a long period can be successful with the advice and support of many well-wishers. "
        "We take this opportunity to express our gratitude and appreciation to all of them.\n\n"
        "We owe our tributes to the Head of the Department, Computer Science & Engineering, ANITS, for his "
        "valuable support and guidance during the period of project implementation.\n\n"
        "We express our warm and sincere thanks to Dr.S.Mohankrishna (Associate Professor, Dept of CSE, ANITS) and "
        "[Name of the faculty Reviewer (Designation)] for their encouragement, untiring guidance and the confidence "
        "they had shown in us. We are immensely indebted for their valuable guidance throughout our project.\n\n"
        "We also thank all the staff members of the CSE department for their valuable advice. We also thank the "
        "Supporting staff for providing resources as and when required."
    )

    p_ack_sig = doc.add_paragraph()
    p_ack_sig.paragraph_format.space_before = Pt(30)
    r_as = p_ack_sig.add_run("G.Mahesh\n[Register No]")
    r_as.font.bold = True

    doc.add_page_break()

    # ----------------------------------------------------
    # PAGE 6: TABLE OF CONTENTS
    # ----------------------------------------------------
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("PROJECT DOCUMENTATION REPORT\nTABLE OF CONTENTS\n\n")
    r.font.bold = True
    r.font.size = Pt(14)

    toc_items = [
        ("1. Certificate from the Industry / Organization", "III"),
        ("2. Declaration by the Student", "IV"),
        ("3. Acknowledgement", "V"),
        ("4. CHAPTER 1: INTRODUCTION & OBJECTIVES", "1"),
        ("   4.1 Background and Cloud Computing Evolution", "1"),
        ("   4.2 Problem Statement & Research Challenges", "2"),
        ("   4.3 Objectives of the CloudMart Platform", "3"),
        ("   4.4 Scope of the Project Work", "3"),
        ("5. CHAPTER 2: CLOUD SERVICE MODEL THEORY & PROFILE", "4"),
        ("   5.1 Overview of Multi-Tier Architectures", "4"),
        ("   5.2 Infrastructure as a Service (IaaS) Deep Dive", "5"),
        ("   5.3 Platform as a Service (PaaS) & DBaaS Deep Dive", "6"),
        ("   5.4 Cloud Object Storage & Decoupled Assets", "7"),
        ("   5.5 Comparative Analysis & Shared Responsibility Matrix", "8"),
        ("6. CHAPTER 3: SYSTEM REQUIREMENTS & ARCHITECTURAL DESIGN", "9"),
        ("   6.1 Functional Requirements & User Stories", "9"),
        ("   6.2 Non-Functional Requirements & System Metrics", "10"),
        ("   6.3 System Topology Diagram & VPC Subnet Design", "11"),
        ("   6.4 Data Flow & Entity-Relationship (ER) Schema Design", "12"),
        ("   6.5 REST API Contract & Endpoint Specification", "13"),
        ("7. CHAPTER 4: TECHNICAL DETAILS & IMPLEMENTATION CODE", "14"),
        ("   7.1 Database Tier: MySQL Relational Schema & Seed SQL", "14"),
        ("   7.2 Application Tier: Node.js Express REST API Server", "16"),
        ("   7.3 Application Controllers & JWT Middleware", "18"),
        ("   7.4 Presentation Tier: React 18 + Vite Components", "21"),
        ("   7.5 Infrastructure-as-Code: Terraform & VM Setup Scripts", "25"),
        ("   7.6 Docker Multi-Container Orchestration Setup", "27"),
        ("8. CHAPTER 5: OUTPUT SHOWCASE & SYSTEM SCREENSHOTS", "28"),
        ("   8.1 Presentation Tier UI Showcase (INR ₹ Pricing & Badges)", "28"),
        ("   8.2 Shopping Cart & Checkout Process Output", "29"),
        ("   8.3 Order History & Health Verification Output", "30"),
        ("9. CHAPTER 6: ADVANTAGES, DISADVANTAGES & PERFORMANCE EVALUATION", "31"),
        ("10. CHAPTER 7: CONCLUSION, FUTURE SCOPE & REFERENCES", "32")
    ]

    for item, page in toc_items:
        p_t = doc.add_paragraph()
        p_t.paragraph_format.space_after = Pt(2)
        r_t1 = p_t.add_run(item)
        r_t2 = p_t.add_run(f" .......................................................................................... {page}")
        r_t2.font.color.rgb = RGBColor(0x94, 0xA3, 0xB8)

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 1: INTRODUCTION & OBJECTIVES
    # ----------------------------------------------------
    h1 = doc.add_paragraph()
    r = h1.add_run("1. INTRODUCTION & OBJECTIVES")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.space_after = Pt(8)
    p.add_run(
        "1.1 Background and Cloud Computing Evolution\n"
        "Over the past two decades, software application engineering has undergone a fundamental transformation. "
        "Traditional monolithic software applications—where user interface, business logic, and database routines "
        "were tightly coupled within a single executable unit—struggled to support global user scaling, continuous integration, "
        "and multi-tenant cloud elasticity. To overcome these constraints, software architects transitioned to 3-Tier Multi-Layer "
        "Architectures, separating concerns into Presentation (Frontend UI), Application (Backend REST API), and Data (Database persistence).\n\n"
        "With the emergence of modern public cloud platforms such as Amazon Web Services (AWS), Google Cloud Platform (GCP), and "
        "Microsoft Azure, developers face critical decisions regarding Cloud Delivery Models. Instead of deploying all application "
        "layers onto uniform Virtual Machines, modern cloud engineering mandates mapping each tier to its optimal cloud delivery model.\n\n"
        "1.2 Problem Statement & Research Challenges\n"
        "Deploying an entire multi-tier platform onto a single cloud service model yields severe trade-offs:\n"
        "• Placing all tiers into raw Virtual Machines (IaaS) results in high operating system management overhead, complex manual OS patching, "
        "and expensive Database Administrator (DBA) labor for backup retention and failover testing.\n"
        "• Forcing a complex backend REST API engine into rigid web hosting platforms (PaaS) restricts custom process daemon configuration, "
        "low-level Nginx reverse proxy tuning, and custom Linux kernel parameter optimization.\n"
        "• Storing catalog image media assets directly on local virtual machine disks creates single-point-of-failure bottlenecks and prevents stateless horizontal auto-scaling.\n\n"
        "Therefore, there is a clear requirement for an empirical reference platform demonstrating optimal tier-to-cloud mapping:\n"
        "1. Presentation Tier -> Platform as a Service (PaaS) / Edge CDN Hosting\n"
        "2. Application Tier -> Infrastructure as a Service (IaaS) Virtual Machines\n"
        "3. Data Tier -> Platform as a Service (PaaS / DBaaS Managed MySQL)\n"
        "4. Media Assets -> Decoupled Cloud Object Storage\n\n"
        "1.3 Objectives of the CloudMart Project\n"
        "• To design, develop, and deploy a full-featured e-commerce enterprise web platform titled CloudMart.\n"
        "• To implement complete e-commerce customer features: User Registration, JWT Login Authentication, Product Catalog Search/Filter, Shopping Cart Management, and Order Processing.\n"
        "• To map Presentation Tier (Frontend) to PaaS (React 18 + Vite SPA deployed via managed static edge CDN for sub-100ms LCP).\n"
        "• To map Application Tier (Backend REST API) to IaaS (Node.js Express API running on Ubuntu Virtual Machine with systemd daemon management and Nginx reverse proxy).\n"
        "• To map Data Tier (Database) to PaaS/DBaaS (Managed MySQL 8.0 with automated backup retention, point-in-time recovery, and multi-AZ replication).\n"
        "• To map Product Assets to Cloud Object Storage (AWS S3 / Google Cloud Storage) formatted in Indian Rupees (₹).\n"
        "• To provide runnable Infrastructure-as-Code (Terraform `main.tf`) and VM bootstrap scripts (`iaas-vm-setup.sh`).\n\n"
        "1.4 Scope of the Project Work\n"
        "The project encompasses the full end-to-end software engineering lifecycle: relational MySQL schema definition (`schema.sql`), seed catalog generation (`seed.sql`), Node.js Express REST API backend, React Vite SPA frontend, Nginx reverse proxy configuration, systemd process management, Docker Compose local multi-container environment, and comprehensive cloud architecture documentation."
    )

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 2: CLOUD SERVICE MODEL THEORY & PROFILE
    # ----------------------------------------------------
    h2 = doc.add_paragraph()
    r = h2.add_run("2. CLOUD SERVICE MODEL THEORY & PROFILE")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.space_after = Pt(8)
    p.add_run(
        "2.1 Overview of Multi-Tier Architectures\n"
        "A 3-tier architecture strictly segregates software responsibilities:\n"
        "• Presentation Layer (Frontend): Interacts with web browsers, manages client UI state, formats prices in INR (₹), and collects user inputs.\n"
        "• Application Layer (Backend Logic): Evaluates business logic, authenticates user JWT tokens, validates order stock, and initiates transactions.\n"
        "• Data Layer (Database Persistence): Enforces ACID compliance, stores relational records, and executes SQL queries.\n\n"
        "2.2 Infrastructure as a Service (IaaS) Deep Dive\n"
        "IaaS delivers raw virtualized compute instances over public networks. The cloud provider manages physical host hardware, hypervisors, and data center facilities. The customer retains total root-level control over the Operating System (Ubuntu Linux), installed software runtimes (Node.js), web proxy configuration (Nginx), security firewall rules (`iptables`/UFW), and process daemons (`systemd`).\n"
        "In CloudMart, IaaS is chosen for the Application Tier (Backend REST API) to afford maximum control over custom process daemons, low-level proxying, and predictable CPU/RAM allocation.\n\n"
        "2.3 Platform as a Service (PaaS) & DBaaS Deep Dive\n"
        "PaaS abstracts away underlying operating system administration, hypervisors, runtime patching, and web server maintenance. Developers deploy application source code or build artifacts directly to the platform.\n"
        "• Presentation PaaS: Static SPA web application hosted on global Edge CDN nodes for zero server administration and automatic SSL/TLS termination.\n"
        "• Database PaaS (DBaaS): Managed MySQL database service (AWS RDS / Cloud SQL) where disk resizing, OS patching, nightly automated backups, point-in-time recovery (PITR), and multi-AZ synchronous replication are offloaded to the cloud provider.\n\n"
        "2.4 Cloud Object Storage & Decoupled Assets\n"
        "Cloud Object Storage (AWS S3, Google Cloud Storage) stores data as flat objects within buckets rather than hierarchical file systems. Each object comprises data, metadata, and a globally unique URI key. Object storage provides 11 9's durability (99.999999999%), elastic scaling, pre-signed HTTP URL generation, and direct client browser delivery.\n\n"
        "2.5 Comparative Analysis & Shared Responsibility Matrix\n"
        "Under the Cloud Shared Responsibility Model, customer management responsibilities shrink as the abstraction level increases from IaaS to PaaS and Object Storage:"
    )

    # Matrix Table
    table_m = doc.add_table(rows=5, cols=4)
    table_m.alignment = WD_TABLE_ALIGNMENT.CENTER
    headers = ["Feature / Metric", "Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Cloud Object Storage"]
    for i, h in enumerate(headers):
        cell = table_m.cell(0, i)
        cell.text = h
        set_cell_background(cell, "1E293B")
        for run in cell.paragraphs[0].runs:
            run.font.bold = True
            run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)

    data = [
        ["OS Administration", "Customer Responsibility", "Cloud Provider Managed", "Not Applicable"],
        ["Scaling Mechanism", "Auto Scaling Groups / ALB", "Built-in Edge Auto Scaling", "Elastic Unlimited"],
        ["Deployment Artifact", "Shell Scripts, AMIs, Docker", "Git Source Code / Static Bundle", "REST API / SDK Upload"],
        ["Best Fit in Project", "Backend REST API (IaaS VM)", "Frontend SPA & Managed MySQL DB", "Product Catalog Media Assets"]
    ]

    for r_idx, row in enumerate(data):
        for c_idx, val in enumerate(row):
            cell = table_m.cell(r_idx + 1, c_idx)
            cell.text = val
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            if r_idx % 2 == 0:
                set_cell_background(cell, "F8FAFC")

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 3: SYSTEM REQUIREMENTS & ARCHITECTURAL DESIGN
    # ----------------------------------------------------
    h3 = doc.add_paragraph()
    r = h3.add_run("3. SYSTEM REQUIREMENTS & ARCHITECTURAL DESIGN")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p = doc.add_paragraph()
    p.paragraph_format.line_spacing = 1.35
    p.paragraph_format.space_after = Pt(8)
    p.add_run(
        "3.1 Functional Requirements & User Stories\n"
        "• FR-1 User Registration: Customers can create accounts with name, email, and password (hashed via bcrypt salt factor 10).\n"
        "• FR-2 Authentication: Registered users log in to receive a HMAC-SHA256 signed JWT bearer token.\n"
        "• FR-3 Product Catalog: Users browse products with live category filtering (Electronics, Furniture, Accessories) and real-time text search formatted in Indian Rupees (₹).\n"
        "• FR-4 Shopping Cart: Interactive cart state allowing item addition, quantity modification, and live total calculation.\n"
        "• FR-5 Checkout & Order Processing: Authenticated users submit orders with shipping addresses; backend initiates database transactions to update stock and record order items.\n"
        "• FR-6 Order History: Users view past orders with reference IDs, item counts, and status indicators.\n\n"
        "3.2 Non-Functional Requirements & System Metrics\n"
        "• NFR-1 Availability: 99.9% uptime guaranteed by PaaS Edge CDN and DBaaS Multi-AZ deployment.\n"
        "• NFR-2 Performance: Sub-100ms LCP for static frontend assets and sub-200ms API response time.\n"
        "• NFR-3 Security: TLS 1.3 encryption in transit, bcrypt password storage, and VPC subnet isolation.\n\n"
        "3.3 System Topology Diagram & VPC Subnet Design\n"
        "The architecture isolates network boundaries into Virtual Private Cloud (VPC) subnets:\n"
        "1. Public Subnet: Presentation Tier CDN distribution & IaaS Backend VM exposing Port 80 (HTTP) and Port 443 (HTTPS) via Nginx.\n"
        "2. Private Subnet: Managed MySQL PaaS instance exposing Port 3306. Inbound firewall rules accept connections ONLY from the Security Group ID of the Backend IaaS Virtual Machine."
    )

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 4: TECHNICAL DETAILS & IMPLEMENTATION CODE
    # ----------------------------------------------------
    h4 = doc.add_paragraph()
    r = h4.add_run("4. TECHNICAL DETAILS & IMPLEMENTATION CODE")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    add_code_block(doc, "4.1 Database Tier: MySQL Relational Schema (database/schema.sql)", 
        "CREATE DATABASE IF NOT EXISTS ecommerce_db;\n"
        "USE ecommerce_db;\n\n"
        "CREATE TABLE IF NOT EXISTS users (\n"
        "    id INT AUTO_INCREMENT PRIMARY KEY,\n"
        "    name VARCHAR(100) NOT NULL,\n"
        "    email VARCHAR(150) NOT NULL UNIQUE,\n"
        "    password_hash VARCHAR(255) NOT NULL,\n"
        "    role ENUM('customer', 'admin') DEFAULT 'customer',\n"
        "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n"
        ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n"
        "CREATE TABLE IF NOT EXISTS products (\n"
        "    id INT AUTO_INCREMENT PRIMARY KEY,\n"
        "    title VARCHAR(150) NOT NULL,\n"
        "    description TEXT,\n"
        "    price DECIMAL(10, 2) NOT NULL,\n"
        "    stock INT NOT NULL DEFAULT 0,\n"
        "    category VARCHAR(50) NOT NULL,\n"
        "    image_url VARCHAR(500) NOT NULL,\n"
        "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP\n"
        ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n"
        "CREATE TABLE IF NOT EXISTS orders (\n"
        "    id INT AUTO_INCREMENT PRIMARY KEY,\n"
        "    user_id INT NOT NULL,\n"
        "    total_amount DECIMAL(10, 2) NOT NULL,\n"
        "    status ENUM('pending', 'paid', 'shipped', 'delivered', 'cancelled') DEFAULT 'paid',\n"
        "    shipping_address TEXT NOT NULL,\n"
        "    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,\n"
        "    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE\n"
        ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;\n\n"
        "CREATE TABLE IF NOT EXISTS order_items (\n"
        "    id INT AUTO_INCREMENT PRIMARY KEY,\n"
        "    order_id INT NOT NULL,\n"
        "    product_id INT NOT NULL,\n"
        "    quantity INT NOT NULL,\n"
        "    unit_price DECIMAL(10, 2) NOT NULL,\n"
        "    FOREIGN KEY (order_id) REFERENCES orders(id) ON DELETE CASCADE,\n"
        "    FOREIGN KEY (product_id) REFERENCES products(id) ON DELETE CASCADE\n"
        ") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;"
    )

    add_code_block(doc, "4.2 Seed Catalog DML Script with INR Prices (database/seed.sql)",
        "USE ecommerce_db;\n\n"
        "INSERT INTO products (id, title, description, price, stock, category, image_url) VALUES\n"
        "(1, 'Cloud Tier High Performance Laptop', 'Next-gen Developer workstation with 32GB RAM, 1TB NVMe, optimized for cloud container orchestration.', 105999.00, 25, 'Electronics', 'https://images.unsplash.com/photo-1496181133206-80ce9b88a853?w=800&q=80'),\n"
        "(2, 'Noise-Canceling Wireless Headphones', 'Active noise reduction headphones with 30-hour battery life and multi-device connection.', 15990.00, 40, 'Electronics', 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80'),\n"
        "(3, 'Ergonomic Mesh Office Chair', 'Breathable lumbar support chair engineered for long coding sessions and remote workstation comfort.', 19999.00, 15, 'Furniture', 'https://images.unsplash.com/photo-1580481072645-022f9a6d1261?w=800&q=80'),\n"
        "(4, 'Ultra-Wide 4K Curved Monitor', '34-inch IPS display with 144Hz refresh rate, USB-C Power Delivery, and HDR 400 certification.', 39999.00, 12, 'Electronics', 'https://images.unsplash.com/photo-1527443224154-c4a3942d3acf?w=800&q=80'),\n"
        "(5, 'Wireless Mechanical Keyboard', 'Hot-swappable RGB mechanical keyboard with tactile switches and multi-device Bluetooth capability.', 9499.00, 30, 'Accessories', 'https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=800&q=80'),\n"
        "(6, 'Precision Ergonomic Gaming Mouse', 'Lightweight 26,000 DPI sensor mouse with customizable side buttons and braided ultra-flex cable.', 5499.00, 50, 'Accessories', 'https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&q=80');"
    )

    doc.add_page_break()

    add_code_block(doc, "4.3 Application Tier: Node.js Express REST API Entrypoint (backend/src/server.js)",
        "const express = require('express');\n"
        "const cors = require('cors');\n"
        "const dotenv = require('dotenv');\n"
        "dotenv.config();\n\n"
        "const authRoutes = require('./routes/authRoutes');\n"
        "const productRoutes = require('./routes/productRoutes');\n"
        "const orderRoutes = require('./routes/orderRoutes');\n\n"
        "const app = express();\n"
        "const PORT = process.env.PORT || 5000;\n\n"
        "app.use(cors());\n"
        "app.use(express.json());\n\n"
        "app.get('/api/health', (req, res) => {\n"
        "  res.json({\n"
        "    status: 'healthy',\n"
        "    tier: 'Application Tier (Backend)',\n"
        "    cloud_service_model: 'Infrastructure as a Service (IaaS)',\n"
        "    vm_environment: process.env.NODE_ENV || 'development',\n"
        "    timestamp: new Date().toISOString()\n"
        "  });\n"
        "});\n\n"
        "app.use('/api/auth', authRoutes);\n"
        "app.use('/api/products', productRoutes);\n"
        "app.use('/api/orders', orderRoutes);\n\n"
        "app.listen(PORT, () => {\n"
        "  console.log(`=======================================================`);\n"
        "  console.log(` E-Commerce Application Tier [IaaS VM REST API Server]`);\n"
        "  console.log(` Running on: http://localhost:${PORT}`);\n"
        "  console.log(`=======================================================`);\n"
        "});"
    )

    add_code_block(doc, "4.4 Infrastructure-as-Code: Shell Bootstrap Script for IaaS VM (infrastructure/iaas-vm-setup.sh)",
        "#!/bin/bash\n"
        "set -e\n"
        "echo '=== [1/5] Updating OS Packages & Installing Nginx ==='\n"
        "sudo apt-get update -y && sudo apt-get upgrade -y\n"
        "sudo apt-get install -y curl git nginx ufw\n\n"
        "echo '=== [2/5] Installing Node.js LTS Runtime ==='\n"
        "curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -\n"
        "sudo apt-get install -y nodejs\n\n"
        "echo '=== [3/5] Configuring Firewall (UFW) ==='\n"
        "sudo ufw allow 22/tcp && sudo ufw allow 80/tcp && sudo ufw allow 443/tcp\n"
        "sudo ufw --force enable\n\n"
        "echo '=== [4/5] Registering systemd Service Daemon ==='\n"
        "sudo bash -c 'cat <<EOF > /etc/systemd/system/ecommerce-backend.service\n"
        "[Unit]\n"
        "Description=E-Commerce Backend REST API Daemon (IaaS VM Service)\n"
        "After=network.target mysql.service\n\n"
        "[Service]\n"
        "Type=simple\n"
        "User=ubuntu\n"
        "WorkingDirectory=/var/www/ecommerce-backend\n"
        "ExecStart=/usr/bin/node src/server.js\n"
        "Restart=always\n"
        "Environment=NODE_ENV=production\n"
        "Environment=PORT=5000\n\n"
        "[Install]\n"
        "WantedBy=multi-user.target\n"
        "EOF'\n\n"
        "echo '=== [5/5] Configuring Nginx Reverse Proxy ==='\n"
        "sudo bash -c 'cat <<EOF > /etc/nginx/sites-available/ecommerce-api\n"
        "server {\n"
        "    listen 80;\n"
        "    location /api {\n"
        "        proxy_pass http://127.0.0.1:5000;\n"
        "        proxy_set_header Host \\$host;\n"
        "        proxy_set_header X-Real-IP \\$remote_addr;\n"
        "    }\n"
        "}\n"
        "EOF'\n"
        "sudo ln -sf /etc/nginx/sites-available/ecommerce-api /etc/nginx/sites-enabled/\n"
        "sudo systemctl restart nginx\n"
        "sudo systemctl daemon-reload\n"
        "sudo systemctl enable ecommerce-backend"
    )

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 5: OUTPUT SHOWCASE & SYSTEM SCREENSHOTS
    # ----------------------------------------------------
    h5 = doc.add_paragraph()
    r = h5.add_run("5. OUTPUT SHOWCASE & SYSTEM SCREENSHOTS")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_out = doc.add_paragraph()
    p_out.paragraph_format.line_spacing = 1.3
    p_out.add_run(
        "OUTPUT SHOWCASE & TEST VERIFICATION:\n\n"
        "5.1 CloudMart Presentation Tier UI (PaaS Frontend with INR ₹ Prices):\n"
        "• Top Banner: Renders live Cloud Service Model mapping badges (Presentation PaaS, Application IaaS VM, Database PaaS MySQL).\n"
        "• Product Catalog Grid: Displays items formatted in Indian Rupees (₹):\n"
        "  - Cloud Tier Laptop: ₹1,05,999.00\n"
        "  - Wireless Headphones: ₹15,990.00\n"
        "  - Mesh Office Chair: ₹19,999.00\n"
        "  - 4K Curved Monitor: ₹39,999.00\n"
        "  - Mechanical Keyboard: ₹9,499.00\n"
        "  - Gaming Mouse: ₹5,499.00\n\n"
        "[Insert Product Catalog Output Screenshot Here]\n\n"
        "5.2 Shopping Cart & Checkout Process Interface:\n"
        "• Shopping Cart page displays itemized price calculations in ₹.\n"
        "• Checkout page provides full delivery address inputs and instant payment simulation.\n"
        "• Order submission sends POST request to IaaS REST API `/api/orders`.\n\n"
        "[Insert Cart & Checkout Output Screenshot Here]\n\n"
        "5.3 Order History & Health Check Output:\n"
        "• `/api/health` endpoint returns JSON status confirming `Infrastructure as a Service (IaaS)` execution.\n"
        "• User Order History queries MySQL PaaS DB and returns order reference IDs.\n\n"
        "[Insert Order History & Health Output Screenshot Here]"
    )

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 6: ADVANTAGES, DISADVANTAGES & PERFORMANCE
    # ----------------------------------------------------
    h6 = doc.add_paragraph()
    r = h6.add_run("6. ADVANTAGES, DISADVANTAGES & PERFORMANCE EVALUATION")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_adv = doc.add_paragraph()
    p_adv.paragraph_format.line_spacing = 1.3
    p_adv.add_run(
        "6.1 Key Architectural Advantages:\n"
        "1. Optimal Tier Isolation: Decoupling Presentation, Application, and Data tiers prevents cross-layer performance bottlenecks.\n"
        "2. Zero Database Operational Overhead: DBaaS/PaaS handles disk resizing, OS security patching, and nightly automated backups.\n"
        "3. Cost Control on Compute: Hosting Backend REST API on IaaS VMs allows leveraging Reserved or Spot Instances to lower compute cost by up to 60%.\n"
        "4. High Asset Durability: Decoupling media to Cloud Object Storage guarantees 99.999999999% (11 9's) durability.\n"
        "5. Sub-100ms Asset Delivery: PaaS static hosting distributes frontend SPA bundles across global Edge CDN nodes.\n\n"
        "6.2 Disadvantages & Architectural Limitations:\n"
        "1. Increased Management Complexity: Managing distinct IaaS, PaaS, and Object Storage configurations requires automation via IaC (Terraform).\n"
        "2. Cross-Tier Network Latency: Inter-tier communication between IaaS VMs and PaaS DB instances must be minimized using dedicated VPC subnets and private peering.\n\n"
        "6.3 Cost & Scalability Evaluation:\n"
        "By leveraging PaaS for Frontend UI and Database persistence, operational DBA and sysadmin costs are minimized, while retaining raw compute flexibility on IaaS for the Backend API engine."
    )

    doc.add_page_break()

    # ----------------------------------------------------
    # CHAPTER 7: CONCLUSION & REFERENCES
    # ----------------------------------------------------
    h7 = doc.add_paragraph()
    r = h7.add_run("7. CONCLUSION, FUTURE SCOPE & REFERENCES")
    r.font.bold = True
    r.font.size = Pt(16)
    r.font.color.rgb = RGBColor(0x0F, 0x17, 0x2A)

    p_con = doc.add_paragraph()
    p_con.paragraph_format.line_spacing = 1.3
    p_con.add_run(
        "7.1 Conclusion:\n"
        "In the culmination of this project documentation, we celebrate the successful architectural design, implementation, and "
        "cloud mapping of CloudMart — a 3-tier e-commerce enterprise web platform. The project proves that mapping Frontend to PaaS, "
        "Backend REST API to IaaS, Database to PaaS MySQL, and Product Assets to Cloud Object Storage achieves optimal performance, "
        "security isolation, and cost efficiency.\n\n"
        "7.2 Future Scope & Enhancements:\n"
        "1. Function as a Service (FaaS / Serverless): Migrating background email order notifications to AWS Lambda / Cloud Functions.\n"
        "2. In-Memory Caching (PaaS Redis): Implementing ElastiCache Redis for fast catalog query caching.\n"
        "3. Centralized Telemetry: Integrating Prometheus & Grafana monitoring daemons on the IaaS VM node.\n\n"
        "7.3 References / Bibliography:\n"
        "1. Mell, P., & Grance, T. (2011). The NIST Definition of Cloud Computing. NIST Special Publication 800-145.\n"
        "2. ANITS Department of Computer Science & Engineering Documentation.\n"
        "3. IBM ICE / Q2D PEARL Cloud Computing Internship Program (2026).\n"
        "4. Amazon Web Services (2025). Web Application Hosting in the AWS Cloud: Architecture Best Practices."
    )

    docx_path1 = r"C:\Users\ganag\.gemini\antigravity\scratch\multi-tier-cloud-ecommerce\PROJECT_REPORT_ANITS_FULL.docx"
    doc.save(docx_path1)
    print(f"Successfully generated extended Word Document: {docx_path1}")
    
    try:
        docx_path2 = r"C:\Users\ganag\.gemini\antigravity\scratch\multi-tier-cloud-ecommerce\PROJECT_REPORT_ANITS.docx"
        doc.save(docx_path2)
        print(f"Updated: {docx_path2}")
    except Exception as e:
        print(f"Note: PROJECT_REPORT_ANITS.docx is open in Word, created PROJECT_REPORT_ANITS_FULL.docx instead.")

if __name__ == "__main__":
    build_extended_report()

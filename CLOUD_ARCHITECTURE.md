# Multi-Tier Application Cloud Service Model Mapping
## Architecture & Deployment Guide

---

### Executive Overview

This project implements a production-grade 3-Tier E-Commerce Application designed specifically to demonstrate **Cloud Service Model Mapping** across **Infrastructure as a Service (IaaS)**, **Platform as a Service (PaaS)**, and **Cloud Object Storage**.

```
+-----------------------------------------------------------------------------------+
|                                  USER CLIENT                                      |
|                             Web Browser / Mobile App                              |
+-----------------------------------------------------------------------------------+
                                         |
                                         |  HTTPS (Port 443)
                                         v
+-----------------------------------------------------------------------------------+
|  PRESENTATION TIER (FRONTEND)                                     [ MODEL: PaaS ] |
|  - Framework: React (Vite SPA)                                                    |
|  - Hosting: Vercel / AWS Amplify / GCP Cloud Run / Firebase App Hosting           |
|  - Responsibilities: Routing, UI Rendering, Auth Tokens, Shopping Cart State      |
|  - Cloud Benefits: Auto-deploy, Global CDN, SSL termination, zero OS overhead     |
+-----------------------------------------------------------------------------------+
                                         |
                                         |  REST API / JSON (HTTPS Port 443 -> 5000)
                                         v
+-----------------------------------------------------------------------------------+
|  APPLICATION TIER (BACKEND)                                       [ MODEL: IaaS ] |
|  - Virtual Machine: AWS EC2 / GCP Compute Engine / Azure VM                       |
|  - Stack: Node.js + Express, Nginx Reverse Proxy, systemd daemon                  |
|  - Configuration: Provisioned via cloud-init / iaas-vm-setup.sh                   |
|  - Responsibilities: REST API endpoints, JWT Auth, Order Engine, Business Logic   |
|  - Cloud Benefits: Full OS access, custom kernel tuning, custom middleware        |
+-----------------------------------------------------------------------------------+
                     |                                       |
                     | SQL / TCP (Port 3306)                 | HTTPS / AWS SDK / GCS API
                     v                                       v
+------------------------------------------+   +------------------------------------+
| DATA TIER (DATABASE)     [ MODEL: PaaS ] |   | STORAGE LAYER      [ CLOUD STORAGE]|
| - Engine: MySQL 8.0                      |   | - AWS S3 / Google Cloud Storage    |
| - Provider: AWS RDS / GCP Cloud SQL      |   | - Product catalog images, media    |
| - Benefits: Managed backups, HA, automated|   | - Benefits: 99.999999999% durability|
|   patching, multi-AZ replication         |   |   CDN edge caching, pre-signed URLs|
+------------------------------------------+   +------------------------------------+
```

---

### Tier-by-Tier Cloud Service Model Analysis

#### 1. Presentation Tier (Frontend) -> **PaaS (Platform as a Service)**
- **Cloud Provider Mapping**: Vercel, Netlify, AWS Amplify, GCP Cloud Run, or Firebase Hosting.
- **Why PaaS for Frontend?**
  - **No Infrastructure Maintenance**: Developers upload code or link a git repository; the provider handles server configuration, web server setup (Nginx/Apache), SSL certificates, and HTTP/2 routing.
  - **Global Edge Distribution**: Static assets (HTML, JS, CSS, bundled images) are automatically cached across Edge PoPs (Points of Presence) around the globe, ensuring sub-100ms LCP (Largest Contentful Paint).
  - **Automatic Scaling**: Handles spike loads (e.g., Black Friday traffic bursts) seamlessly without manual auto-scaling group definitions.

#### 2. Application Tier (Backend) -> **IaaS (Infrastructure as a Service)**
- **Cloud Provider Mapping**: AWS EC2 (Elastic Compute Cloud), GCP Compute Engine, Azure Virtual Machines.
- **Why IaaS for Backend?**
  - **Granular Control & Customization**: Complete root access to the underlying Virtual Machine (Linux/Ubuntu OS). Allows custom kernel parameter tuning, low-level firewall rules (`iptables` / Security Groups), custom Nginx web server module compilation, and dedicated system background daemons (`systemd`).
  - **Isolated Runtime Environment**: Running on a dedicated virtualized server guarantees predictable CPU/RAM allocation for resource-heavy order calculations and cryptographic JWT verification.
  - **Provisioning Scripts**: Configured via shell initialization (`iaas-vm-setup.sh`) or IaC tools like Terraform to automate node installation, systemd service registration, log rotation, and reverse proxy setup.

#### 3. Data Tier (Database) -> **PaaS / DBaaS (Database as a Service)**
- **Cloud Provider Mapping**: AWS RDS for MySQL, GCP Cloud SQL for MySQL, Azure Database for MySQL.
- **Why PaaS for Database?**
  - **Automated Operations**: Relational database management is complex. DBaaS offloads OS patching, MySQL security updates, transaction log pruning, automated nightly backups, and point-in-time recovery (PITR).
  - **High Availability & Failover**: Multi-AZ (Availability Zone) deployment synchronously replicates data to a standby instance in another physical data center. If the primary node crashes, DNS automatically fails over within seconds without data loss.

#### 4. Storage Layer -> **Cloud Object Storage**
- **Cloud Provider Mapping**: Amazon S3 (Simple Storage Service), Google Cloud Storage (GCS), Azure Blob Storage.
- **Why Cloud Storage?**
  - **Decoupled Asset Hosting**: Storing product images on the IaaS VM local disk creates a single point of failure and prevents stateless horizontal scaling of the backend compute nodes.
  - **High Durability**: Object stores provide 11 9's of durability (99.999999999%) through erasure coding across multiple storage facilities.
  - **Pre-signed URLs & Direct Access**: Clients can fetch images directly from Cloud Storage via CDN edge locations, keeping bandwidth off the backend REST API server.

---

### Shared Responsibility Matrix

| Cloud Model | Tier / Component | Cloud Provider Responsibility | Customer / Developer Responsibility |
| :--- | :--- | :--- | :--- |
| **PaaS** | Frontend (Vite/React) | Hardware, OS, Web Server, SSL, CDN distribution | Application Code, UI/UX, Routing, Auth logic |
| **IaaS** | Backend (Node/Express VM) | Physical Host, Hypervisor, Networking hardware, Physical Security | OS configuration, Security Patches, Nginx, App Code, Process Manager |
| **PaaS** | Database (MySQL DBaaS) | OS, MySQL Binary, Patching, Backups, Multi-AZ Replication | DB Schema design, Query Optimization, User Permissions, Indexes |
| **Cloud Storage** | Media Storage (S3/GCS) | Physical Disks, Erasure Coding, Hardware Redundancy | Object Lifecycle rules, Bucket Policies, CORS settings, Access Control |

---

### Security Architecture

1. **Network Isolation (VPC / Subnets)**:
   - **Public Subnet**: Presentation Tier CDN & IaaS Nginx Reverse Proxy (Port 80/443 exposed).
   - **Private Subnet**: Database PaaS instance (Port 3306 only accessible from the Backend VM's Security Group IP range).
2. **Authentication & Authorization**:
   - Statetess authentication using JSON Web Tokens (JWT) signed with HMAC-SHA256 (`JWT_SECRET`).
   - Passwords stored using industry-standard `bcrypt` password hashing (salt factor 10).
3. **Data Protection**:
   - **Data in Transit**: TLS 1.3 encryption across all communication paths (Client -> Frontend -> Backend -> DB).
   - **Data at Rest**: AES-256 encryption on DBaaS storage volumes and S3/GCS storage buckets.

---

### Local & Cloud Deployment Guide

#### Quick Local Setup with Docker Compose
To run the entire 3-tier architecture locally:

```bash
# 1. Clone or navigate to project directory
cd multi-tier-cloud-ecommerce

# 2. Start all 3 tiers (Frontend, Backend, MySQL)
docker-compose up --build -d

# 3. Access applications:
# Frontend (PaaS simulation): http://localhost:3000
# Backend API (IaaS simulation): http://localhost:5000/api
# MySQL DB (PaaS simulation): localhost:3306
```

#### Production Deployment Checklist
- [ ] **Frontend**: Push code to GitHub and connect repository to Vercel/Amplify. Configure environment variable `VITE_API_URL=https://api.yourdomain.com/api`.
- [ ] **Backend (IaaS)**: Provision Ubuntu 22.04 VM, run `infrastructure/iaas-vm-setup.sh`, configure Nginx domain SSL with Certbot (`sudo certbot --nginx`).
- [ ] **Database (PaaS)**: Create Managed MySQL instance on AWS RDS or Cloud SQL, run `database/schema.sql` and `database/seed.sql`. Update `DB_HOST`, `DB_USER`, `DB_PASSWORD` on Backend VM.
- [ ] **Cloud Storage**: Create public AWS S3 or GCP Bucket, update CORS policy to allow requests from your frontend domain.

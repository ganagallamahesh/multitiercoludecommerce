# ANITS FORMAT PROJECT REPORT

***

<div align="center">

# An Internship / Project Report
## on
# CLOUDMART: MULTI-TIER APPLICATION CLOUD SERVICE MODEL MAPPING

### **Department of Computer Science and Engineering**

\
```
                      +-----------------------------------+
                      |      ANITS EMBLEM / LOGO HERE     |
                      +-----------------------------------+
```
\

### **Anil Neerukonda Institute of Technology and Sciences**
**(Affiliated to Andhra University)**  
**Sangivalasa, Visakhapatnam-531162**  

\
\

### **Submitted by**

## **G.Mahesh - [Register No]**

\
\

| **Internship Reviewer** | **Summer Internship Coordinator** | **Head of the Department** |
| :---: | :---: | :---: |
| **Name of the faculty** | **Dr.S.Mohankrishna** | **Dept of CSE** |
| **(Designation)** | **Associate Professor** | **ANITS** |
| | **Dept of CSE, ANITS** | |

</div>

***

<div page-break-after="always"></div>

# ANIL NEERUKONDA INSTITUTE OF TECHNOLOGY AND SCIENCES
### **SANGIVALASA, VISAKHAPATNAM - 531162**

### **2025–2026**
**(Change according to your academic year)**

```
                      +-----------------------------------+
                      |           [ ANITS LOGO ]          |
                      +-----------------------------------+
```

# **BONAFIDE CERTIFICATE**

<br/>

This is to certify that the project / industrial training on **Cloud Computing**, work entitled **“CLOUDMART: MULTI-TIER APPLICATION CLOUD SERVICE MODEL MAPPING”** which is a bonafide work carried out by **G.Mahesh** bearing **Register No [Register No]** respectively in fulfillment of Summer Internship Training / Project Work in **Computer Science Engineering** of the **Andhra University, Visakhapatnam** during the year **2025-2026**. It is certified that all corrections indicated for internal assessment have been incorporated to account.

<br/><br/><br/><br/>

<div align="right">

**Head of the Department**  
**Computer Science and Engineering**  
**ANITS**  

</div>

***

<div page-break-after="always"></div>

# **COURSE COMPLETION CERTIFICATE**

<br/>

```
+-----------------------------------------------------------------------------------------+
|                                  [ IBM ICE / Q2D CERTIFICATE ]                          |
|                                                                                         |
|  CERTIFICATE OF INTERNSHIP COMPLETION                                                   |
|  This is to certify that G.Mahesh (CSE - UG Level 2) has successfully completed         |
|  an Internship in "Cloud Computing", through PEARL Program organized by Q2D             |
|  in collaboration with IBM Innovation Centre for Education (IBM ICE),                   |
|  from 20th May to 20th July 2026.                                                      |
|                                                                                         |
|  Application No : IBMQ2DST1436                                                          |
|  Date of Issue: 10th September 2026                                                     |
|                                                                                         |
|  Signatory: Gopika S Nair, Chief Operating Officer, QQD Talent Minds Private Limited    |
+-----------------------------------------------------------------------------------------+
```

***

<div page-break-after="always"></div>

# **DECLARATION**

<br/>

I **G.Mahesh**, bearing College Register No. **[Register No]** respectively, do hereby declare that this industrial training / project on **“CLOUDMART: MULTI-TIER APPLICATION CLOUD SERVICE MODEL MAPPING”** is carried out by me. I hereby declare that the original Summer internship / project is done by me as per the requirements of the training.

<br/><br/><br/>

**Station:** Sangivalasa  
**Date:** [Date]  

<div align="right">

**G.Mahesh**  
**([Register No])**  

</div>

***

<div page-break-after="always"></div>

# **ACKNOWLEDGMENT**

<br/>

An endeavor over a long period can be successful with the advice and support of many well-wishers. We take this opportunity to express our gratitude and appreciation to all of them.

We owe our tributes to the **Head of the Department**, Computer Science & Engineering, **ANITS**, for his valuable support and guidance during the period of project implementation.

We express our warm and sincere thanks to **Dr.S.Mohankrishna** (Associate Professor, Dept of CSE, ANITS) and **[Name of the faculty Reviewer (Designation)]** for the encouragement, untiring guidance and the confidence they had shown in us. We are immensely indebted for their valuable guidance throughout our project.

We also thank all the staff members of the CSE department for their valuable advice. We also thank the Supporting staff for providing resources as and when required.

<br/><br/><br/>

**G.Mahesh**  
**[Register No]**  

***

<div page-break-after="always"></div>

# **DOCUMENTATION REPORT**
# **TABLE OF CONTENTS**

```
1. Certificate from the Industry / Organization ................................................................ III
2. Declaration by the Student .................................................................................... IV
3. Acknowledgement ............................................................................................... V
4. Introduction & Objectives ................................................................................... 1
   4.1 About the Internship / Project Program ............................................................. 2
   4.2 Objectives of the Project ........................................................................... 2
5. Cloud Service Model Theory & Profile .................................................................... 4
   5.1 Overview of 3-Tier Architecture .................................................................... 4
   5.2 Infrastructure as a Service (IaaS) ................................................................ 5
   5.3 Platform as a Service (PaaS) ...................................................................... 6
   5.4 Cloud Object Storage .............................................................................. 7
6. System Architecture & Tier Mapping Details ........................................................... 8
   6.1 Presentation Tier (PaaS Frontend) ................................................................ 9
   6.2 Application Tier (IaaS Backend REST API) ........................................................ 10
   6.3 Data Tier (PaaS MySQL Database) ................................................................. 11
   6.4 Storage Layer (Cloud Object Store) ............................................................... 12
7. Technical Details & Implementation Code ........................................................... 13
   7.1 Database Schema & Seed SQL .................................................................... 13
   7.2 Backend Express REST API Server .................................................................. 15
   7.3 Frontend React Vite Components .................................................................. 18
   7.4 Infrastructure-as-Code (Terraform & VM Bootstrap) ................................................. 22
   7.5 Docker Container Orchestration .................................................................. 24
8. Output Showcase & System Screenshots ................................................................. 26
9. Advantages and Disadvantages ........................................................................... 30
10. Conclusion & Future Enhancements .................................................................... 32
11. References / Bibliography .............................................................................. 33
```

***

<div page-break-after="always"></div>

# **1. INTRODUCTION & OBJECTIVES**

## **1.1 About the Project / Internship Program**
Under the guidance of the **Department of Computer Science and Engineering, ANITS (Anil Neerukonda Institute of Technology and Sciences)**, in collaboration with the **IBM ICE / Q2D PEARL Cloud Computing Internship Program**, this project implements a full production-grade 3-tier e-commerce platform titled **"CloudMart"**.

## **1.2 Objectives of the Project**
1. **Architect** a 3-tier enterprise cloud application with distinct Presentation, Application, and Data layers.
2. **Map Presentation Tier (Frontend)** to **Platform as a Service (PaaS)** (React 18 + Vite SPA deployed on managed static edge CDN for sub-100ms asset delivery).
3. **Map Application Tier (Backend REST API)** to **Infrastructure as a Service (IaaS)** (Node.js + Express REST API running on an Ubuntu Virtual Machine with systemd daemon management and Nginx reverse proxy tuning).
4. **Map Data Tier (Database)** to **PaaS / DBaaS** (Managed MySQL 8.0 with automated backup policies, point-in-time recovery, and multi-AZ replication).
5. **Map Media Assets** to **Cloud Object Storage** (Decoupled AWS S3 / GCP Cloud Storage with INR ₹ price formatting).

***

<div page-break-after="always"></div>

# **2. CLOUD SERVICE MODEL THEORY**

## **2.1 Overview of 3-Tier Architecture**
- **Presentation Tier**: Renders user interface, handles browser routing, and collects customer input.
- **Application Tier**: Executes business logic, verifies JWT bearer tokens, and processes orders.
- **Data Tier**: Enforces relational ACID compliance and persists user/product records.

## **2.2 Infrastructure as a Service (IaaS)**
Provides raw virtualized compute instances. Customer maintains OS configuration, Nginx web server tuning, security group firewalls (`iptables`), and daemon execution (`systemd`).

## **2.3 Platform as a Service (PaaS)**
Abstracts OS administration and runtime environment. Used for Presentation static web hosting and Managed MySQL Database (DBaaS).

## **2.4 Cloud Object Storage**
Provides 11 9's durability for decoupled product media assets.

***

<div page-break-after="always"></div>

# **3. TECHNICAL DETAILS & IMPLEMENTATION CODE**

### **3.1 Database Tier (MySQL PaaS Schema DDL)**
```sql
CREATE DATABASE IF NOT EXISTS ecommerce_db;
USE ecommerce_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    role ENUM('customer', 'admin') DEFAULT 'customer'
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    category VARCHAR(50) NOT NULL,
    image_url VARCHAR(500) NOT NULL
);
```

### **3.2 Backend Express REST API Server (server.js)**
```javascript
const express = require('express');
const cors = require('cors');
const app = express();

app.use(cors());
app.use(express.json());

app.get('/api/health', (req, res) => {
  res.json({ status: 'healthy', tier: 'IaaS Backend VM' });
});

app.listen(5000, () => console.log('IaaS REST API Server running on port 5000'));
```

***

<div page-break-after="always"></div>

# **4. OUTPUT SHOWCASE & SYSTEM SCREENSHOTS**

### **4.1 Product Catalog UI (PaaS Presentation Tier with INR ₹ Prices)**
- **Cloud Tier Banner**: Displays live architecture mapping badges.
- **Product Cards**: High Performance Laptop (₹1,05,999.00), Wireless Headphones (₹15,990.00), Office Chair (₹19,999.00), 4K Curved Monitor (₹39,999.00), Mechanical Keyboard (₹9,499.00), Gaming Mouse (₹5,499.00).

```
[ INSERT PRODUCT CATALOG SCREENSHOT HERE ]
```

### **4.2 Shopping Cart & Checkout Interface**
- Interactive cart calculating subtotal in Indian Rupees (₹).
- Checkout order placement invoking IaaS REST API transaction engine.

```
[ INSERT CHECKOUT SCREENSHOT HERE ]
```

***

<div page-break-after="always"></div>

# **5. ADVANTAGES AND DISADVANTAGES**

### **Advantages**
1. **Optimal Tier Separation**: Prevents bottlenecking by placing UI on edge CDN and compute on dedicated VMs.
2. **Zero Database Maintenance**: DBaaS/PaaS eliminates DBA overhead for manual backup scripts.
3. **Cost Control**: IaaS compute nodes allow selecting reserved VM instances.
4. **High Asset Durability**: Cloud Object Storage provides 11 9's durability for product media.

### **Disadvantages**
1. **Multi-Model Complexity**: Requires Infrastructure-as-Code (IaC) tooling.
2. **Cross-Tier Latency**: Network latency between IaaS VM and PaaS MySQL DB must be minimized via VPC subnets.

***

<div page-break-after="always"></div>

# **6. CONCLUSION & REFERENCES**

### **Conclusion**
In the culmination of this documentation, we celebrate the creation of **CloudMart** — a 3-tier e-commerce cloud platform. The project proves that mapping Frontend to PaaS, Backend to IaaS, Database to PaaS MySQL, and Media to Cloud Object Storage yields optimal performance, security, and operational efficiency.

### **References**
1. Mell, P., & Grance, T. (2011). *The NIST Definition of Cloud Computing*. NIST Special Publication 800-145.
2. ANITS Department of Computer Science & Engineering Documentation.
3. IBM ICE / Q2D PEARL Cloud Computing Internship Program (2026).

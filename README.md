# 🔐 Secure Health System — Role-Based Access Control for Medical Records

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-RBAC%20%7C%20Encryption-red?style=for-the-badge&logo=shieldsdotio&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)

---

## 📌 Project Overview

**Secure Health System** is a command-line application that demonstrates **enterprise-grade security principles** applied to a medical records management system. It implements the core pillars of information security — **Authentication, Authorisation, Confidentiality, and Integrity** — in a Python-based health records context.

---

## 🛡️ Security Features

| Pillar | Implementation |
|--------|----------------|
| **Authentication** | Username/password login with hashed credentials |
| **Authorisation** | Role-Based Access Control (RBAC) — Group H vs. standard users |
| **Confidentiality** | Data encryption/decryption for sensitive records |
| **Integrity** | SHA hash generation and verification for all retrieved data |
| **Access Control** | Query and update permissions enforced per user group |

---

## 🏗️ System Architecture

```
main.py
  ├── db_setup.py          → Initialise SQLite database schema
  ├── authentication.py    → User initialisation & login validation
  ├── access_control.py    → Role-based query & update operations
  ├── confidentiality.py   → Encrypt / decrypt patient record data
  └── integrity.py         → SHA hash generation & verification
```

---

## 👥 User Roles

| Group | Permissions |
|-------|------------|
| **Group H** (Healthcare) | View records + Update records |
| **Standard Users** | View records only |

---

## 🖥️ Application Flow

```
Start → Database Initialisation
      → User Authentication (username + password)
      → Role Detection (Group H or Standard)
      → Menu Display (role-appropriate options)
      → Record Query → Hash Verification → Display
      → (Group H only) Record Update
```

---

## 📁 Project Structure

```
secure_health/
│
├── main.py              # Application entry point & menu loop
├── db_setup.py          # Database schema initialisation
├── authentication.py    # User management & login
├── access_control.py    # RBAC query & update logic
├── confidentiality.py   # Data encryption & decryption
├── integrity.py         # Hash generation & verification
├── requirements.txt     # Dependencies
└── README.md
```

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/homeshwarnelakurthi/secure_health.git
cd secure_health
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python main.py
```

### 4. Login with test credentials
```
Username: [as configured in authentication.py]
Password: [as configured in authentication.py]
```

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.8+ | Core language |
| SQLite | Lightweight embedded database |
| hashlib | SHA integrity hashing |
| cryptography / Fernet | Data encryption |

---

## 👨‍💻 Author

**Homeswar Rao Nelakurthi**
[![GitHub](https://img.shields.io/badge/GitHub-homeshwarnelakurthi-181717?style=flat&logo=github)](https://github.com/homeshwarnelakurthi)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

# 🔐 Password Security Analyzer & Hashing System

A professional web-based Password Security Analyzer developed using Flask that helps users evaluate password strength, generate secure password hashes, analyze security risks, and download detailed PDF reports.

The system provides a complete password security assessment dashboard with user authentication, password policy validation, cryptographic hashing algorithms, analytics, and report generation.

---

## 🚀 Features

### 👤 User Authentication

* Secure User Registration
* User Login & Logout
* Session Management with Flask-Login
* Multi-User Support

### 🔍 Password Security Analysis

* Password Strength Evaluation
* Password Policy Validation
* Security Recommendations
* Weak Password Detection
* Password Score Calculation

### 🔐 Cryptographic Hashing

* MD5 Hash Generation
* SHA-256 Hash Generation
* SHA-512 Hash Generation
* BCrypt Hash Generation
* Argon2 Hash Generation

### 📊 Analytics Dashboard

* Password Analysis History
* Security Statistics
* User Activity Tracking
* Report Management

### 📄 Reporting

* PDF Report Generation
* Downloadable Security Reports
* Detailed Password Analysis Summary

### 🎨 User Interface

* Professional Dark Theme
* Responsive Design
* Interactive Dashboard
* Modern Flask Web Interface

---

## 🛠️ Technologies Used

| Technology  | Purpose                   |
| ----------- | ------------------------- |
| Python      | Core Programming Language |
| Flask       | Web Framework             |
| SQLite      | Database Management       |
| Flask-Login | User Authentication       |
| SQLAlchemy  | Database ORM              |
| BCrypt      | Secure Password Hashing   |
| Argon2      | Advanced Password Hashing |
| FPDF        | PDF Report Generation     |
| HTML5       | Frontend Structure        |
| CSS3        | Styling                   |
| JavaScript  | Client-Side Functionality |

---

## 📂 Project Structure

```bash
password_security_project/
│
├── app.py
├── database.db
│
├── modules/
│   ├── password_analyzer.py
│   ├── hashing.py
│   ├── reporting.py
│
├── templates/
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│   ├── reports.html
│
├── static/
│   ├── css/
│   ├── js/
│
├── reports/
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/password-security-project.git

cd password-security-project
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
```

### 3️⃣ Activate Environment

**Windows**

```bash
.venv\Scripts\activate
```

**Linux / Mac**

```bash
source .venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Application

```bash
python app.py
```

---

## 🌐 Access Application

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---


## 📸 Project Screenshots

### 🔐 Login Page
![Login Page](screenshots/login-page.png)

### 📊 Dashboard
![Dashboard](screenshots/dashboard.png)

### 📄 Reports Page
![Reports Page](screenshots/reports-page.png)

### 📥 PDF Report
![PDF Report](screenshots/pdf-report.png)

    --------

## 🎯 Learning Outcomes

This project demonstrates:

* Web Application Development with Flask
* User Authentication & Authorization
* Database Integration using SQLAlchemy
* Password Security Principles
* Cryptographic Hashing Techniques
* PDF Report Generation
* Secure Coding Practices
* Cybersecurity Fundamentals

---

## 🔒 Supported Hashing Algorithms

| Algorithm | Purpose                    |
| --------- | -------------------------- |
| MD5       | Basic Hashing              |
| SHA-256   | Secure Hashing             |
| SHA-512   | Advanced Secure Hashing    |
| BCrypt    | Password Storage           |
| Argon2    | Modern Password Protection |

---

## 👩‍💻 Author

**Maria Tariq**

Cybersecurity Enthusiast | BS Information Technology Student

---

## 📜 License

This project is developed for educational and academic purposes.

---

⭐ If you found this project useful, consider giving it a star on GitHub!

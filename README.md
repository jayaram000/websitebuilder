# 🌐 WebsiteBuilder API

WebsiteBuilder is a Django-based backend that enables users to register, authenticate using JWT, and generate personalized business website content. It allows users to manage their generated websites and view HTML previews of their content.

---

## 🚀 Features

- ✅ JWT-based user authentication (email & password)
- 📝 Generate business website content via API
- 🧾 Store and retrieve websites per authenticated user
- 👁️ HTML preview of generated content
- 🧪 Postman collection included for easy testing

---

## 🛠️ Tech Stack

- Python 3.10+
- Django 3.x
- Django REST Framework
- MongoDB using [Djongo](https://www.djongomapper.com/)
- JWT Authentication

---

## ⚙️ Setup Instructions

### 📦 Prerequisites

- Python 3.10+
- MongoDB installed and running locally or on Atlas
- Git, pip

### 🔧 Installation

```bash
# Clone the repo
git clone https://github.com/jayaram000/websitebuilder.git
cd websitebuilder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

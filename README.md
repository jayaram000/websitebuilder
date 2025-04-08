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


API END POINTS

## POST /api/register/
Register a new user.

{
  "email": "user@example.com",
  "password": "yourpassword"
}

## POST /api/login/
Login and receive JWT access & refresh tokens.
{
  "email": "user@example.com",
  "password": "yourpassword"
}

## POST /api/generate/
Generate website content based on business type and industry.

{
  "business_type": "Cafe",
  "industry": "Food & Beverage"
}

## GET /api/websites/
Retrieve all websites created by the currently logged-in user.

## GET /api/websitedetails/<int:pk>/
Retrieve specific website details by ID.
Also supports:

PUT – Update content
DELETE – Delete entry

## GET /api/preview/<uuid:preview_id>/
HTML preview of a generated website using UUID.

# Install dependencies
pip install -r requirements.txt

# 🌐 WebsiteBuilder API

**WebsiteBuilder** is a Django-based backend that enables users to register, authenticate using JWT, and generate personalized business website content. It allows users to manage their generated websites and view HTML previews of the content.

---

## 🚀 Features

✅ JWT-based user authentication (email & password)  
📝 Generate business website content via API  
🧾 Store and retrieve websites per authenticated user  
👁️ HTML preview of generated content  
🧪 Postman collection included for easy testing  

---

## 🛠️ Tech Stack

- Python 3.10+  
- Django 3.x  
- Django REST Framework  
- MongoDB (with Djongo)  
- JWT Authentication  

---

## ⚙️ Setup Instructions

### 📦 Prerequisites

- Python 3.10+  
- MongoDB (local or MongoDB Atlas)  
- Git  
- pip (Python package manager)

---

### 🔧 Installation

```bash
# Clone the repository
git clone https://github.com/jayaram000/websitebuilder.git
cd websitebuilder

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📡 API Endpoints

### 🔐 Authentication

#### POST `/api/register/`  
Register a new user.

**Body:**
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

---

#### POST `/api/login/`  
Login and receive JWT access & refresh tokens.

**Body:**
```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

**Response:**
```json
{
  "access": "your-access-token",
  "refresh": "your-refresh-token"
}
```

Use `access` token in header:  
`Authorization: Bearer <access-token>`

---

### 🏗️ Website Generation

#### POST `/api/generate/`  
Generate website content.

**Body:**
```json
{
  "business_type": "Cafe",
  "industry": "Food & Beverage"
}
```

---

### 📂 Website Management

#### GET `/api/websites/`  
List all websites created by the authenticated user.

---

#### GET `/api/websitedetails/<int:pk>/`  
Retrieve specific website by ID.  
**Also supports:**  
- `PUT` – Update content  
- `DELETE` – Delete website  

---

### 👁️ HTML Preview

#### GET `/api/preview/<uuid:preview_id>/`  
Preview the generated content in raw HTML using UUID.

---

## 📩 Postman Collection

Import the following file into Postman to test all endpoints:  
**`Websitebuilder.postman_collection.json`**


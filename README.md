# 🛒 TechKart - Secure E-Commerce Backend API

## 📌 Overview

TechKart is a secure RESTful E-Commerce Backend API developed using Flask and MySQL. It provides authentication, product management, category management, shopping cart, and order management functionalities using JWT-based authentication.

## 🚀 Features
- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt
- Product CRUD Operations
- Category CRUD Operations
- Shopping Cart Management
- Order Management
- MySQL Database Integration
- Database Migrations using Flask-Migrate

## 🛠 Tech Stack
- Python
- Flask
- MySQL
- SQLAlchemy
- Flask-Migrate
- Flask-JWT-Extended
- bcrypt
- Thunder Client
- Git & GitHub
- 
## 📂 Project Structure

```
TechKart-Ecommerce-Backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── config.py
│   ├── extensions.py
│   └── __init__.py
│
├── migrations/
├── requirements.txt
├── run.py
└── README.md
```
## 🔐 Authentication APIs
| Method | Endpoint |
|---------|----------|
| POST | /register |
| POST | /login |

## 📦 Product APIs
| Method | Endpoint |
|---------|----------|
| POST | /products |
| GET | /products |
| GET | /products/<id> |
| PUT | /products/<id> |
| DELETE | /products/<id> |

## 📁 Category APIs
| Method | Endpoint |
|---------|----------|
| POST | /categories |
| GET | /categories |
| GET | /categories/<id> |
| PUT | /categories/<id> |
| DELETE | /categories/<id> |

## 🛒 Cart APIs
| Method | Endpoint |
|---------|----------|
| POST | /cart |
| GET | /cart |
| DELETE | /cart/<id> |

## 📦 Order APIs
| Method | Endpoint |
|---------|----------|
| POST | /orders |
| GET | /orders |
| GET | /orders/<id> |

## ▶️ Run the Project
```bash
git clone <repository-url>

cd TechKart-Ecommerce-Backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python run.py
```
## 🔮 Future Improvements
- Role-Based Access Control (Admin/User)
- Payment Gateway Integration
- Product Reviews
- Wishlist
- Inventory Management
- Docker Deployment

## 👨‍💻 Author
Developed by **Jaya Hasini Kothapalli**

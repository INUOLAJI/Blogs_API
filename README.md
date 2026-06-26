# Blogs API

A RESTful Blog API built with Django REST Framework, featuring JWT authentication, posts, comments, and likes. Deployed on Render with a Supabase PostgreSQL database.

## 🚀 Live API

**Base URL:** `https://blogs-api-w90z.onrender.com`

**Swagger Docs:** [https://blogs-api-w90z.onrender.com/api/schema/swagger/](https://blogs-api-w90z.onrender.com/api/schema/swagger/)

**ReDoc:** [https://blogs-api-w90z.onrender.com/api/schema/redoc/](https://blogs-api-w90z.onrender.com/api/schema/redoc/)

---

## 🛠 Tech Stack

- **Backend:** Django 4.2, Django REST Framework
- **Auth:** JWT via `djangorestframework-simplejwt`
- **Database:** PostgreSQL (Supabase)
- **Docs:** drf-spectacular (Swagger / ReDoc)
- **Hosting:** Render
- **Static Files:** WhiteNoise

---

## 📦 Features

- User registration and authentication with JWT
- Create, read, update, and delete blog posts
- Comment on posts
- Like/unlike posts
- Auto-generated API documentation (Swagger & ReDoc)
- Token blacklisting on logout

---

## 🔑 Authentication

This API uses JWT Bearer tokens. Include the token in the `Authorization` header:

```
Authorization: Bearer <your_access_token>
```

Access tokens expire after **4 weeks**.

---

## 📌 API Endpoints

### Auth — `/api/auth/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/register/` | Register a new user |
| POST | `/api/auth/login/` | Login and get JWT tokens |
| POST | `/api/auth/logout/` | Blacklist refresh token |
| POST | `/api/auth/token/refresh/` | Refresh access token |

### Posts — `/api/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/posts/` | List all posts |
| POST | `/api/posts/` | Create a post (auth required) |
| GET | `/api/posts/<id>/` | Get a single post |
| PUT/PATCH | `/api/posts/<id>/` | Update a post (auth required) |
| DELETE | `/api/posts/<id>/` | Delete a post (auth required) |

### Comments — `/api/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/comments/` | List all comments |
| POST | `/api/comments/` | Add a comment (auth required) |
| PUT/PATCH | `/api/comments/<id>/` | Update a comment (auth required) |
| DELETE | `/api/comments/<id>/` | Delete a comment (auth required) |

### Likes — `/api/`
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/likes/` | Like a post (auth required) |
| DELETE | `/api/likes/<id>/` | Unlike a post (auth required) |

> For the full list of endpoints with request/response schemas, visit the [Swagger docs](https://blogs-api-w90z.onrender.com/api/schema/swagger/).

---

## ⚙️ Local Setup

### Prerequisites
- Python 3.10+
- PostgreSQL or a Supabase account

### Installation

```bash
# Clone the repo
git clone https://github.com/INUOLAJU/Blogs_API.git
cd Blogs_API

# Create and activate virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DB_NAME=postgres
DB_USER=postgres.your-project-ref
DB_PASS=your-supabase-password
DB_HOST=aws-0-eu-west-1.pooler.supabase.com
DB_PORT=6543
```

### Run the server

```bash
python manage.py migrate
python manage.py runserver
```

API will be available at `http://127.0.0.1:8000/`

---

## 🗂 Project Structure

```
Blogs_API/
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/       # User auth
├── posts/          # Blog posts
├── comments/       # Post comments
├── likes/          # Post likes
├── requirements.txt
├── Procfile
└── manage.py
```

---

## 📄 License

MIT
# Order Management System - Learning Project

A Python-based order management application built with FastAPI to demonstrate clean architecture patterns, database integration, and RESTful API design.

## Project Overview

This is a learning project designed to showcase:
- **Clean Architecture**: Separation of concerns with routers, services, repositories, and models
- **FastAPI Framework**: Building modern async web APIs
- **Database Integration**: Using SQLAlchemy ORM for database operations
- **Data Validation**: Pydantic schemas for request/response validation
- **RESTful Design**: Proper HTTP methods and status codes

## Project Structure

```
ordermanagement/
├── app/
│   ├── main.py                 # Application entry point
│   ├── database/
│   │   └── database.py         # Database configuration and connection
│   ├── models/                 # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── order.py           # Order model
│   │   └── user.py            # User model
│   ├── schemas/               # Pydantic schemas for validation
│   │   ├── order.py           # Order request/response schemas
│   │   └── user.py            # User request/response schemas
│   ├── repositories/          # Data access layer
│   │   ├── order_repository.py
│   │   └── user_repository.py
│   ├── services/              # Business logic layer
│   │   ├── order_service.py
│   │   └── user_service.py
│   └── routers/               # API route handlers
│       ├── orders.py          # Order endpoints
│       └── users.py           # User endpoints
```

### Layer Breakdown

- **Routers**: Handle HTTP requests and responses
- **Services**: Contain business logic and orchestration
- **Repositories**: Handle database operations
- **Models**: Define database table structures
- **Schemas**: Define API request/response validation
- **Database**: Configuration and connection management

## Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository**
   ```bash
   cd ordermanagement
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy python-dotenv
   ```

## Running the Application

Start the development server:

```bash
cd app
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## Key Concepts Demonstrated

### 1. **Repository Pattern**
Abstracting database access into dedicated repository classes for better testability and maintainability.

### 2. **Service Layer**
Encapsulating business logic separate from HTTP handling for reusability across different interfaces.

### 3. **Schema Validation**
Using Pydantic models to validate and serialize API data automatically.

### 4. **Async/Await**
FastAPI's support for asynchronous request handling for improved performance.

### 5. **Dependency Injection**
FastAPI's built-in dependency system for managing database sessions and other resources.

## Learning Goals

This project demonstrates:
- ✅ How to structure a scalable Python backend application
- ✅ Implementing CRUD operations following clean architecture principles
- ✅ Writing testable, maintainable code through proper separation of concerns
- ✅ Building RESTful APIs with FastAPI
- ✅ Database interaction patterns with SQLAlchemy

## Future Enhancements

- Add authentication and authorization
- Implement comprehensive error handling
- Add unit and integration tests
- Add database migrations with Alembic
- Add logging
- Add API rate limiting
- Deploy to production

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI web server

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Clean Architecture in Python](https://www.cosmicpython.com/)

---

**This is a learning project created to understand and practice modern Python backend development patterns.**

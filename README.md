# Order Management System - Learning Project

A Python-based order management application built with FastAPI to demonstrate clean architecture patterns, database integration, and RESTful API design.

## Project Overview

This is a learning project designed to showcase:
- **Clean Architecture**: Separation of concerns with routers, services, repositories, models, and exception handling
- **FastAPI Framework**: Building modern web APIs with type-safe request/response validation
- **Database Integration**: Using SQLAlchemy ORM and PostgreSQL via `DATABASE_URL`
- **Data Validation**: Pydantic schemas for request/response validation
- **RESTful Design**: Proper HTTP methods and status codes

## Project Structure

```
ordermanagement/
├── alembic.ini
├── requirements.txt
├── app/
│   ├── main.py                   # Application entry point
│   ├── core/
│   │   └── dependencies.py       # FastAPI dependency providers
│   ├── database/
│   │   └── database.py           # SQLAlchemy engine and session setup
│   ├── exceptions/
│   │   ├── custom_exceptions.py  # Application exception classes
│   │   └── handlers.py           # Global exception handlers
│   ├── models/                   # SQLAlchemy ORM models
│   │   ├── order.py              # Order model
│   │   └── user.py               # User model
│   ├── schemas/                  # Pydantic schemas for validation
│   │   ├── order.py              # Order request/response schemas
│   │   └── user.py               # User request/response schemas
│   ├── repositories/             # Data access layer
│   │   ├── order_repository.py
│   │   └── user_repository.py
│   ├── services/                 # Business logic layer
│   │   ├── order_service.py
│   │   └── user_service.py
│   ├── routers/                  # API route handlers
│   │   ├── orders.py             # Order endpoints
│   │   └── users.py              # User endpoints
│   └── utils/
│       └── decorators.py         # Helpers such as logging decorators
```

### Layer Breakdown

- **Routers**: Handle HTTP requests and responses
- **Services**: Contain business logic and orchestration
- **Repositories**: Handle database operations
- **Models**: Define database table structures
- **Schemas**: Define API request/response validation
- **Exceptions**: Convert business errors into consistent API responses
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

2. **Create and activate a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the database**
   Create a `.env` file or export `DATABASE_URL` before running the app.
   Example:
   ```bash
   export DATABASE_URL="postgresql://user:password@localhost:5432/dbname"
   ```

## Running the Application

Start the development server from the repository root:

```bash
python -m uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## API Endpoints

### Users
- `POST /users/` - Create a new user
- `GET /users/` - Get all users
- `GET /users/{user_id}` - Get a user by ID
- `PUT /users/{user_id}` - Update a user
- `DELETE /users/{user_id}` - Delete a user

### Orders
- `POST /orders/` - Create a new order
- `GET /orders/` - Get all orders
- `GET /orders/{order_id}` - Get an order by ID
- `PUT /orders/{order_id}` - Update an order
- `DELETE /orders/{order_id}` - Delete an order
- `GET /orders/user/{user_id}` - Get orders for a specific user

## Key Concepts Demonstrated

### 1. **Repository Pattern**
Abstracting database access into dedicated repository classes for better testability and maintainability.

### 2. **Service Layer**
Encapsulating business logic separate from HTTP handling for reusability across different interfaces.

### 3. **Schema Validation**
Using Pydantic models to validate and serialize API data automatically.

### 4. **Dependency Injection**
FastAPI's dependency system is used to inject database sessions and services.

### 5. **Custom Exception Handling**
Application-defined exceptions are translated into JSON responses with consistent status codes.

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
- Support database migrations with Alembic
- Add logging
- Add API rate limiting
- Deploy to production

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **SQLAlchemy**: SQL toolkit and ORM
- **Pydantic**: Data validation using Python type annotations
- **Uvicorn**: ASGI web server
- **python-dotenv**: Environment variable loading

## Resources

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Clean Architecture in Python](https://www.cosmicpython.com/)

---

**This is a learning project created to understand and practice modern Python backend development patterns.**

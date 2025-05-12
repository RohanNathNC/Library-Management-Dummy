# Library Management System

A simple FastAPI application for managing a library's books and users.

## Features

- Add and list books
- Add and list users
- Borrow and return books
- Handle missing books and users gracefully

## Getting Started

1. Clone the repo or download the ZIP.
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the server:
    ```bash
    uvicorn main:app --reload
    ```
4. Access the API at:
    - Swagger UI: http://127.0.0.1:8000/docs
    - ReDoc: http://127.0.0.1:8000/redoc

## Example

- Add a book using POST `/books/`
- Add a user using POST `/users/`
- Borrow a book using POST `/borrow/`
- Return a book using POST `/return/`


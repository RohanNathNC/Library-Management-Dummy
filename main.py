from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    available: bool = True

class User(BaseModel):
    id: int
    name: str
    borrowed_books: List[int] = []

books_db: Dict[int, Book] = {}
users_db: Dict[int, User] = {}

@app.get("/")
async def home():
    return {"message": "📚 Welcome to the Library Management System!"}

@app.post("/books/")
async def add_book(book: Book):
    if book.id in books_db:
        raise HTTPException(status_code=400, detail="Book already exists")
    books_db[book.id] = book
    return {"message": "Book added successfully"}

@app.get("/books/")
async def list_books():
    return list(books_db.values())

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    book = books_db.get(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/users/")
async def add_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User already exists")
    users_db[user.id] = user
    return {"message": "User added successfully"}

@app.get("/users/")
async def list_users():
    return list(users_db.values())

@app.get("/users/{user_id}")
async def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/borrow/")
async def borrow_book(user_id: int, book_id: int):
    user = users_db.get(user_id)
    book = books_db.get(book_id)
    if not user or not book:
        raise HTTPException(status_code=404, detail="User or Book not found")
    if not book.available:
        raise HTTPException(status_code=400, detail="Book is already borrowed")
    user.borrowed_books.append(book_id)
    book.available = False
    return {"message": f"'{book.title}' borrowed by {user.name}"}

@app.post("/return/")
async def return_book(user_id: int, book_id: int):
    user = users_db.get(user_id)
    book = books_db.get(book_id)
    if not user or not book:
        raise HTTPException(status_code=404, detail="User or Book not found")
    if book_id not in user.borrowed_books:
        raise HTTPException(status_code=400, detail="User didn't borrow this book")
    user.borrowed_books.remove(book_id)
    book.available = True
    return {"message": f"'{book.title}' returned by {user.name}"}

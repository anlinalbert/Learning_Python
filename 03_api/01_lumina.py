"""
The Challenge: The "Lumina" Library API
Objective: Develop a production-ready RESTful API for a digital library system.

The Requirements:

Endpoints:

Implement a GET endpoint that returns a list of all books in the system.

Implement a POST endpoint that accepts a JSON object (title, author, and year) and stores it in a persistent SQLite database.

Validation: Ensure that the API returns a 422 Unprocessable Entity error if a user tries to add a book without a title.

Persistence: Data must survive a server restart (i.e., use a database file, not a Python list).

Documentation: The API must be self-documenting (FastAPI does this automatically via Swagger UI).

Deployment (Stretch Goal): Host the finished API on a platform like Render, Railway, or Fly.io.
"""

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, Session, declarative_base

from pydantic import BaseModel, ConfigDict
from typing import Optional, List

app = FastAPI(title="Lumina")

# Database setup
engine = create_engine("sqlite:///library.db", connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    year = Column(Integer)

Base.metadata.create_all(engine)

# Pydantic models
class CreateBook(BaseModel):
    title: str
    author: str
    year: int

class UserResponse(BaseModel):
    id: int
    title: str
    author: str
    year: int

    model_config = ConfigDict(from_attributes=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoints
@app.get("/")
def read_root():
    return {"message": "Hello World!"}

@app.get("/books/{book_id}", response_model=UserResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@app.post("/books", response_model=UserResponse)
def add_book(book: CreateBook, db: Session = Depends(get_db)):

    # Create book
    new_book = Book(**book.model_dump())
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.put("/books/{book_id}", response_model=UserResponse)
def update_book(book_id: int, book: CreateBook, db: Session = Depends(get_db)):
    updated_book = db.query(Book).filter(Book.id == book_id).first()
    if not updated_book:
        raise HTTPException(status_code=404, detail="Book not found")

    for field, value in book.model_dump().items():
        setattr(updated_book, field, value)

    db.commit()
    db.refresh(updated_book)
    return updated_book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    return {"message": "Book deleted"}

@app.get("/books", response_model=List[UserResponse])
def read_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

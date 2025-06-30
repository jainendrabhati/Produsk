
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database, cache
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=database.engine)

@app.get("/books", response_model=list[schemas.Book])
def read_books(db: Session = Depends(database.get_db)):
    cached = cache.get_books_cache()
    if cached:
        return cached
    books = crud.get_books(db)
    cache.set_books_cache(books)
    return books

@app.post("/books", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(database.get_db)):
    return crud.create_book(db, book)

@app.get("/books/{book_id}/reviews", response_model=list[schemas.Review])
def read_reviews(book_id: int, db: Session = Depends(database.get_db)):
    return crud.get_reviews_by_book(db, book_id)

@app.post("/books/{book_id}/reviews", response_model=schemas.Review)
def create_review(book_id: int, review: schemas.ReviewCreate, db: Session = Depends(database.get_db)):
    return crud.create_review(db, review, book_id)

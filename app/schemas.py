
from pydantic import BaseModel

class ReviewBase(BaseModel):
    content: str

class ReviewCreate(ReviewBase):
    pass

class Review(ReviewBase):
    id: int
    book_id: int

    class Config:
        orm_mode = True

class BookBase(BaseModel):
    title: str

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int
    reviews: list[Review] = []

    class Config:
        orm_mode = True

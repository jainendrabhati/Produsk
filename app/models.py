
from sqlalchemy import Column, Integer, String, Text, ForeignKey, Index
from sqlalchemy.orm import relationship
from app.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    reviews = relationship("Review", back_populates="book")

class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
    book_id = Column(Integer, ForeignKey("books.id"))
    book = relationship("Book", back_populates="reviews")

    __table_args__ = (
        Index('ix_reviews_book_id', 'book_id'),
    )

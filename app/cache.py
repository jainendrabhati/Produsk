
import redis
import json
from dotenv import load_dotenv
import os

load_dotenv()

REDIS_URL = os.getenv("REDIS_URL")
r = redis.Redis.from_url(REDIS_URL)

def get_books_cache():
    try:
        cached = r.get("books")
        if cached:
            return json.loads(cached)
    except:
        return None

def set_books_cache(books):
    try:
        from app.schemas import Book
        r.set("books", json.dumps([Book.from_orm(book).dict() for book in books]))
    except:
        pass

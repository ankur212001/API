from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database_conn import get_mysql_db
from database import books_data
from schemas import book


router = APIRouter(
    prefix="/api/books",
    tags=['Books API']
)

@router.get('/', status_code=200)
def get_all_books(db: Session = Depends(get_mysql_db)):
    try:
        print(books_data.get_all_books(db))
    
    except Exception as e:
        print(e)

    
@router.post('/', status_code=200)
def add_new_book(new_book: book, db: Session = Depends(get_mysql_db)):
    try:
        books_data.post_book(new_book, db)

    except Exception as e:
        print(e)


@router.patch('/{id}', status_code=200)
def update_book(id, updated_book: book, db: Session = Depends(get_mysql_db)):
    try:
        books_data.update_book(id, updated_book, db)

    except Exception as e:
        print(e)

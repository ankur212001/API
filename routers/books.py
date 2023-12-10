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
        books = books_data.get_all_books(db)
        
        data = []
        val = {}
        for book in books:
            val["id"] = book[0]
            val["isbn"] = book[1]
            val["title"] = book[2]
            val["subtitle"] = book[3]
            val["author"] = book[4]
            val["published"] = book[5]
            val["publisher"] = book[6]
            val["pages"] = book[7]
            val["description"] = book[8]
            val["website"] = book[9]

            data.append(val)

        return data

    
    except Exception as e:
        print(e)

    
@router.post('/', status_code=200)
def add_new_book(new_book: book, db: Session = Depends(get_mysql_db)):
    try:
        return books_data.post_book(new_book, db)

    except Exception as e:
        print(e)
        return 


@router.patch('/{id}', status_code=200)
def update_book(id, updated_book: book, db: Session = Depends(get_mysql_db)):
    try:
        return books_data.update_book(id, updated_book, db)

    except Exception as e:
        print(e)

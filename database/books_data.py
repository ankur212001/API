from sqlalchemy.sql import text
from schemas import book

def get_all_books(db):
    query_get_all_books = f"""
                            SELECT * FROM books;
                        """
    
    books = db.execute(text(query_get_all_books))\
                .fetchall()

    return books


def post_book(new_book, db):
    query_check_if_exists = f"""
                                SELECT COUNT(isbn) 
                                FROM books 
                                WHERE isbn = :isbn;
                            """

    query_insert_book = f"""
                            INSERT INTO books (isbn, title, subtitle, author, published, publisher, pages, description, website)
                            VALUES(:isbn, :title, :subtitle, :author, :published, :publisher, :pages, :description, :website)
                        """
    
    b = db.execute(text(query_check_if_exists), {"isbn": new_book.isbn})\
            .fetchall()\
            [0][0]

    if b == 1:
        return "book already exists"
    
    db.execute(text(query_insert_book), new_book.__dict__)

    db.commit()

    return "book added successfully"


def update_book(id, updated_book, db):
    query_check_if_exists = f"""
                                SELECT COUNT(id)
                                FROM books
                                WHERE id = :id
                            """
    
    query_update_book = f"""
                            UPDATE books
                            SET isbn = :isbn, title = :title, subtitle = :subtitle, author = :author, published = :published, publisher = :publisher, pages = :pages, description = :description, website = :website
                            WHERE id = {id}
                        """
    
    b = db.execute(text(query_check_if_exists), {"id": id})\
            .fetchall()\
            [0][0]

    if b == 0:
        return "no such book exists"
    
    db.execute(text(query_update_book), updated_book.__dict__)

    db.commit()


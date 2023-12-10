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
    query_insert_book = f"""
                            INSERT INTO books (isbn, title, subtitle, author, published, publisher, pages, description, website)
                            VALUES(:isbn, :title, :subtitle, :author, :published, :publisher, :pages, :description, :website)
                        """
    
    db.execute(text(query_insert_book), new_book.__dict__)

    db.commit()


def update_book(id, updated_book, db):
    query_update_book = f"""
                            UPDATE books
                            SET isbn = :isbn, title = :title, subtitle = :subtitle, author = :author, published = :published, publisher = :publisher, pages = :pages, description = :description, website = :website
                            WHERE id = {id}
                        """
    
    db.execute(text(query_update_book), updated_book.__dict__)

    db.commit()


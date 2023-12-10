from sqlalchemy import Column, BigInteger, Integer, String
from database_conn import Base
from pydantic import BaseModel

class books(Base):

    __tablename__='books'

    id = Column(Integer, primary_key = True)  
    isbn = Column(BigInteger, nullable = False, unique = True)
    title = Column(String(128), nullable = False)
    subtitle = Column(String(128))
    author = Column(String(512), nullable = False)
    published = Column(String(64), nullable = False)
    publisher = Column(String(128), nullable = False)
    pages = Column(Integer, nullable = False)
    description = Column(String(512), nullable = False)
    website = Column(String(512), nullable = False)

class book(BaseModel):

    isbn: int
    title: str
    subtitle: str
    author: str
    published: str
    publisher: str
    pages: int
    description: str
    website: str

    def __repr__(self):
        print(f"{self.isbn} {self.title} {self.subtitle} {self.author} {self.published} {self.publisher} {self.pages} {self.description} {self.website}")

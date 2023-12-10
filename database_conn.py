from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


# Handle Connection to MySQL database
MSYQL_DATABASE_HOST = os.getenv('MSYQL_DATABASE_HOST')
MYSQL_DATABASE_USER = os.getenv('MYSQL_DATABASE_USER')
MYSQL_DATABASE_PASSWORD = os.getenv('MYSQL_DATABASE_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

# Creating the MYSQL database URL for sqlalchemy
MYSQL_DATABASE_URL = URL.create(
    "mysql+pymysql",
    username = MYSQL_DATABASE_USER,
    password = MYSQL_DATABASE_PASSWORD,
    host = MSYQL_DATABASE_HOST,
    database = MYSQL_DATABASE,
)

mysql_engine = create_engine(
    MYSQL_DATABASE_URL, 
    echo = True,
)

MYSQL_SessionLocal = sessionmaker(
    bind = mysql_engine,
    autocommit = False,
    autoflush = False,
)

# function to return MySQL database instance
def get_mysql_db():
    Base.metadata.create_all(bind = mysql_engine)
    db = MYSQL_SessionLocal()
    try:
        yield db
    finally:
        db.close()
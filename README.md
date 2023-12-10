# API
# To start the API
    1 Setup MySQL server on your local computer.
    2 Add a .env file including:
                    MYSQL_DATABASE_HOST,
                    MYSQL_DATABASE_USER, 
                    MYSQL_DATABASE_PASSWORD, 
                    MYSQL_DATABASE
    3 After this is done run the API using command line by 
        uvicorn main:app --reload
    4 To test the API using a graphical interface press ctrl and 
        visit the /docs route of the link where the API is hosted. 

    Language Used - Python 
    Libraries Used - FastAPI, SQLAlchemy

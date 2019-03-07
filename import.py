# Import all entries from books.csv in postgreSQL Db
import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


def main():
    # create table books
    db.execute("CREATE TABLE books(id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year VARCHAR NOT NULL)")
    db.execute("CREATE TABLE users(id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year VARCHAR NOT NULL)")
    db.execute("CREATE TABLE reviews(id SERIAL PRIMARY KEY, isbn VARCHAR NOT NULL, title VARCHAR NOT NULL, author VARCHAR NOT NULL, year VARCHAR NOT NULL)")

    f = open("books.csv")
    reader = csv.reader(f)
    for isbn, title, author, year in reader:
        db.execute("INSERT INTO books(isbn, title, author, year) VALUES(:isbn, :title, :author, :year)",
                   {"isbn": isbn, "title": title, "author": author, "year": year})

    db.commit()


if __name__ == "__main__":
    main()

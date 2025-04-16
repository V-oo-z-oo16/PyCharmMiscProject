import random
import sqlite3

library = sqlite3.connect("library.db")
cursor = library.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS book(book_id INTEGER PRIMARY KEY, "
               "title TEXT, "
              "author TEXT,"
               "year INTEGER,"
               "pages INTEGER)")
library.commit()
library.close()


def add_book():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    book_id = random.randint(1, 1000)
    title = input("введите название книги: ")
    author = input("введите автора книги: ")
    year = int(input("введите год выпуска книги: "))
    pages = int(input("введите кол-во страниц: "))
    cursor.execute("INSERT INTO book (book_id, title, author, year, pages)"
                        "VALUES (?, ?, ?, ?, ?)", (book_id, title, author, year, pages))
    library.commit()
    library.close()


def show_book():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    cursor.execute("SELECT title FROM book ")
    sbook = cursor.fetchall()
    for books in sbook:
        print(f"название: {''.join(books)}")
    print()
    library.commit()
    library.close()


def find_books_by_author():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    author = input("введите автора: ")
    cursor.execute("SELECT title FROM book WHERE author = ?", (author,))
    show = cursor.fetchall()
    for author in show:
        print(f"название: {''.join(author)}")
    print()
    library.commit()
    library.close()


def update_page_count():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    book_id = int(input("введите id книги: "))
    new_pages = int(input("кол-во страниц: "))
    cursor.execute("UPDATE book SET pages = ? WHERE book_id = ?", (new_pages, book_id))
    library.commit()
    library.close()


def main():
    while True:
        action = int(input("введите действие: "))
        match action:
            case 1:
                add_book()
            case 2:
                show_book()
            case 3:
                find_books_by_author()
            case 4:
                update_page_count()


main()
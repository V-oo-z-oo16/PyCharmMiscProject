import random
import sqlite3
library = sqlite3.connect("library.db")
cursor = library.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS book(book_id INTEGER, "
               "title TEXT, "
              "author TEXT,"
               "year INTEGER,"
               "availabale INTEGER DEFAULT 1)")

cursor.execute("CREATE TABLE IF NOT EXISTS readers (reader_id INTEGER,"
               "name TEXT,"
               "phone INTEGER,"
               "book_id INTEGER)")

library.commit()
library.close()

def add_book():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    book_id = random.randint(1, 1000)
    title = input("введите название книги: ")
    author = input("введите автора книги: ")
    year = input("введите год выпуска книги: ")
    cursor.execute("INSERT INTO book (book_id, title, author, year)"
                   "VALUES (?, ?, ?, ?)", (book_id, title, author, year))
    library.commit()
    library.close()
def add_reader():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    reader_id = random.randint(1, 1000)
    name = input("введите имя: ")
    phone = int(input("введите номер телефона: "))
    cursor.execute("INSERT INTO readers (reader_id, name, phone)"
                   "VALUES (?, ?, ?)", (reader_id, name, phone))
    library.commit()
    library.close()

def give_book():
    library = sqlite3.connect("library.db")
    cursor = library.cursor()
    cursor.execute("UPDATE book SET availabale=? WHERE book_id=?", (0, book_id))
    library.commit()
    library.close()
def return_book():
    pass

while True:
    print("1. добавить книгу\n"
          "2. добавить нового читателя\n"
          "3. получить книгу")
    actions = input("введите номер действия: ")

    match actions:
        case "1":
            add_book()
        case "2":
            add_reader()
        case "3":
            give_book()
            # ен
        case "4":
            pass




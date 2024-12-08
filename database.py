import sqlite3
from typing import Optional, Union

from model import Book


class LibraryManager:
    def __init__(self, db_path: str = "Books.db"):
        """Инициализация класса LibraryManager и подключение к базе данных."""
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self.cur: sqlite3.Cursor = self.conn.cursor()
        self.create_table()

    def create_table(self) -> None:
        """Создает таблицу для хранения данных, если ее еще нет."""
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS library (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            status TEXT NOT NULL
        )
        """)
        self.conn.commit()

    def add_book(self, book: Book) -> None:
        """Добавляет новую книгу в библиотеку."""
        with self.conn:
            self.cur.execute(
                "INSERT INTO library (title, author, year, status) VALUES (?, ?, ?, ?)",
                (book.title, book.author, book.year, book.status),
            )
            self.conn.commit()
            print(f"Книга {book.title} добавлена.")

    def list_books(self, **filters) -> None:
        """Выводит список книг, соответствующих критериям поиска."""
        query: str = "SELECT * FROM library WHERE 1=1"
        parameters: dict[str, Optional[Union[str, int]]] = {}
        filter_conditions = {
            "title": "AND title LIKE :title",
            "author": "AND author LIKE :author",
            "year": "AND year = :year"
        }
        for field, condition in filter_conditions.items():
            if field in filters and filters[field] is not None:
                query += f" {condition}"
                parameters[field] = f"%{filters[field]}%" if field in {"title", "author"} else filters[field]

        self.cur.execute(query, parameters)
        results = self.cur.fetchall()
        books = []
        for result in results:
            book = Book(
                title=result["title"],
                author=result["author"],
                year=result["year"],
                status=result["status"]
            )
            print(book)
            books.append(book)
        return books

    def edit_book(self, book_id: int, status: str) -> None:
        """Изменяет статус книги по ID."""
        with self.conn:
            self.cur.execute("UPDATE library SET status=? WHERE id=?", (status, book_id))
            self.conn.commit()
            print(f"Статус книги с ID {book_id} изменен.")

    def remove_book(self, book_id: int) -> None:
        """Удаляет книгу по ID."""
        with self.conn:
            self.cur.execute("DELETE FROM library WHERE id=?", (book_id,))
            self.conn.commit()
            print(f"Книга с ID {book_id} удалена.")

    def close(self) -> None:
        """Закрывает соединение с базой данных."""
        self.conn.close()

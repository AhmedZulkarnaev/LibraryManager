import sqlite3
from typing import Optional

from model import Book


class LibraryManager:
    def __init__(self, db_path: str = "Books.db"):
        """Инициализация класса LibraryManager и подключение к базе данных."""
        self.conn: sqlite3.Connection = sqlite3.connect(db_path)
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

    def list_books(self, title: Optional[str] = None, author: Optional[str] = None, year: Optional[int] = None) -> None:
        """Выводит список книг, соответствующих критериям поиска."""
        query: str = "SELECT * FROM library WHERE 1=1"
        parameters: dict[str, Optional[str | int]] = {}

        if title:
            query += " AND title LIKE :title"
            parameters["title"] = f"%{title}%"
        if author:
            query += " AND author LIKE :author"
            parameters["author"] = f"%{author}%"
        if year:
            query += " AND year = :year"
            parameters["year"] = year

        with self.conn:
            self.cur.execute(query, parameters)
            books: list[tuple[int, str, str, int, str]] = self.cur.fetchall()
            if not books:
                print("\nНет книг, соответствующих заданным параметрам.\n")
            else:
                headers = ["ID", "Название", "Автор", "Год", "Статус"]
                column_widths = [max(len(str(row[i])) for row in books + [headers]) for i in range(len(headers))]
                row_format = " | ".join(f"{{:<{width}}}" for width in column_widths)
                print("\n" + "=" * (sum(column_widths) + len(headers) * 3 - 1))
                print(row_format.format(*headers))
                print("=" * (sum(column_widths) + len(headers) * 3 - 1))
                for book in books:
                    print(row_format.format(*book))
                print("=" * (sum(column_widths) + len(headers) * 3 - 1) + "\n")

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

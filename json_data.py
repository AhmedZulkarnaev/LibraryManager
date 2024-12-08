import json
from typing import List

from model import Book


def save_books_to_json(books: List[Book], file_path: str):
    """Сохраняет задачи в файл JSON."""
    with open(file_path, "w", encoding="utf-8") as file:
        books_list = []
        for i, book in enumerate(books, start=1):
            task_dict = {
                "id": i,
                "title": book.title,
                "author": book.author,
                "date": book.year,
                "status": book.status
            }
            books_list.append(task_dict)
        json.dump(books_list, file, ensure_ascii=False, indent=4)

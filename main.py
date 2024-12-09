from typing import Optional
from datetime import datetime

from database import LibraryManager, Book
from json_data import save_books_to_json


def main() -> None:
    """Основная функция приложения."""
    manager: LibraryManager = LibraryManager()
    print("Добро пожаловать в управление библиотекой!")
    print("Команды:")
    print("  add - добавить книгу")
    print("  list - показать список книг")
    print("  edit - изменить статус книги")
    print("  remove - удалить книгу по ID")
    print("  exit - выйти из программы")

    while True:

        command: str = input("\nВведите команду: ").lower()

        if command == "add":
            try:
                title: str = input("Введите название книги: ")
                author: str = input("Введите автора книги: ")
                year: int = int(input("Введите год издания(формат YYYY): "))
                book: Book = Book(title, author, year)
                manager.add_book(book)
            except ValueError:
                print("Год издания должен быть числом.")

        elif command == "list":
            print("Введите одно из ключевых слов, книги которых вы хотите найти, иначе пропустите")
            title: Optional[str] = input("Введите название книги: ") or None
            author: Optional[str] = input("Введите автора книги: ") or None
            year: Optional[str] = input("Введите год издания: ") or None
            year_int: Optional[int] = int(year) if year else None
            books = manager.list_books(title=title, author=author, year=year_int)
            if not books:
                print("\nНет книг, соответствующих заданным параметрам.\n")
            print("\nСписок найденных книг:")
            headers = ["ID", "Название", "Автор", "Год", "Статус"]
            print("=" * 70)
            print("{:<5} | {:<20} | {:<20} | {:<5} | {:<15}".format(*headers))
            print("=" * 70)
            for idx, book in enumerate(books, start=1):
                print(
                    "{:<5} | {:<20} | {:<20} | {:<5} | {:<15}".format(
                        book.id, book.title, book.author, book.year, book.status
                    )
                )
            print("=" * 70)

        elif command == "edit":
            try:
                book_id: int = int(input("Введите ID книги для изменения: "))
                status: str = input("Введите новый статус книги: ")
                manager.edit_book(book_id, status)
            except ValueError:
                print("id должен быть числом типа int")

        elif command == "remove":
            try:
                book_id: int = int(input("Введите ID книги для удаления: "))
                manager.remove_book(book_id)
            except ValueError:
                print("id должен быть числом типа int")

        elif command == "exit":
            print("Выход из программы.")
            manager.close()
            save_books_to_json(books, "library.json")
            break
        else:
            print("Неизвестная команда. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()

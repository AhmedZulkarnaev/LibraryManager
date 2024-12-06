from typing import Optional

from database import LibraryManager, Book


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
            title: str = input("Введите название книги: ").strip()
            author: str = input("Введите автора книги: ").strip()
            year: str = input("Введите год издания: ").strip()
            status: str = "в наличии"
            try:
                year_int: int = int(year)
                book: Book = Book(title, author, year_int, status)
                manager.add_book(book)
            except ValueError:
                print("Год издания должен быть числом.")

        elif command == "list":
            print("Введите одно из ключевых слов, книги которых вы хотите найти, иначе пропустите")
            title: Optional[str] = input("Введите название книги: ") or None
            author: Optional[str] = input("Введите автора книги: ") or None
            year: Optional[str] = input("Введите год издания: ") or None
            year_int: Optional[int] = int(year) if year else None
            manager.list_books(title=title, author=author, year=year_int)

        elif command == "edit":
            try:
                book_id: int = int(input("Введите ID книги для изменения: ").strip())
                status: str = input("Введите новый статус книги: ").strip()
                manager.edit_book(book_id, status)
            except ValueError:
                print("ID должен быть числом.")

        elif command == "remove":
            try:
                book_id: int = int(input("Введите ID книги для удаления: ").strip())
                manager.remove_book(book_id)
            except ValueError:
                print("ID должен быть числом.")

        elif command == "exit":
            print("Выход из программы.")
            manager.close()
            break

        else:
            print("Неизвестная команда. Пожалуйста, попробуйте снова.")


if __name__ == "__main__":
    main()

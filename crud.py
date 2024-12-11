import json
from model import Book


class Library:
    """
    Класс для управления библиотекой книг. Он предоставляет функциональность
    для добавления, удаления, поиска и изменения статуса книг в библиотеке, а также
    для сохранения и загрузки данных о книгах в/из JSON файла.

    Атрибуты:
        filename (str): Имя файла, в котором хранится база данных библиотеки. По умолчанию "library.json".
        books (list): Список книг, загруженных из файла.
    """

    def __init__(self, filename="library.json"):
        """
        Инициализация объекта библиотеки.

        Аргументы:
            filename (str): Имя файла для загрузки и сохранения данных (по умолчанию "library.json").
        """
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """
        Загружает книги из файла в формате JSON.

        Возвращает:
            list: Список объектов Book, загруженных из файла. Если файл не найден или данные повреждены, возвращает пустой список.
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return [Book(**book) for book in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_books(self):
        """
        Сохраняет список книг в файл в формате JSON.
        """
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump([book.__dict__ for book in self.books], file, ensure_ascii=False, indent=4)

    def add_book(self, title, author, year):
        """
        Добавляет новую книгу в библиотеку.

        Аргументы:
            title (str): Название книги.
            author (str): Автор книги.
            year (int): Год издания книги.
        """
        new_book = Book(title, author, year)
        new_book.id = len(self.books) + 1  # Генерация уникального ID
        self.books.append(new_book)
        self.save_books()

    def delete_book(self, book_id):
        """
        Удаляет книгу по ID.

        Аргументы:
            book_id (int): ID книги, которую необходимо удалить.

        Вывод:
            Сообщение об ошибке, если книга с данным ID не найдена.
        """
        book = self.find_book_by_id(book_id)
        if book:
            self.books.remove(book)
            self.save_books()
        else:
            print("Книга с таким id не найдена.")

    def find_books(self, search_term):
        """
        Ищет книги по строке поиска (название, автор или год).

        Аргументы:
            search_term (str): Строка поиска.

        Возвращает:
            list: Список книг, удовлетворяющих поисковому запросу.
        """
        results = []
        for book in self.books:
            if (search_term.lower() in book.title.lower() or
                    search_term.lower() in book.author.lower() or
                    search_term.lower() in str(book.year)):
                results.append(book)
        return results

    def find_book_by_id(self, book_id):
        """
        Ищет книгу по ID.

        Аргументы:
            book_id (int): ID книги.

        Возвращает:
            Book: Книга с данным ID, если она найдена, иначе None.
        """
        for book in self.books:
            if book.id == book_id:
                return book
        return None

    def update_status(self, book_id, new_status):
        """
        Обновляет статус книги по ID.

        Аргументы:
            book_id (int): ID книги, статус которой нужно обновить.
            new_status (str): Новый статус книги ("в наличии" или "выдана").

        Вывод:
            Сообщение об ошибке, если книга с данным ID не найдена или статус некорректен.
        """
        book = self.find_book_by_id(book_id)
        if book:
            if new_status in ["в наличии", "выдана"]:
                book.status = new_status
                self.save_books()
            else:
                print("Некорректный статус.")
        else:
            print("Книга с таким id не найдена.")

    def display_books(self):
        """
        Выводит список всех книг в библиотеке.

        Если книг нет, выводится сообщение о пустоте библиотеки.
        """
        if self.books:
            for book in self.books:
                print(
                    f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Year: {book.year}, Status: {book.status}")
        else:
            print("В библиотеке нет книг.")



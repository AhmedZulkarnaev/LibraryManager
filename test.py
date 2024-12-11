import pytest
from unittest.mock import patch, mock_open
from crud import Library

class TestLibrary:
    @pytest.fixture
    def mock_library(self):
        """Создаёт объект библиотеки с поддельным файлом"""
        with patch("builtins.open", mock_open(read_data="[]")):
            library = Library("test_library.json")
        return library

    def test_load_books_empty(self, mock_library):
        """Тест на загрузку пустого списка книг"""
        assert mock_library.books == []

    def test_add_book(self, mock_library):
        """Тест добавления книги"""
        mock_library.add_book("Python Programming", "Mark Lutz", 2023)
        assert len(mock_library.books) == 1
        book = mock_library.books[0]
        assert book.title == "Python Programming"
        assert book.author == "Mark Lutz"
        assert book.year == 2023
        assert book.status == "в наличии"

    def test_delete_book(self, mock_library):
        """Тест удаления книги"""
        mock_library.add_book("Python Programming", "Mark Lutz", 2023)
        book_id = mock_library.books[0].id
        mock_library.delete_book(book_id)
        assert len(mock_library.books) == 0

    def test_find_books(self, mock_library):
        """Тест поиска книг"""
        mock_library.add_book("Python Programming", "Mark Lutz", 2023)
        mock_library.add_book("Learn Java", "John Doe", 2021)
        results = mock_library.find_books("Python")
        assert len(results) == 1
        assert results[0].title == "Python Programming"

    def test_find_book_by_id(self, mock_library):
        """Тест поиска книги по ID"""
        mock_library.add_book("Python Programming", "Mark Lutz", 2023)
        book_id = mock_library.books[0].id
        book = mock_library.find_book_by_id(book_id)
        assert book is not None
        assert book.title == "Python Programming"

    def test_update_status(self, mock_library):
        """Тест обновления статуса книги"""
        mock_library.add_book("Python Programming", "Mark Lutz", 2023)
        book_id = mock_library.books[0].id
        mock_library.update_status(book_id, "выдана")
        book = mock_library.find_book_by_id(book_id)
        assert book.status == "выдана"

    def test_display_books(self, mock_library, capsys):
        """Тест отображения книг"""
        mock_library.add_book("Python Programming", "Mark Lutz", 2023)
        mock_library.display_books()
        captured = capsys.readouterr()
        assert "Python Programming" in captured.out
        assert "Mark Lutz" in captured.out
        assert "2023" in captured.out

class Book:
    """Модель данных Book."""
    def __init__(self, title: str, author: str, year: int, status: str = "В наличии", book_id: int = None):
        self.id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

class Book:
    """Модель данных Book."""
    def __init__(self, title, author, year, status="В наличии"):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

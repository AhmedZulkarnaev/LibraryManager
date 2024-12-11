class Book:
    def __init__(self, title: str, author: str, year: int, status="в наличии", id=None):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status


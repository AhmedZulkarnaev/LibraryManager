from typing import NamedTuple


class Book(NamedTuple):
    """Модель Book."""
    title: str
    author: str
    year: int
    status: str

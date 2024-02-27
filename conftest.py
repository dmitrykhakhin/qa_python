from main import BooksCollector

import pytest


# Фикстура collector для создания экземпляра класса BooksCollector:
@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

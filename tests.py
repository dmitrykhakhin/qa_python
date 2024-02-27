from main import BooksCollector

import pytest


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_add_one_book_len_books_genre1(self, collector):
        collector.add_new_book('Мастер и Маргарита')

        # Проверяем, что метод add_new_book добавил одну книгу в словарь books_genre
        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_41characters_name_len_books_genre0(self, collector):
        collector.add_new_book('Звездная ночь: Путешествие во Вселенную 2')

        # Проверяем, что метод add_new_book не добавил книгу с названием длинной 41 символ в словарь books_genre
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_random_valid_genre_book_has_genre(self, collector, genre):
        new_book_name = 'Обо всём'
        collector.add_new_book(new_book_name)
        collector.set_book_genre(new_book_name, genre)

        # Проверяем, что метод set_book_genre добавил один из доступных жанров
        assert collector.get_book_genre(new_book_name) == genre

    def test_set_book_genre_invalid_genre_book_has_no_genre(self, collector):
        new_book_name = 'Я помню чудное мгновенье…'
        collector.add_new_book(new_book_name)
        collector.set_book_genre(new_book_name, 'Лирика')

        # Проверяем, что метод set_book_genre НЕ добавил жанр,
        # которого нет в списке genre конструктора класса BooksCollector
        assert collector.get_book_genre(new_book_name) == ''

    def test_get_book_genre_valid_book_name_genre_name(self, collector):
        new_book_name = 'Собака Баскервилей'
        genre_name = 'Детективы'
        collector.add_new_book(new_book_name)
        collector.set_book_genre(new_book_name, genre_name)

        # Проверяем, что метод get_book_genre возвращает название жанра по названию книги
        assert collector.get_book_genre('Собака Баскервилей') == genre_name

    def test_get_books_with_specific_genre_name_of_genre_book_list(self, collector):
        book_dict = {
            'Война миров': 'Фантастика',
            'Убийство в "Восточном экспрессе': 'Детективы',
            'Марсианин': 'Фантастика',
            'Король Лев': 'Мультфильмы',
            'По следам преступления': 'Детективы'
        }

        for book, genre in book_dict.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        genre_name = 'Детективы'
        expected_book_list = ['Убийство в "Восточном экспрессе', 'По следам преступления']

        # Проверяем получение списка книг по названию жанра
        assert collector.get_books_with_specific_genre(genre_name) == expected_book_list

    def test_get_books_genre_add_two_books_dict_len2(self, collector):
        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.add_new_book('Убийство в "Восточном экспрессе')

        # Проверяем, что метод get_books_genre вернул словарь и размер словаря соответствует кол-ву добавленных книг
        assert type(collector.get_books_genre()) == dict and len(collector.get_books_genre()) == 2

    def test_get_books_for_children_add_different_books_children_book_list(self, collector):
        book_dict = {
            'Двенадцать стульев': 'Комедии',
            'Убийство в "Восточном экспрессе': 'Детективы',
            'Марсианин': 'Фантастика',
            'Король Лев': 'Мультфильмы'
        }

        for book, genre in book_dict.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        expected_children_books_list = ['Двенадцать стульев', 'Марсианин', 'Король Лев']

        # Проверяем, что метод get_books_for_children вернул корректный список
        assert collector.get_books_for_children() == expected_children_books_list

    def test_add_book_in_favorites_add_one_favorite_book_of_two_list_with_one_book(self, collector):
        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.add_new_book('Убийство в "Восточном экспрессе')

        collector.add_book_in_favorites('Война миров')

        # Проверяем, что метод add_book_in_favorites добавляет одну из книг в Избранное
        assert collector.get_list_of_favorites_books() == ['Война миров']

    def test_delete_book_from_favorites_add_and_delete_book_from_favorites_len_favorites0(self, collector):
        collector.add_new_book('Убийство в "Восточном экспрессе')
        collector.add_book_in_favorites('Убийство в "Восточном экспрессе')
        collector.delete_book_from_favorites('Убийство в "Восточном экспрессе')

        # Проверяем, что метод delete_book_from_favorites удалил книгу из Избранного
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_get_list_of_favorites_books_add_two_books_to_favorites_list_has_two_book_names(self, collector):
        collector.add_new_book('Война миров')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.add_new_book('Убийство в "Восточном экспрессе')

        collector.add_book_in_favorites('Война миров')
        collector.add_book_in_favorites('Убийство в "Восточном экспрессе')

        expected_list_of_favorites = ['Война миров', 'Убийство в "Восточном экспрессе']

        # Проверяем что метод get_list_of_favorites_books вернул список имен избранных книг
        assert collector.get_list_of_favorites_books() == expected_list_of_favorites














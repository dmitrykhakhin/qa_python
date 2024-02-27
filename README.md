# qa_python

Список реализованных тестов:
1) test_add_new_book_add_one_book_len_books_genre1 - Проверяем, что метод add_new_book добавил одну книгу в словарь books_genre
2) test_add_new_book_41characters_in_the_name_len0 - Проверяем, что метод add_new_book не добавляет книгу с названием длинной 41 символ в словарь books_genre
3) test_set_book_genre_random_valid_genre_book_has_genre - Проверяем, что метод set_book_genre добавляет один из доступных жанров
4) test_set_book_genre_invalid_genre_book_has_no_genre - Проверяем, что метод set_book_genre НЕ добавил жанр, которого нет в списке genre конструктора класса BooksCollector
5) test_get_book_genre_valid_book_name_genre_name - Проверяем, что метод get_book_genre возвращает название жанра по названию книги
6) test_get_books_with_specific_genre_name_of_genre_book_list - Проверяем что метод get_books_with_specific_genre возвращает спискок книг по названию жанра
7) test_get_books_genre_add_two_books_dict_len2 - Проверяем, что метод get_books_genre вернул словарь и размер словаря соответствует кол-ву добавленных книг
8) test_get_books_for_children_add_different_books_children_book_list - Проверяем, что метод get_books_for_children вернул корректный список
9) test_add_book_in_favorites_add_one_favorite_book_of_two_list_with_one_book - Проверяем, что метод add_book_in_favorites добавляет одну из книг в Избранное
10) test_delete_book_from_favorites_add_and_delete_book_from_favorites_len_favorites0 - Проверяем, что метод delete_book_from_favorites удалил книгу из Избранного
11) test_get_list_of_favorites_books_add_two_books_to_favorites_list_has_two_book_names - Проверяем что метод get_list_of_favorites_books вернул список имен избранных книг
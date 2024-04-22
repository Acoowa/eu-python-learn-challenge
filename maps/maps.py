from typing import Union
from functools import reduce


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def get_rate(movie: dict) -> float or None:
            if movie["rating_kinopoisk"] not in ["0", ""] and movie["country"].count(",") >= 1:
                return float(movie["rating_kinopoisk"])
            return None

        list_of_ratings = [
            rating for rating in (map(get_rate, list_of_movies)) if rating is not None
        ]

        return sum(list_of_ratings) / len(list_of_ratings)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def get_name(movie: dict) -> float or None:
            if (
                movie["rating_kinopoisk"] not in ["0", ""]
                and float(movie["rating_kinopoisk"]) > rating
            ):
                return movie["name"]
            return None

        list_of_movies = [movie for movie in (map(get_name, list_of_movies)) if movie is not None]
        count = sum(i.count("и") for i in list_of_movies)
        return count

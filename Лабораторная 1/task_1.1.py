# TODO Написать 3 класса с документацией и аннотацией типов
from typing import Union
import doctest


class Time:

    def __init__(self, hour_: int, minute_: int):
        """
        Формирование времени в формате часы - минуты

        Задаем время
        :param hour_: час в интервале от 0 до 24
        :param minute_: минуты

        Примеры:
        >>> time = Time(20,15)  # инициализация экземпляра класса
        """
        self.hour = None
        self.init_hour_(hour_)

        if not isinstance(minute_, int):
            raise TypeError("Неправильный тип данных")
        if hour_ <= 0:
            raise ValueError("Невозможна отрицательная величина")
        if hour_ >= 24:
            raise ValueError("Значение должно быть меньше 60")
        self.minute = minute_

    def init_hour_(self, hour_):

        """ Проверяет введенное значение времени на корректность
        и принимает значение, если проверки пройдены успешно
        :param hour_: час в интервале от 0 до 24
        :TypeError: введен неправильный тип данных
        :ValueError: если введена отрицательная величина, либо значение больше 24
        :return: если данные введены некорректно - ошибка,
        если проверка пройдена заданное значение часа

        Пример:
        >>> hour = Time(20, 15)
        >>> hour.init_hour_(3)
        """

        if not isinstance(hour_, int):
            raise TypeError("Неправильный тип данных")
        if hour_ <= 0:
            raise ValueError("Невозможна отрицательная величина")
        if hour_ >= 24:
            raise ValueError("Значение должно быть меньше 24")
        self.hour = hour_

    def __str__(self) -> str:
        """ Выдает результат, в отображении, удобном для восприятия пользователем """

        return f"Заданное время: {self.hour} часов {self.minute} минут"


class ListFormat:
    def __init__(self, width: Union[int, float], length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Размер шаблона для печати"

        :param width: ширина в мм
        :param length: длина в мм

        Примеры:
        >>> listF = ListFormat (200,300)  # инициализация экземпляра класса
        """

        if not isinstance(width, (int, float)):
            raise TypeError("Неправильный тип данных")
        if width <= 0:
            raise ValueError("Невозможна отрицательная величина")
        self.width = width

        if not isinstance(length, (int, float)):
            raise TypeError("Неправильный тип данных")
        if width <= 0:
            raise ValueError("Невозможна отрицательная величина")
        self.length = length

        if width > length:
            raise TypeError("width не может быть больше length")

    def increase_length(self, add_mm: int):
        """
        Увеличивает длину шаблона для печати

        :add_mm: размер, на который увеличиваем длину в мм
        :raise ValueError: Если введено отрицательное число вызываем ошибку

        Примеры:
        >>> listF = ListFormat (200,300)
        >>> listF.increase_length(100)

        """

        if add_mm <= 0:
            raise ValueError("Невозможна отрицательная величина")
        self.length += add_mm

    def decrease_length(self, del_mm: int):
        """
        Уменьшает длину шаблона для печати

        :del_mm: размер, на который уменьшаем длину в мм
        :raise ValueError: Если введено отрицательное число или число,
         большее текущей длины, вызываем ошибку

        Примеры:
        >>> listF = ListFormat (200,300)
        >>> listF.decrease_length(100)

        """

        if del_mm <= 0:
            raise ValueError("Невозможна отрицательная величина")
        if del_mm >= self.length:
            raise ValueError("Значение, на которое уменьшаем, должно быть меньше текущей длины")
        self.length -= del_mm


class Dress:
    def __init__(self, name: str, color: str, size: int):
        """
        Создание и подготовка к работе объекта "Одежда"

        :param name: название
        :param color: цвет
        :param size: размер

        Примеры:
        >>> dress = Dress ("платье","зеленое", 44)  # инициализация экземпляра класса
        """

        if not isinstance(name, str):
            raise TypeError("Неверный тип данных")
        if not name.isalpha():
            raise ValueError("Необходимо ввести текст")
        self.name = name

        if not isinstance(color, str):
            raise TypeError("Неверный тип данных")
        if not color.isalpha():
            raise ValueError("Необходимо ввести текст")
        self.color = color

        if not isinstance(size, int):
            raise TypeError("Неправильный тип данных")
        if size <= 0:
            raise ValueError("Невозможна отрицательная величина")
        self.size = size

    def change_color(self, new_color: str):
        """
        Измененяет цвет одежды

        :new_color: новый цвет
        :raise TypeError: Если введен неправильный тип данных, не строка
        :raise ValueError: Если введен не строковй тип

        Примеры:
        >>> dress = Dress ("платье","зеленое", 44)
        >>> dress.change_color("красное")
        """

        if not isinstance(new_color, str):
            raise TypeError("Неверный тип данных")
        if not new_color.isalpha():
            raise ValueError("Необходимо ввести текст")
        self.color = new_color

    def increase_size(self, add: int):
        """
        Увеличивает размер одежды

        :add: величина, на которую увеличиваем размер, должна быть кратна двум
        :raise TypeError: если введен неправильный тип данных
        :raise ValueError: если величина, на которую увеличиваем размер,
        не кратна двум

        Примеры:
        >>> dress = Dress ("платье","зеленое", 44)
        >>> dress.increase_size(4)
        """

        if not isinstance(add, int):
            raise TypeError("Неверный тип данных")
        if not add % 2 == 0:
            raise ValueError("Число должно быть кратно двум")
        self.size += add


if __name__ == "__main__":
    doctest.testmod()


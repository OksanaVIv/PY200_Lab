class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = ={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Неверный тип данных, должно быть целое число")
        if not value > 0:
            raise ValueError("Должно быть положительное значение")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages = ={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, float):
            raise TypeError("Неверный тип данных")
        if not value > 0:
            raise ValueError("Должно быть положительное значение")
        self._pages = value


if __name__ == "__main__":
    a = Book("Книга_1", "Пушкин А.С.")
    b = PaperBook("Книга_2", "Лермонтов М.Ю.", 300)
    c = AudioBook("Книга_3", "Толстой Л.Н", 3.25)

    print(a)
    print(b)
    print(c)



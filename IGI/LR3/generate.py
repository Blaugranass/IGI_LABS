from typing import Iterator

def generate_list(start: int, count: int, step: int = 1) -> Iterator[int]:
    """
    Генератор последовательности целых чисел
    :param start: начальное значение
    :param count: количество элементов
    :param step: шаг между элементами
    """
    current = start
    for _ in range(count):
        yield current
        current += step
# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.

import time
import pytest


def gcd(a, b):
    """Возвращает НОД двух чисел"""
    while b:
        a, b = b, a % b
    return a


# Маркируем для использования фикстуры для всего класса
@pytest.mark.usefixtures("time_class")
class TestMultiply:

    def test_positive(self):
        assert gcd(180, 150) == 30

    # Вызываем фикстуру для конкретного теста
    def test_negative(self):
        assert gcd(5, 0) == 5
        time.sleep(2)
        assert gcd(0, 0) == 0

    def test_one_prime_number(self):
        assert gcd(250, 13) == 1

    def test_coprime_numbers(self, time_test):
        assert gcd(84, 275) == 1

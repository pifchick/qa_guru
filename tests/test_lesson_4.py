import math
import random


def test_greeting(): #Completed
    """
    Напишите программу, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25
    # TODO Сформируйте нужную строку
    output = f"Привет, {name}! Тебе {age} лет."
    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."


def test_rectangle(): #Completed
    """
    Напишите программу, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20
    # TODO сосчитайте периметр
    perimeter = 0
    c = (a + b) * 2 # Или perimeter r= (a + b) * 2
    perimeter = c
    assert perimeter == 60

    # TODO сосчитайте площадь
    area = 0
    area = a * b #Или с = a * b
    assert area == 200


def test_circle(): #Completed
    """
    Напишите программу, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23
    c = 0
    # TODO сосчитайте площадь
    area = 0
    c = math.pi * r**2 #Или сразу можно написать  area = math.pi * r**2. Или area = math.pi * math.pow(r, 2).
    area = c
    assert area == 1661.9025137490005

    # TODO сосчитайте длину окружности
    length = 0
    length = 2 * math.pi * r
    assert length == 144.51326206513048


def test_random_list(): #Completed
    """
    Создайте список из 10 случайных чисел от 1 до 100 (включая обе границы) и отсортируйте его по возрастанию.
    """
    # TODO создайте список
    # -- -------- -- Вариант 1
    # a = random.randint(0, 101) #command + /
    # b = random.randint(0, 101)
    # c = random.randint(0, 101)
    # d = random.randint(0, 101)
    # e = random.randint(0, 101)
    # f = random.randint(0, 101)
    # g = random.randint(0, 101)
    # h = random.randint(0, 101)
    # y = random.randint(0, 101)
    # z = random.randint(0, 101)
    # l = [a, b, c, d, e, f, g, h, y, z]
    # l.sort(reverse=True)
    # -- -------- -- Вариант 2
    l = [random.randint(0,101) for i in range(10)]
    l.sort(reverse=False)
    # -- -------- -- Вариант 3
    # l = []
    # for i in range(10):
    #     l.append(random.randint(0,101))
    # l.sort(reverse=False)
    # print(l)
    # -- -------- --
    assert len(l) == 10
    assert all(l[i] <= l[i + 1] for i in range(len(l) - 1))


def test_unique_elements(): #Completed
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = list(set([1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]))
    # TODO удалите повторяющиеся элементы

    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts(): #Completed
    """
    Создайте словарь из двух списков.
    Используйте первый список как ключи, а второй - как значения.
    Подсказка: используйте встроенную функцию zip.
    """
    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]
    # TODO создайте словарь
    d = {}
    up_zip = zip(first, second)
    up_list = dict(up_zip) #up_list = list(up_zip) если нужно в обычный словарь
    d = up_list
    print(d)

    """
    Функция zip() принимает итерируемый объект, например, список, кортеж, 
    множество или словарь в качестве аргумента. Затем она генерирует список кортежей,
    которые содержат элементы из каждого объекта, переданного в функцию.
    """
    assert isinstance(d, dict)
    assert len(d) == 5
    assert list(d.keys()) == first
    assert list(d.values()) == second
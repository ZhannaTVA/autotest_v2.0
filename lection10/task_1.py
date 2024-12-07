# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами

import random


def generate_random_name():
    letters_str = 'abcdefghijklmnopqrstuvwxyz'
    while True:
        length1, length2 = random.randint(1, 15), random.randint(1, 15)
        res_str = ''
        for _ in range(length1):
            res_str += random.choice(letters_str)
        res_str += ' '
        for _ in range(length2):
            res_str += random.choice(letters_str)
        yield res_str


gen = generate_random_name()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

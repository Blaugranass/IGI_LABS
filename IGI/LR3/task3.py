"""
Lab 3, Task 3
Developer: Logovoy Artem Alekseevich
Date: 2025-07-04
Version: 1.0
Description: Check if a string is a binary number.
"""

def is_binary(s):
    return all(char in {'0', '1'} for char in s)

def task3():
    print("\n--- Задание 3: Проверка двоичного числа ---")
    s = input("Введите строку: ")
    print(f"Строка {'является' if is_binary(s) else 'не является'} двоичным числом.")
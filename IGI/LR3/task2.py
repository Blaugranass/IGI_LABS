"""
Lab 3, Task 2
Developer: Logovoy Artem Alekseevich
Date: 2023-10-01
Version: 1.0
Description: Count integers greater than 12 until 0 is entered.
"""

def task2():
    print("\n--- Задание 2: Подсчёт чисел >12 ---")
    count = 0
    while True:
        num = input("Введите целое число (0 для завершения): ")
        try:
            num = int(num)
            if num == 0:
                break
            if num > 12:
                count += 1
        except ValueError:
            print("Ошибка: введите целое число.")
    print(f"Количество чисел больше 12: {count}")
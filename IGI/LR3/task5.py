"""
Lab 3, Task 5
Developer: Logovoy Artem Alekseevich
Date: 2025-07-04
Version: 1.0
Description: Process real list with generator support.
"""

from generate import generate_list

def input_real_list():
    """Создание списка с выбором способа заполнения."""
    while True:
        try:
            n = int(input("Размер списка: "))
            if n < 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка: введите положительное целое число.")

    while True:
        choice = input("Способ заполнения (1 - ручной, 2 - генератор): ")
        if choice in ('1', '2'):
            break
        print("Ошибка: введите 1 или 2.")

    lst = []
    if choice == '2':
        while True:
            try:
                start = int(input("Начальное значение генератора: "))
                step = int(input("Шаг генератора: "))
                break
            except ValueError:
                print("Ошибка: введите целые числа для параметров генератора!")
        
        gen = generate_list(start, n, step)
        lst = [float(num) for num in gen]
        print(f"\nСгенерированный список: {lst}")
    else:
        for i in range(n):
            while True:
                try:
                    num = float(input(f"Элемент {i+1}: "))
                    lst.append(num)
                    break
                except ValueError:
                    print("Ошибка: введите число.")
    return lst

def task5():
    print("\n--- Задание 5: Обработка списка ---")
    lst = input_real_list()

    product = 1
    has_positives = False
    for num in lst:
        if num > 0:
            product *= num
            has_positives = True
            
    print(f"\nПроизведение положительных: {product if has_positives else 0:.2f}")

    if not lst:
        print("Список пуст!")
        return
    
    min_abs_index = min(range(len(lst)), key=lambda i: abs(lst[i]))
    sum_before = sum(lst[:min_abs_index])
    print(f"Сумма до элемента с минимальным модулем: {sum_before:.2f}")

if __name__ == "__main__":
    task5()
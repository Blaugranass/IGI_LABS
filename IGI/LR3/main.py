"""
Lab 3 Main Module
Developer: Logovoy Artem Alekseevich
Date: 2025-07-04
Version: 1.0
Description: Main menu for lab tasks.
"""

from task1 import task1
from task2 import task2
from task3 import task3
from task4 import task4
from task5 import task5

def main():
    tasks = {
        '1': task1,
        '2': task2,
        '3': task3,
        '4': task4,
        '5': task5,
        'q': quit
    }
    
    while True:
        print("\nГлавное меню")
        print("1 - Задание 1")
        print("2 - Задание 2")
        print("3 - Задание 3")
        print("4 - Задание 4")
        print("5 - Задание 5")
        print("q - Выход")
        choice = input("Выберите задание: ").lower()
        
        if choice == 'q':
            print("Выход из программы.")
            break
        elif choice in tasks:
            tasks[choice]()
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()
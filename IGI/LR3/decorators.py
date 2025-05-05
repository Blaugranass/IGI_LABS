def repeatable(func):
    """Декоратор для повторного выполнения задачи без выхода из программы."""
    def wrapper():
        while True:
            func()
            again = input("\nПовторить задание? (y/n): ").lower()
            if again != 'y':
                break
    return wrapper

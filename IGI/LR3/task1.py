"""
Lab 3, Task 1
Developer: Logovoy Artem Alekseevich
Date: 2025-07-04
Version: 2.0
Description: Calculating arcsin(x) using power series expansion.
"""

import math
from decorators import repeatable
from inputCheck import input_check

@repeatable
def task1():
    print("\n--- Задание 1: Вычисление arcsin(x) через степенной ряд ---")
  
    x = input_check(
        "Введите x (от -1 до 1): ",
        float,
        lambda x: -1 <= x <= 1
    )
    
    eps = input_check(
        "Введите точность eps (> 0): ",
        float,
        lambda x: x > 0
    )

    true_value = math.asin(x)
    series_sum, n_used = calculate_arcsin_series(x, eps)

    print(f"\nРезультаты:")
    print(f"x: {x}")
    print(f"n: {n_used}")
    print(f"arcsin(x) (степенной ряд): {series_sum:.6f}")
    print(f"arcsin(x) (math.asin): {true_value:.6f}")
    print(f"eps: {eps}")
    print(f"Разница: {abs(series_sum - true_value):.6f}")

def calculate_arcsin_series(x: float, eps: float) -> tuple[float, int]:

    series_sum = x
    term = x
    n_used = 1 
    
    for n in range(1, 500):
        term *= ((2*n - 1)**2 * x**2) / (2*n * (2*n + 1))
        series_sum += term
        
        if abs(series_sum - math.asin(x)) <= eps:
            n_used = n + 1
            break
    
    return series_sum, n_used

if __name__ == "__main__":
    task1()
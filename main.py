from colors import color_coefficients
from parts import part_coefficients
from paintMethods import paintMethod_coefficients
from calculator import calculate_cost

# Базовая стоимость
base_price = 12000

# Ввод данных
part = input("Введите наименование детали: ").lower()
color = input("Введите цвет: ").lower()
paintMethod = input("Введите метод покраски: ").lower()

try:
    # Рассчитываем стоимость
    total_cost = calculate_cost(base_price, part, color, paintMethod, part_coefficients, color_coefficients, paintMethod_coefficients)
    print(f"Стоимость покраски: {total_cost} рублей")
except ValueError as e:
    print(e)
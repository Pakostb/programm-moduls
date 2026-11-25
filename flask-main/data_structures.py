"""
Lesson 14 — Практические задания по структурам данных
Запуск: python data_structures.py
"""

# ========== 1. list из 10 чисел ==========
nums = list(range(1, 11))          # [1, 2, 3, ..., 10]
even = [x for x in nums if x % 2 == 0]
print("1. Чётные числа:", even)


# ========== 2. dict «товар → цена» ==========
products = {
    "хлеб": 45,
    "молоко": 70,
    "яйца": 90
}
products["сыр"] = 250              # добавить
products["молоко"] = 75            # обновить

print("\n2. Товары:")
for name, price in products.items():
    print(f"  {name}: {price} руб.")


# ========== 3. set из списка с дублями ==========
raw = ["яблоко", "груша", "яблоко", "банан", "груша", "яблоко"]
tags = set(raw)
print("\n3. Уникальные:", tags)
print("   Есть 'банан'?", "банан" in tags)
print("   Есть 'kiwi'?", "kiwi" in tags)


# ========== 4. tuple координат ==========
point = (10, 20)
print("\n4. Точка:", point)

try:
    point[0] = 99                  # нельзя изменять tuple
except TypeError as e:
    print("   TypeError (ожидаемо):", e)


# ========== 5. цикл vs comprehension ==========
# Квадраты чисел 1..10

# через for
squares_for = []
for i in range(1, 11):
    squares_for.append(i ** 2)

# через comprehension
squares_comp = [i ** 2 for i in range(1, 11)]

print("\n5. Квадраты (for):         ", squares_for)
print("   Квадраты (comprehension):", squares_comp)
print("   Одинаково?", squares_for == squares_comp)


# ========== Проверка для сдачи ==========
print("\n--- Проверка ---")
assert isinstance(nums, list)
assert isinstance(products, dict)
assert isinstance(tags, set)
assert isinstance(point, tuple)
print("OK")

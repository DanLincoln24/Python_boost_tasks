#6. Отсортируйте список строк по: (длина, затем лексикографически в обратном порядке)
sorted_strings = sorted(["яблоко", "банан", "вишня", "арбуз"], key=lambda s: (len(s), s), reverse=True)
# 7. Верните топ-3 элементов по частоте встречаемости
top_three = [item for item, _ in __import__('collections').Counter(["яблоко", "банан", "яблоко", "вишня", "банан", "яблоко", "финик"]).most_common(3)]

# тесты для №6
strings = ["яблоко", "банан", "вишня", "арбуз"]
result = sorted(strings, key=lambda s: (len(s), s), reverse=True)
print(result == ['яблоко', 'банан', 'вишня', 'арбуз'])
print(sorted(["cat", "elephant", "dog", "bird"], key=lambda s: (len(s), s), reverse=True) == ['elephant', 'bird', 'cat', 'dog'])

# тесты для №7
items = ["яблоко", "банан", "яблоко", "вишня", "банан", "яблоко", "финик"]
from collections import Counter
result = [item for item, _ in Counter(items).most_common(3)]
print(result == ['яблоко', 'банан', 'вишня'] or result == ['яблоко', 'банан', 'финик'])

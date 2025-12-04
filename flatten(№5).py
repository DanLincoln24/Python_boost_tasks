# 5. Flatten: Функция flatten для произвольной вложенности списков/кортежей (только последовательности, строки не трогаем).
def flatten(nested):
    stack = [iter(nested)]
    result = []
    while stack:
        current = stack[-1]
        try:
            item = next(current)
            if isinstance(item, (list, tuple)) and not isinstance(item, str):
                stack.append(iter(item))
            else:
                result.append(item)
        except StopIteration:
            stack.pop()
    return result

print(flatten([1, [2, [3, 4]], [5, 6]]) == [1, 2, 3, 4, 5, 6])
print(flatten([[[[]]]]) == [])
print(flatten(["abc", [1, 2]]) == ["abc", 1, 2])

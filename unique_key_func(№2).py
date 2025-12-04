# 2. Unique key func: Реализуйте unique_by(iterable, key) — возвращает элементы, уникальные по key‑функции, сохраняя порядок.

def unique_by(iterable, key):
    seen = set()
    result = []
    for item in iterable:
        k = key(item)
        if k not in seen:
            seen.add(k)
            result.append(item)
    return result

people = [{"name": "Fedor", "age": 23}, {"name": "Bob", "age": 25}, {"name": "Samir", "age": 28}]
result = unique_by(people, key=lambda p: p["age"])
print(len(result) == 2)
print(result[2]["name"] == "Samir")
# 1. Safe get: Напишите функцию safe_get(d, path, default=None) которая возвращает d[a][b][c]... по списку ключей path, не кидая исключение при отсутствии.
def safe_get(d, path, default=None):
    current = d
    for key in path:
        try:
            current = current[key]
        except (KeyError, TypeError, IndexError):
            return default
    return current

test_dict = {"a": {"b": {"c": 42}}}
print(safe_get(test_dict, ["a", "b", "c"]) == 42)
print(safe_get(test_dict, ["a", "x"], "Нет") == "Нет")
print(safe_get({}, ["key"]) == None)

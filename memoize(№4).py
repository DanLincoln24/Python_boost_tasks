# 4. Memoize: Собственная версия memoize для чистых функций с ограничением размера кэша.
def memoize(maxsize=128):
    def decorator(func):
        from collections import OrderedDict
        from functools import wraps
        cache = OrderedDict()
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            if len(cache) >= maxsize:
                cache.popitem(last=False)
            cache[key] = result
            return result
        return wrapper
    return decorator

call_count = 0
@memoize(maxsize=2)
def test_memo(x):
    global call_count
    call_count += 1
    return x * 2
test_memo(5); test_memo(5); test_memo(3); test_memo(7); test_memo(5)
print(call_count == 4)  # 5, 3, 7, 5 (последний 5 снова, так как был удален)

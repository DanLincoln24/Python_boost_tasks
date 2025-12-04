# 3. Retry decorator: Напишите декоратор retry_backoff(retries, base_delay) с экспоненциальной паузой base_delay * 2**attempt.
def retry_backoff(retries=3, base_delay=1):
    def decorator(func):
        from functools import wraps
        import time
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt == retries - 1:
                        raise
                    time.sleep(base_delay * (2 ** attempt))
            return func(*args, **kwargs)
        return wrapper
    return decorator

attempts = []
@retry_backoff(retries=3, base_delay=0.01)
def test_func():
    attempts.append(1)
    if len(attempts) < 3:
        raise ValueError("Not yet")
    return "Done"
print(test_func() == "Done")
print(len(attempts) == 3)

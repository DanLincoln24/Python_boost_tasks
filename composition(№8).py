# 8. Композиция двух функций f∘g с помощью lambda
compose = lambda f, g: lambda *args, **kwargs: f(g(*args, **kwargs))


add_two = lambda x: x + 2
multiply_by_three = lambda x: x * 3
composed = compose(add_two, multiply_by_three)
print(composed(5) == 17)
print(compose(multiply_by_three, add_two)(5) == 21)
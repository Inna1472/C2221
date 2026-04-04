def calculator_decorator(func):
    def wrapper(expression):
        try:
            return func(expression)
        except Exception as e:
            print(f"Помилка обчислення: {e}")
            return None
    return wrapper

@calculator_decorator
def calculate(expression):
    return eval(expression)


print(calculate("12+5"))
print(calculate("6-13"))
print(calculate("17/0"))
print(calculate("17*3"))
print(calculate("17**3"))
print(calculate("abc"))

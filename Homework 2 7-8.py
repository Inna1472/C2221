import time
import unittest

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        wrapper.last_run_time = end - start
        print(f"\n[⏱️] Час виконання функції: {wrapper.last_run_time:.6f} сек")
        return result
    return wrapper

@timer_decorator
def count_between(a, b):
    if a == b: 
        return ""
    step = 1 if a < b else -1
    res = list(range(a + step, b, step))
    return ", ".join(map(str, res))

def run_manual_mode():
    print("--- Режим ручного введення ---")
    user_input = input("Введіть два числа через пробіл (наприклад, '2 7' або '9 3'): ")
    try:
        n1, n2 = map(int, user_input.split())
        result = count_between(n1, n2)
        print(f"Результат перерахунку: {result}")
    except ValueError:
        print("Помилка: потрібно ввести саме два цілих числа через пробіл.")

class TestCalculator(unittest.TestCase):
    def test_forward_counting(self):
        self.assertEqual(count_between(2, 7), "3, 4, 5, 6")

    def test_backward_counting(self):
        self.assertEqual(count_between(9, 3), "8, 7, 6, 5, 4")

    def test_timer_exists(self):
        count_between(1, 100)
        self.assertTrue(hasattr(count_between, 'last_run_time'))

if __name__ == "__main__":
    print("Запуск автоматичних тестів...")
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCalculator)
    unittest.TextTestRunner(verbosity=1).run(suite)
    
    print("\n" + "="*30 + "\n")
    
    run_manual_mode()

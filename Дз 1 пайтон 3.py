n = int(input("Введіть число n: "))
factorial = 1
numbers = []

for i in range(1, n + 1):
    factorial *= i
    numbers.append(str(i))

path = "*".join(numbers)

print(f"!{n} = {path} = {factorial}")


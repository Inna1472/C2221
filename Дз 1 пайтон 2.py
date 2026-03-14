start = int(input("Введіть число З: "))
end = int(input("Введіть число ПО: "))

if start <= end:
    for i in range(start, end + 1):
        print(i, end=" ")
else:
    for i in range(start, end - 1, -1):
        print(i, end=" ")

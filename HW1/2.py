# Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |


num = int(input("Введите любое число: "))

v = 0

while num > 0:
    n = num % 10
    v += n
    num //= 10

print(v)
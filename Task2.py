# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

i = int(input("Введите трехзначное число "))
sum = 0
index = 0
while index < 3:
    sum += (i % 10)
    i = i // 10
    index += 1
print(f"Сумма цифр равна {sum}")
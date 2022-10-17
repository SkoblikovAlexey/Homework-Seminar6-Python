# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11


real_num = input("Введите вещественное число: ")
result = list(map(int, [dig for dig in real_num if dig.isdigit()]))
num_sum = 0
for elem in result :
    num_sum += elem

print(f'Сумма цифр в числе равна {num_sum}')
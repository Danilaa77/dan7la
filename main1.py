#Кретов Данила Иванович Группа 44-22-116 Вариант 7 Задание 1
import math

def calculate_value(x):
    if x < 1.1:
       return math.exp(math.sin(x)) + math.tan(x)
    else:
       return math.log(abs(math.sin(x) + math.sqrt(2*x)))

try:
    x = float(input("Введите значение x: "))
    result = calculate_value(x)
    print("Результат:", result)
except ValueError:
    print("Ошибка ввода числа")
except Exception as e:
    print("Ошибка:", e)
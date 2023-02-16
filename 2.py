"""
Задание 2.

Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt
       
        
num1 = int(input ("Введите первое число: "))
num2 = int(input ("Введите второе число: "))

try:
    if num2 == 0:
        raise OwnError("Вы пытаетесь делить на ноль!")
except ValueError:
    print ("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print (f"Результат деления {num1} на {num2} : {num1/num2:.2f}")
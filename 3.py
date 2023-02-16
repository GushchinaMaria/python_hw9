"""
Задание 3.

Создайте собственный класс-исключение,
который должен проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять
список только числами.

Класс-исключение должен контролировать типы данных элементов списка.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


arr = list()

while True:
    i = input("Введите положительное число: ")
    if i != "":
        try:
            if i.isdigit():
                i = int(i)
                arr.append(i) 
            elif "." in i:
                i_dot = i
                i_dot_remove = i_dot.replace(".","")
                if i_dot_remove.isdigit():
                    i = float(i)
                    arr.append(i)
                else:
                    raise OwnError("Вы ввели не число!")
            else:
                raise OwnError("Вы ввели не число!")
        except ValueError:
            print ("Вы ввели не число")
        except OwnError as err:
            print(err)
        else:
            print("Число добавлено в список!")
    else:
       break
    
print(f"Вы завершили ввод чисел. \nВаш список: {arr}")

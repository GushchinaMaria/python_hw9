"""
Задание 1.

Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()),
который должен принимать данные (список списков) для формирования матрицы.

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.

Далее реализовать перегрузку метода add() для реализации операции
сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно —
первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.

Пример:
1 2 3
4 5 6
7 8 9

1 2 3
4 5 6
7 8 9

Сумма матриц:
2 4 6
8 10 12
14 16 18
"""


class Matrix:
    def __init__(self,matr):
        self.my_matr = matr
        
        
        
    def __str__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.my_matr])
        

    def __add__(self, other):
        matr_3 = [[0]*len(self.my_matr[0]) for i in range(len(self.my_matr))]
               
        for numrows in range(len(self.my_matr)): 
            for numcols in range(len(self.my_matr[0])):  
                matr_3[numrows][numcols] = int(self.my_matr[numrows][numcols]) + int(other.my_matr[numrows][numcols])
                
        return '\n'.join(['\t'.join(map(str, row)) for row in matr_3])


matr1 = list() 


while True:
    input_str = input("Введите строку первой матрицы: ")
    if input_str !='':
        row = input_str.split()
        matr1.append(row)
    else:
        break


matr_1 = Matrix(matr1)
print("\n Ваша 1 матрица: ")
print(matr_1)

matr2 = list() 

while True:
    input_str = input("Введите строку второй матрицы: ")
    if input_str !='':
        row = input_str.split()
        matr2.append(row)
    else:
        break


matr_2 = Matrix(matr2)
print("\n Ваша 2 матрица: ")
print(matr_2)

res_matr = matr_1 + matr_2
print("\n Результат сложения двух матриц: ")
print(res_matr)
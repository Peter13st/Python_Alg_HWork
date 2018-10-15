# Написать программу, которая генерирует в указанном пользователем диапазоне:
#   случайное целое число,
#   случайное вещественное число,
#   случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Если надо получить случайный символ от 'a' до 'f', вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

import sys
def show_sizeof(*vars):
    sv=0
    for v in vars:
        print(v.__class__, sys.getsizeof(v), v)
        sv+=sys.getsizeof(v)
    print('Total size of vars: ', sv)


#   случайное целое число
print('Случайное целое число')
num_start = int(input('Начало диапазона: '))
num_end = int(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(result)

#   случайное вещественное число
print('Случайное вещественное число')
num_start = float(input('Начало диапазона: '))
num_end = float(input('Конец диапазона: '))
# result = random.random() * (num_end - num_start) + num_start
result = random.uniform(num_start, num_end)
print(round(result, 3))

#   случайный символ
print('Случайный символ')
num_start = ord(input('Начало диапазона: '))
num_end = ord(input('Конец диапазона: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(chr(result))

show_sizeof(num_start,num_end,result)
#Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
#<class 'int'> 28 100
#<class 'int'> 28 107
#<class 'int'> 28 105
#Total size of vars:  84

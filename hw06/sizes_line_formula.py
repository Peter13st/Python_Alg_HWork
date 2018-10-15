# По введенным пользователем координатам двух точек вывести уравнение прямой,
# которая проходит через эти точки

import sys
def show_sizeof(*vars):
    sv=0
    for v in vars:
        print(v.__class__, sys.getsizeof(v), v)
        sv+=sys.getsizeof(v)
    print('Total size of vars: ', sv)


print('Координаты точки A(x1, y1):')
x1 = float(input('x1 = '))
y1 = float(input('y1 = '))

print('Координаты точки B(x2, y2):')
x2 = float(input('x2 = '))
y2 = float(input('y2 = '))

print('Уравнение прямой, проходящей через эти точки:')
if x1 == x2:
    print(f'x = {x1:.2f}')
else:
    k = (y1 - y2) / (x1 - x2)
    b = y2 - k * x2
    print(f'y = {k:.2f} * x + {b:.3f}')


show_sizeof(x1,y1,x2,y2,k,b)

#Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 18:11:49) [MSC v.1900 64 bit (AMD64)] on win32
#<class 'float'> 24 56.0
#<class 'float'> 24 36.0
#<class 'float'> 24 86.0
#<class 'float'> 24 37.0
#<class 'float'> 24 0.03333333333333333
#<class 'float'> 24 34.13333333333333
#Total size of vars:  144

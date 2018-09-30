#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
#Числа и знак операции вводятся пользователем.
#После выполнения вычисления программа не должна завершаться,
#а должна запрашивать новые данные для вычислений.
#Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
#Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'),
#то программа должна сообщать ему об ошибке и снова запрашивать знак операции.
#Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.
mop = ''
while mop != '0':
    n1 = float(input('Введите число №1: '))
    n2 = float(input('Введите число №2: '))
    while mop not in ['+', '-', '*', '/', '0']:
        mop = input("Введите операцию: '+', '-', '*', '/', или '0' для выхода из программы: ")
        if mop not in ['+', '-', '*', '/', '0']:
            print('Ошибка ввода операции!')

    if mop != '0':
        if mop == '+':
            res = n1 + n2
            print('Результат n1+n2: ', res)
        if mop == '-':
            res = n1 - n2
            print('Результат n1-n2: ', res)
        if mop == '*':
            res = n1 * n2
            print('Результат n1*n2: ', res)
        if mop == '/':
            if n2 != 0:
                res = n1 / n2
                print('Результат n1/n2: ', res)
            else:
                print('На 0 делить нельзя!')
        mop = ''
    else:
        print('Выбран "0" - Выход из программы!')
        break

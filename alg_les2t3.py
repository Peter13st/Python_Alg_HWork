#Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#Например, если введено число 3486, то надо вывести число 6843
s = input('Введите целое положительное число: ')
sr = ''
i = -1
while i >= -len(s):
    sr = sr + s[i]
    i -=1
print('Ваше число наоборот: ', sr)

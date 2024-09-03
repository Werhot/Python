# print('Hello world!', end=',')
# print('Hello world!')
# print('Hello world!')



# a = input('Введите ваше имя: ')
# print('Вас зовут:' + a)

l = ['1', 1, 'asfafmhkjh']
# list список

t = (4, 9, 0, 4)
# touple картеж

d = {'green': 'apple', 'red': 'cherry'}
# dictionary словарь

set_1 = {5, 7, 3, 5}
# set множество

boolean = True

# + - / *
# ** возведение в степень
# // деление с только целыми числами
# % деление с остатком, выводит 0 или 1

# > < >= <=
# == равно ли?
# != не равно?

# and логич. умножение
# or логич. сложение
# not логич. отрицание



# num_1 = int(input('Введите число: '))
#
# if num_1 > 0:
#     print('Число больше 0')
# elif num_1 < 0:
#     print('Число меньше 0')
# else:
#     print('Число равно 0')


# for i in range(5, 21, 2):
#     print(i)
# с 5 до 20 с шагом 2


# for i in range(5, 21, 2):
#      print(i, end=',')
#
#
# stroke = 'abavaveva'
# for char in stroke:
#     print(char , end=' ')
#
#
# for i in range(len(stroke)):
#     print(stroke[i])
#
#
# print(f' Словарь: {d}'
#       f' \n Список: {l}'
#       f' \n Булевая переменная: {boolean}')



# num = 1234
# print(num // 1000)
# print(num // 100 % 10) # если слева больше, получаем 1 или 0, если меньше получаем число слева
# print(num // 10 % 10)
# print(num % 10)



# from random import randint as rInt
# secret_number = rInt(1, 10)
# attempts = 3
# print('Программа загадала число от 1 до 10, у вас есть 3 попытки, чтобы его угадать')
# while attempts > 0:
#     print('У вас осталось: ' + str(attempts) + 'попыток')
#     attempts -= 1
#     user_number = int(input('Введите число от 1 до 10: '))
#     if user_number > secret_number:
#         print('Ваше число больше загадонному')
#     elif user_number < secret_number:
#         print('Ваше число меньше загадонному')
#     else:
#         print('Вы угадали, ваше число равно загадонному')
#         break
#     if attempts == 0:
#         print('Вы проиграли, у вас не осталось попыток. \n Загаданным числом было: ' + str(secret_number))
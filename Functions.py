print()
# def func1(**kwargs): #Ключ: значение, как в словарях
#     str_1 = ''
#     for key, value in kwargs.items():
#         str_1 += value
#     return str_1
# def func2(*args):
#     print(*args)
# print(func1(a = 'a', b = 'b'))
# func2(6, 4, 7)
# print()






# is_full = bool(input('True/False: '))
# a = int(input('Введите длинну стороны квадрата: '))
# char = input('Введите символ: ')
# def printSquare(a, char, is_full):
#     if is_full == 'True':
#         for i in range(a):
#             print(char * a)
#     else:
#         print(char * a)
#         for i in range(a - 2):
#             print(char + ' ' * (a - 2) + char)
#         print(char * a)
#
# printSquare(a, char, str(is_full))
# Не работает!






# def count_digit(number):
#     return len(str(number))
#
# try:
#     num = int(input('Введите число: '))
#     print(count_digit(num))
# except ValueError:
#     print('Вы ввели не число!')
# print()







# def remove_element(numbers, target): 1 способ:
#     count = 0
#     i = 0
#     while i < len(numbers):
#         if numbers[i] == target:
#             numbers.pop(i)
#             count += 1
#         else:
#             i += 1
#     return print(f'{count} удалёных чисел "{target}"')

# def remove_element(numbers, target): 2 способ:
#     new_numbers = [x for x in numbers if x == target]
#     return print(len(new_numbers))
#
# numbers = input('Введите список чисел через пробел: ') Условие:
# numbers = numbers.split()
# target = input('Введите число: ')
# remove_element(numbers, target)






text = 'Python is great. Python si fun! Programming with Python is enjotable!'
def analyze_text(text: str, stop_words=None):
    if stop_words == None:
        stop_words = []
    test = text.lower()
    for char in "'.,!&-:;":
        text = text.replace(char, ' ')
    words = text.split()
    words_count = {}
    for word in words:
        if word not in stop_words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1
    return words_count
print(analyze_text(text, stop_words=['is', 'with']))
print()






orders = [
    {'order_id': 1,
     'customer': 'Alice',
     'items': {'laptop': 1, 'mouse': 2},
     'total_price': 1200},
    {'order_id': 2,
     'customer': 'Bob',
     'items': {'laptop': 1, 'keyboard': 1},
     'total_price': 1500},
    {'order_id': 3,
     'customer': 'Alice',
     'items': {'phone': 2, 'headphones': 1},
     'total_price': 600},
]

def generate_report(orders):
    categorys_count = {}
    customer_orders = {}
    total_price = 0
    total_orders = len(orders)

    # общая стоимость заказов
    for order in orders:
        total_price += order['total_price']

        # кол-во заказов по клиентам
        customer = order['customer']
        if customer in customer_orders:
           customer_orders[customer] += 1
        else:
            customer_orders[customer] = 1

        # кол-во проданных товаров по категориям
        for item, quantity in order['items'].items():
            if item in categorys_count:
                categorys_count[item] += quantity
            else:
                categorys_count[item] = quantity

    # средняя стоимость заказа
    avg_order_value = total_price / total_orders

    print('Общее кол-во проданных товаров: ')
    for category,quantity in categorys_count.items():
        print(f'- {category}: {quantity}')
    print(f'\n Средняя стоимость заказа: {avg_order_value}\n')

    print('Заказы по клиентам')
    for customer, count in customer_orders.items():
        print(f'- {customer}: {count} заказ{"a" if count == 1 else "ов"}')

    print(f'\n Общее кол-во заказов: {total_orders}')
    print()


generate_report(orders)






import random
import string
def generate_password(lenght: int, complexity: int):
    # lower = 'abcdefghijklmnopqrstuvwxyz'
    # random.choice(lower)
    if lenght < 8:
        raise ValueError('Пароль должен быть не менее 8-ти символов')
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_letters
    elif complexity == 3:
        characters = string.ascii_letters + string.digits
    elif complexity == 4:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        raise ValueError('Уровень сложности пароля должен быть в диапозоне от 1 до 4')

    password = ''
    for _ in range(lenght):
        password += ''.join(random.choice(characters))

    return password

lenght = int(input('Введите длинну: '))
complexity = int(input('Введите уровень сложности пароля 1-4: '))

result = generate_password(lenght, complexity)
print(f'Ваш пароль {result}, длинна {lenght}, сложность {complexity}')
print()
# dict_1 = {'a': 5, 'b': 8, 'c': 9}
# print(dict_1)
# print()
#
# print(dict_1['a'])
# print()
#
# print(id(dict_1))
# print()
#
# dict_1['d'] = 10
# print(dict_1)
# print()
#
# print(dict_1.items())
# print()
#
# print(dict_1.keys())
# print()
#
# print(dict_1.values())
# print()
#
# dict_2 = dict_1.copy()
# print(id(dict_1))
# print(id(dict_2))
# print('"Разные id"')
# print()
#
# dict_1.update(dict_2)
# print(dict_1)
# print()
#
# dict_3 = {1: 'x', 2: 'y', 3: 'z'}
# dict_3.update(dict_1)
# print(dict_3)
# print()
#
# dict_3.setdefault('q')
# print(dict_3)
# print()
#
# t = dict_3.pop(2)
# print(t)
# print()
#
# u = dict_3.popitem()
# print(u)
# print()
#
# dict_4 = {'k': 11, 'n': 7}
# o = dict_4.popitem()
# print(o, dict_4)
# print()
#
# print(dict_4.get('L', 9))
# print('"Ключа L не существует"')
# print()
#
# set_1 = set()
# set_2 = {4, 7, 4, 8, 9, 1}
# print(set_2)
# print()
#
# list_3 = [4, 7, 2, 4, 9, 7]
# list_3 = list(set(list_3))
# print(list_3)
# print('"Убраны все дубликаты"')
# print()
#
# set_3 = {'a', 'b', 'c', 'a'}
# print(set_3)
# print('"Дубликаты других типов данных тоже удаляются"')
# print()
#
# set_3.remove('b')
# print(set_3)
# print('"Мы убрали "b" методом remove"')
# a = set_3.pop()
# print(a,set_3)
# print('"Мы убрали "a" методом pop"')
# print()
#
# set_4 = {1, 2, 3, 5, 8}
# set_5 = {2, 4 ,5 ,8, 0}
# set_4.union(set_5)
# print(set_4)
# print('"Мы соеденили множеств, дубликаты сами убрались"')
# print()
#
# print(set_4.intersection(set_5))
# print('"Вывели все пересечения"')
# print()
#
# print(set_4.difference(set_5))
# print('"Элементы которых нет в set_5"')
# print(set_5.difference(set_4))
# print('"Элементы которых нет в set_4"')
# print()

# numbers = (1, 0, -5, -2.5, 6, 3.7, 0, 0)
# sum_positive = 0
# product_negative = 1
# has_negative = False
# extentions = []
# for num in numbers:
#     if num > 0:
#         sum_positive += num
#     elif num < 0:
#         product_negative *= num
#         has_negative = True
#     else:
#         extentions.append(num)
# if not has_negative:
#     product_negative = 0
# result = (sum_positive, product_negative)
# print()
# print(result)
# print('Список чисел неподходящих под условие: ')
# print(extentions)
# print()
#
#
#
#
#
#
# dict_students = {
#     'Семён': {'лет': 21, 'Оценки': [3, 5, 4, 2, 2]},
#     'Артём': {'лет': 20, 'Оценки': [5, 5, 5, 4, 4]},
#     'Пётр': {'лет': 22, 'Оценки': [3, 3, 4, 4, 3]},
# }
# sum_grades = 0
# sum_student_grades = []
# count_grades = 0
# count_student_grades = 0
#
# for student in dict_students.values():
#     count_student_grades = len(student['Оценки'])
#     sum_grades += sum(student['Оценки'])
#     count_grades += len(student['Оценки'])
#
# print('Всего у каждого студента оценок: ' + str(count_student_grades))
# avg_grades = sum_grades / count_grades
# student_name = []
#
# for name, info in dict_students.items():
#     if sum(info['Оценки']) / len(info['Оценки']) > avg_grades:
#         print('Средняя оценка по группе: ' + str(sum(info['Оценки']) / len(info['Оценки'])))
#         student_name.append(name)
#
# print('Превышают среднюю оценку: ' + str(student_name))
# print()
#
#
#
#
#
#
# words = ['green', 'red', 'green', 'orange', 'blue', 'red', 'green']
# words_count = {}
# for word in words:
#     if word in words_count:
#         words_count[word] += 1
#     else:
#         words_count[word] = 1
# print(words_count)
# print()






# print('"добавить"| Добавить книгу')
# print('"удалить"| Удалить книгу')
# print('"найти"| Найти книгу')
# print('"удалить"| Удалить книгу')
# print('"исправить"| Исправить информацию о книге')
# print('"показать коллекцию"| Показать коллекцию книг')
# print('"выход"| Выйти из прогоаммы')
# print()
# books = {}
# while True:
#     choise = input('Выберите действие: ')
#
#     if choise == 'выход':
#         break
#
#     elif choise == 'добавить':
#         title = input('Введите название книги: ')
#         author = input('Введите автора книги: ')
#         year = input('Введите год издания книги: ')
#         books[title] = {
#             'author': author,
#             'year': year
#         }
#         print(f'Книга {title} добавлена')
#         print()
#
#     elif choise == 'удалить':
#         print('Удаление книги по названию')
#         print()
#         title = input('Введите название книги: ')
#         if title in books:
#             # books.remove(title)
#             del books[title]
#             print(f'Книга {title} удалена')
#             print()
#         else:
#             print('Не удалось найти такую книгу')
#             print()
#
#     elif choise == 'найти':
#         title = input('Введите название книги: ')
#         if title in books:
#             books_info = books[title]
#             print(f'Книга {title}: {books_info}')
#             print()
#         else:
#             print('Не удалось найти такую книгу')
#             print()
#
#     elif choise == 'исправить':
#         title = input('Введите название книги: ')
#         if title in books:
#             author = input('Введите автора книги: ')
#             year = input('Введите год издания книги: ')
#             print('Оставте пустыми поля которые не хотите изменять')
#             print()
#             if author:
#                 books[title]['author'] = author
#             if year:
#                 books[title]['year'] = year
#             print(f'Информация о книге обновлена')
#             print()
#         else:
#             print('Не удалось найти такую книгу')
#             print()
#
#     elif choise == 'показать коллекцию':
#             if books:
#                 for title, info in books.items():
#                     print(f'Название книги: {title}, общая информация: {info}')
#                     print()
#             else:
#                 print('В коллекции пока ничего нет')
#     else:
#         print("Вы ввели неверную комманду")






# print()
# print(ord(' '))
# print(ord('A'))
# print(ord('B'))
# print(ord('Z'))
# print('"Кодировка от 65 до 90 (БОЛЬШИЕ буквы (26)"')

text = 'K ffffffffffffff TTTTTTTTTTTTTTTTT KKKKKKKKKKKKKKKKKKKK BBBBBBBBBBBBBBBBB AAAAAA GGGGG JJJJJ MMMMMMMM XXXXX YYYY ZZZZZ UUUU OOOOO WWWWW QQQQQ'
shift = 3
shifted_text = ''

for char in text:
    if char.isalpha():
        base = 0
        if char.isupper():
            base = ord('A') #65
        else:
            base = ord('a') #97
        position = ord(char) - base #позиция буквы в алфавите (0-25(26))
        new_position = (position + shift) % 26 + base
        new_char = chr(new_position)
        shifted_text += new_char
    else:
        shifted_text += char
print(shifted_text)
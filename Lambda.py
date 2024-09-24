# # lambda arguments: expression
# print('Программа считает площаль квадрата')
# square = lambda x: x ** 2
# print(square(4))
#
#
# sum_squares = lambda x, y: x**2 + y**2
# print(sum_squares(4, 6))
#
# # sort, filter, map
#
# l1 = [1, 5, 8, 3]
# l1.sort()
# print(l1)
#
# l2_even = list(filter(lambda x: x % 2 == 0, l1))
# print(l2_even)
#
# l3 = [1, 2, 3, 4, 5]
# sq = list(map(lambda x: x ** 2, l3))
# print(sq)
#
# # sorted()
#
# str_1 = ['python', 'js', 'java', 'c#']
# sorted_str = sorted(str_1, key=lambda x: len(x))
# print(sorted_str)
#
# number = [-8, -1, 8, -3, 7, 9, 10]
# positive_num = list(filter(lambda x: x > 0, number))
# print(positive_num)
#
# str_upper = list(map(lambda x: x.upper(), str_1))
# print(str_upper)






# 1
students = [
{'name': 'Иван', 'age': 20, 'grade': 4.5},
{'name': 'Пётр', 'age': 22, 'grade': 4.8},
{'name': 'Фёдр', 'age': 21, 'grade': 5.0},
{'name': 'Семён', 'age': 20, 'grade': 4.9},
{'name': 'Артём', 'age': 23, 'grade': 4.1}
]

filtered_std_list_1 = list(filter(lambda x: x['age'] >= 21 and x['grade'] >= 4.6, students))
print([student['name'] for student in filtered_std_list_1])
print()

orders = [
{'customer': 'Иван', 'total': 1000},
{'customer': 'Мария', 'total': 500},
{'customer': 'Пётр', 'total': 2000},
{'customer': 'Ольга', 'total': 800},
{'customer': 'Сергей', 'total': 1500}
]

# total_sum = sum(list(map(lambda x: x['total'], orders)))
total_sum = sum(map(lambda x: x['total'], orders))
print(total_sum)
print()






employees = [
{'name': 'Иван', 'department': 'IT', 'salary': 50000},
{'name': 'Пётр', 'department': 'HR', 'salary': 40000},
{'name': 'Фёдр', 'department': 'IT', 'salary': 60000},
{'name': 'Семён', 'department': 'Marketing', 'salary': 70000},
{'name': 'Артём', 'department': 'IT', 'salary': 55000},
]

filtered_empl = list(filter(lambda x: x['department'] == 'IT' and x['salary'] >= 55000, employees))
print([empl['name'] for empl in filtered_empl])
print()






# file = open('example.txt', 'r')
# print(file.read())
# file.close()

# with open('example.txt', 'r') as f:
#     print(f.read())
#     print()

# read()
# write()
# readline()
# readlines()
# writelines()
# seek()
# tell()
'w' #запись (перезаписывает с нуля)
'r' #чтение
'a' #запись (добавляет в конец)
'w+' #запись (перезаписывает с нуля) (не создаёт новый файл)
'a+' #запись (добавляет в конец) (не создаёт новый файл)

# import os
# os.getcwd()
# os. mkdir()
# os.rmdir()
# os.rename()
# os.remove()
# os.path()





# path_1 = os.path.join(os.path.dirname(__file__), 'example.txt')
# print(path_1)
# print()
# user_text = '111111111'
# # path_2 = os.path.dirname(__file__)
# # print(path_2)
# with open(path_1, 'r') as f:
#     print(f.readlines(1))
#     print()
#
#
# with open(path_1, 'a') as f:
#     print(f.writelines(user_text))
#     print()
#
#
# with open(path_1, 'r') as f:
#     (f.seek(5))
#     pos = f.tell()
#     print(f.read())
#     print(pos)
#     print()
#
#
# with open(path_1, 'a', encoding='utf-8') as f:
#     f.write('привет мир!')





import os
import json
path_j = os.path.join(os.path.dirname(__file__), 'weather.json')
with open(path_j, 'r') as f:
    data = json.load(f) #десериализация
print(data)


data = {'name': 'Mike', 'age': 15}
with open('data.json', 'w') as f:
    json.dump(data, f) #сериализация данных в формат JSON


json_str = '{"name": "Mike", "age": 15}'
data_1 = json.loads(json_str)
print(data_1)


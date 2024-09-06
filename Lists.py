# l_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#
# l_2 = list('regfdrgg')
#
# l_3 = list(('Python', 'Java', 'C++'))
#
# print(l_3)
# print(l_2[2:5])
# print(l_2[4])
# print(l_2[::2])
# print(l_2[-3])
#
# l_2[2] = 'new value'
# print(l_2)
#
# l_4 = [[1, 4, 6], [7, 3, 9], [2, 0, 7]]
# print(l_4[1][2])
#
# l_2[:3] = 'a', 'n', 'w'
# print(l_1)
# print(l_3 + l_2)
#
# l_5 = [4, 8, 1, 0, 10, 45, 81]
# print(len(l_5))
# print(min(l_5))
# print(max(l_5))
# print(sum(l_5))
# print(sorted(l_5))
#
# for el in l_5:
#     el = el ** 2
#     print(el, end=' ')
# print()
# l_5.append(6)
# print(l_5)
# l_5.pop(4)
# print(l_5)
# l_5.append(0)
# print(l_5)
# l_5.remove(0)
# print(l_5)






# list_of_numbers = (6, 2, 1, 9, 3, 0, 5, 1)
# target = 6
# unique_pairs = []
#
# for i in range(len(list_of_numbers)):
#     for j in range(i+1, len(list_of_numbers)):
#         if list_of_numbers[i] + list_of_numbers[j] == target:
#             pair = (min(list_of_numbers[i], list_of_numbers[j]), max(list_of_numbers[i], list_of_numbers[j]))
#             if pair not in unique_pairs:
#                 unique_pairs.append(pair)
# print(unique_pairs)






# numbers = [8, 4, 9, 8, 8, 2, 4, 1, 9]
# new_numbers = []
# counter_dictionary = {}
#
# for i in numbers:
#     if i in counter_dictionary:
#         counter_dictionary[i] += 1
#     else:
#         counter_dictionary[i] = 1
# print(counter_dictionary)
#
# list_tuple = []
#
# for key, val in counter_dictionary.items():
#     list_tuple.append((key, val))
# print(list_tuple)
#
# sorted_list = []
# while list_tuple:
#     max_freq = -1 #max частота
#     min_num = None #min значение с max частотой
#     for i in range(len(list_tuple)):
#         num, freq = list_tuple[i]
#         if freq > max_freq:
#             max_freq = freq
#             min_num = num
#         elif freq == max_freq and (min_num is None or num < min_num):
#             min_num = num
#     sorted_list.append((min_num, max_freq))
#     list_tuple.remove((min_num, max_freq))
# print(sorted_list)
#
# for i in sorted_list:
#     num = i[0]
#     freq = i[1]
#     for _ in range(freq):
#         new_numbers.append(num)
# print(new_numbers)






# list_circle = [2, 8, 4, 2, 9, 1]
# n = int(input('Введите позицию сдвига: (+/-) \n'))
# len_l = len(list_circle)
# n = n % len_l
# shifted_list = list_circle[-n:] + list_circle[:-n]
# print(shifted_list)






# list_1 = [ i*i for i in range(6)]
# print(list_1)
#
# list_2 = [ i + ' ' for i in "dsfsfdsfdf"]
# print(list_2)
#
# list_3 = [i*i for i in range(1, 11) if i % 2 == 0]
# print(list_3)






# from random import randint
# list_1 = [randint(1, 20) for _ in range(10)]
# list_2 = [randint(1, 20) for _ in range(10)]
# print(list_1)
# print(list_2)
#
# combine_list = list_1+list_2
# print(combine_list)
#
# unique_combine_list = list(set(combine_list))
# print(unique_combine_list)
#
# intersect_list = list(set(list_1).intersection(set(list_2)))
# print(intersect_list)
#
# u_l1 = list(set(list_1))
# u_l2 = list(set(list_2))
# unique_elements = u_l1 + u_l2
# print(unique_elements)
#
# min_max_1 = [min(list_1), max(list_1)]
# min_max_2 = [min(list_2), max(list_2)]
# min_max = min_max_1 + min_max_2
# print(min_max)






# i1j1 i2j1 i3j1 i4j1 i5j1
# i1j2 i2j2 i3j2 i4j2 i5j2

matrix = [[(i+1)*(j+1) for j in range(5)] for i in range(5)]
for row in matrix:
    print(row)
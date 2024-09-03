import re

# {n}
# {m, n} #от n включительно и более
# {m,} #m вслючительно и больше
# {,n} #до n всключительно
# ?_0/1 #
# + 0 > #
# * 1 > #
#
# student/d{5}
#
# /d /D
# /w /W
# /s /S
# [0-5] #от 0 до 5
# [^a-g] #кроме
#
# re.match(pattern=, str) #находит совпадение
# re.findall(pattern=, str) #возвращает список со всеми совпадениями
# re.search(pattern=, str) #находит первое совпадение
# re.split(pattern=, str) # разбить строку
# re.sub() #замена строки






# str_email = input()
# userPattern = r"^[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]*\.[a-zA-Z0-9.-]{2,}$"
# if re.match(userPattern, str_email):
#     print("электронная")
# else:
#     print("неэлектронная")






# str_date = input()
#
# datePattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|[1][012])\.((19|20)/d{2}|2100)$"
#
# if re.match(datePattern, str_date):
#     print("подходит")
# else:
#     print("неподходит")





text = input('Введите ссылку: \n')
urlPattern = r"(http|https)://[^/s][0-9a-zA-Z_.-]{1,}"
urls = re.findall(urlPattern, text)
print(f'Url адреса {urls}')
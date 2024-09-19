# Рекурсия:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))


def fibonacci(n, memo={}):
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


print(fibonacci(6))






import random

def  generate_number():
    return str(random.randint(10, 99))


def check_number(user_number, generic_number):
    bulls = 0
    cows = 0
    for i in range(2):
        if user_number[i] == generic_number[i]:
            cows += 1
        elif user_number[i] in generic_number:
            bulls += 1
    return bulls, cows

generic_number = generate_number()

def play_game(attempts=0):
    user_number = input('Введите двухзначное число\nдля того чтобы выйти из программы введите 0:\n')
    if user_number == '0':
        return
    else:
        if len(user_number) != 2 or not user_number.isdigit():
            print('Вы ввели неподходящее число')
            return play_game(attempts)
    bulls, cows = check_number(user_number, generic_number)
    print(f'быки {bulls}, коровы {cows}')
    attempts += 1
    if cows == 2:
        print(f'Вы выйграли! Попытки:{attempts}')
    else:
        play_game(attempts)

play_game()






def check_win(field):
    win_condition = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_condition:
        if field[condition[0]] == field[condition[1]] == field[condition[2]] != ' ':
            return field[condition[0]]
    if ' ' not in field:
        return 'Ничья!'
    return False


def game(field, player):
    print_field(field)
    move = int(input(f'Игрок {player}, выберите ячейку (1-9):\n'))
    if field[move - 1] != ' ':
        print('Эта ячейка занята!')
        return game(field, player)
    # if player == 'X':
    #     field[move - 1] = 'X'
    # else:
    #     field[move - 1] = 'O'
    field[move - 1] = 'X' if player == 'X' else 'O'
    result = check_win(field)
    if result:
        print_field(field)
        if result == 'Ничья!':
            print('Ничья!')
        else:
            print(f'Победил {result}!')
        return
    game(field, 'O' if player == 'X' else 'X')


def print_field(field):
    print(f' {field[0]} | {field[1]} | {field[2]}')
    print('---+---+---')
    print(f' {field[3]} | {field[4]} | {field[5]}')
    print('---+---+---')
    print(f' {field[6]} | {field[7]} | {field[8]}')

field = [' '] * 9
game(field, 'X')

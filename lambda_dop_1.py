import os
path_a = os.path.join(os.path.dirname(__file__), 'finances.txt')

def add_fin(file_name, date, type, amount, description):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{date}:{type}:{amount}:{description}\n')


def delete_fin(file_name, date):
    lines = []
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            if not line.startswith(date):
                lines.append(line)
    with open(file_name, 'w', encoding='utf-8') as file:
        file.writelines(lines)


def print_fin(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        print(file.read())


def get_balance(file_name):
    balance = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            _, type, amount, _ = line.split(':')
            if type == '-':
                balance -= float(amount)
            elif type == '+':
                balance += float(amount)
    return balance

def main():
    file_name = os.path.join(os.path.dirname(__file__), 'finances.txt')
    while True:
        choice = input("""Выберите действие:
        "Д" добавление
        "У" удаление
        "В" вывести список
        "Б" баланс счёта
        "Выход" остановить программу\n""")

        if choice == 'Выход':
            break

        elif choice == 'Д':
            date = input('Введите дату: ')
            type = input('Введите тип(+\-): ')
            amount = input('Введите сумму: ')
            description = input('Введите описание: ')
            add_fin(file_name, date, type, amount, description)

        elif choice == 'У':
            date = input('Введите дату для удаления: ')
            delete_fin(file_name, date)

        elif choice == 'В':
            print_fin(file_name)

        elif choice == 'Б':
            print(get_balance(file_name))

        else:
            print('Вы ввели неподходящее значение, попробуйте снова')

main()
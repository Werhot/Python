secret_word = 'автомобиль'
attempts = 6
for char in secret_word:
    print('*', end=' ')
print()
user_chars = []

while True:
    Is_win = True
    print('\n У вас осталось: ' + str(attempts) + 'попыток')
    user_letter = str(input('Назовите букву: '))
    if user_letter not in user_chars:
        user_chars.append(user_letter)
    else:
        print("Вы уже называли эту букву")
    for char in secret_word:
        if char in user_chars:
            print(char, end=' ')
        else:
            print('*', end=' ')
            Is_win = False
    if user_letter not in secret_word:
        attempts -= 1
    if attempts == 0:
        print('\n Вы проиграли, у вас не осталось попыток. \n Загаданным словом было: ' + secret_word)
        break
    if Is_win == True:
        print('\n Вы выйграли Ааааааавтомобиль!')
class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}: {self.price}р'




class MainDish(Dish):
    def __init__(self, name, price, vegetarian=False):
        super().__init__(name, price,)
        self.vegetarian = vegetarian

    def __str__(self):
        veg = '(Вегетарианское)' if self.vegetarian else ''
        return f'Основное блюдо-{self.name}-{veg}: {self.price}р'




class Desert(Dish):
    def __init__(self, name, price, sugar_free=False):
        super().__init__(name, price)
        self.sugar_free = sugar_free

    def __str__(self):
        sug = '(Без сахара)' if self.sugar_free else ''
        return f'Десерт-{self.name}-{sug}: {self.price}р'




class Drink(Dish):
    def __init__(self, name, price, alcohol=False):
        super().__init__(name, price)
        self.alcohol = alcohol

    def __str__(self):
        alc = '(Алкогольное)' if self.alcohol else '(Безалкогольное)'
        return f'Напитки-{self.name}-{alc}: {self.price}р'




class Order:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def remove_dish(self, dish):
        if dish in self.dishes:
            self.dishes.remove(dish)

    def total_sum(self):
        return sum(dish.price for dish in self.dishes)

    def __str__(self):
        order_summary = '\n'.join(str(dish) for dish in self.dishes)
        return f'Ваш заказ: \n{order_summary}\n Общаяя сумма: {self.total_sum()}\n'

    def __add__(self, other):
        combinate_order = Order()
        combinate_order.dishes = self.dishes + other.dishes
        return combinate_order

    def __gt__(self, other):
        return self.total_sum() > other.total_sum()


pizza = MainDish('Маргарита', 550, vegetarian=True)
burger = MainDish('Чизбургер', 200)

cake = Desert('Чизкейк', 250)
juice = Drink('Аппельсиновый сок', 150, alcohol=False)
wine = Drink('Красное вино', 450, alcohol=True)

order1 = Order()
order1.add_dish((pizza))
order1.add_dish(juice)

order2 = Order()
order2.add_dish(burger)
order2.add_dish(cake)
order2.add_dish(wine)

combined = order1 + order2
o1_o2 = order1 > order2

order1_sum = str(order1)
order2_sum = str(order2)
combined_sum = str(combined)

print(order1_sum, order2_sum, combined_sum, o1_o2)
print()






# from datetime import datetime as dt
# class Logger:
#     def log(self, massage, level):
#         pass
#
#
#
#
# class FileLogger(Logger):
#     def log(self, massage, level):
#         with open('log.txt', 'w') as file:
#             timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')
#             file.write(f'{timestamp} | {level} | {massage}\n')
#
#
#
#
# class ConsoleLogger(Logger):
#     def log(self, massage, level):
#         timestamp = dt.now().strftime('%Y-%m-%d %H:%M:%S')
#         print(f'{timestamp} | {level} | {massage}\n')
#
#
#
#
# class HybridLogger(FileLogger, ConsoleLogger):
#     def log(self, massage, level):
#         FileLogger.log(self, massage, level)
#         ConsoleLogger.log(self, massage, level)
#
#         if level == 'DEBUG':
#             print('This massage DEBUG level')
#         elif level == 'INFO':
#             print('This massage INFO level')
#         elif level == 'ERROR':
#             print('This massage ERROR level')
#
#
# logger = HybridLogger()
# logger.log('Программа зарущена', 'INFO')
# logger.log('Дебаг информация', 'DEBUG')
# logger.log('Произошла ошибка', 'ERROR')






from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass


    def fly(self):
        return 'Can fly'




class Dog(Animal):
    def sound(self):
        return 'WOF'




class Cat(Animal):
    def sound(self):
        return 'MEOW'




class Bird(Animal):
    def sound(self):
        return 'Chirp'


def make_sound(animal: Animal):
    print(animal.sound())


make_sound(Dog())
make_sound(Cat())


bird = Bird()
print(bird.fly())
dog = Dog()
cat = Cat()
print(dog.sound())
print(cat.sound())
print()






class Shape(ABC):

    @property
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    @property
    def area(self):
        return self.side ** 2


square = Square(6)
print(square.area)
print()






from abc import ABC, abstractmethod
class Account(ABC):
    def __init__(self, balance=0.0, account_number=None):
        self.balance = balance
        self.account_number = account_number


    @abstractmethod
    def deposit(self, amount):
        pass


    @abstractmethod
    def withdraw(self, amount):
        pass




class SavingAccount(Account):
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f'Депозит: {amount}р на аккаунт {self.account_number} | Баланс: {self.balance}')
        else:
            print(f'Сумма дирозита не может быть меньше нуля')


    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f'Списание: {amount}р с аккаунта {self.account_number} | Баланс: {self.balance}')
        else:
            print(f'Сумма Списания не может быть меньше нуля')




class CheckingAccount(Account):
    def deposit(self, amount):
        pass


    def withdraw(self, amount):
        pass


    def checking_accounts(self, customer):
        total = 0
        for account in customer.accounts:
            total += account.balance
        if total >= 2000000:
            return VIPCustomer(customer.name)




class Customer():
    def __init__(self, name):
        self.name = name
        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)


    def transfer(self, from_account, to_account, amount):
        if amount <= from_account.balance:
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f'Перевод от {from_account.account_number} к {to_account}')
        else:
            print('ERROR')




 class AccountComprission():
     def __lt__(self, other):
         return self.balance < other.balance


     def __eq__(self, other):
         return self.balance == other.balance


     def __gt__(self, other):
         return self.balance > other.balance
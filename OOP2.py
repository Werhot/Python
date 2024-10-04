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


    def __lt__(self, other):
        return self.balance < other.balance


    def __eq__(self, other):
        return self.balance == other.balance


    def __gt__(self, other):
        return self.balance > other.balance




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
    def __init__(self, balance=0.0, account_number=None,
                 min_balance=500.0, withdraw_limit=100000.0,
                 tr_fee=50.0):
        super().__init__(balance, account_number)
        self.min_balance = min_balance
        self.withdraw_limit = withdraw_limit
        self.tr_fee = tr_fee


    def deposit(self, amount):
        if amount > 0:
            self.balance += amount - self.tr_fee
            print(f'Депозит: {amount}р на аккаунт {self.account_number} | Баланс: {self.balance}')
        else:
            print(f'Сумма дирозита не может быть меньше нуля')


    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print(f'Сумма привышает допустимый лимит')
        elif self.balance - amount - self.tr_fee < self.min_balance:
            print(f'Сумма привышает допустимый минимум баланса')
        elif 0 < amount <= self.balance:
            self.balance -= amount + self.tr_fee
            print(f'Списание: {amount}р на аккаунт {self.account_number} | Баланс: {self.balance}')
        else:
            print(f'Сумма списания не может быть меньше нуля')


    def checking_accounts(self, customer):
        total = 0
        for account in customer.accounts:
            total += account.balance
        if total >= 2000000:
            print(f'{customer.name} стал VIP клиентом')




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



class VIPCustomer(Customer, CheckingAccount):
    def __init__(self, name, accounts=None):
        Customer.__init__(self, name)
        CheckingAccount.__init__(self)
        self.accounts = accounts if accounts is not None else []
        self.interset_rate = 0.05
        
        
    def apply_interset(self):
        for account in self.accounts:
            if isinstance(account, SavingAccount):
                interset = account.balance * self.interset_rate
                account.deposit(interset)
                print(f'{interset}. Баланс: {account.balance}')
                
                
saving = SavingAccount(1000000, 'C1234')
cheking = CheckingAccount(1200000, 'SA456', min_balance=500, withdraw_limit=10000, tr_fee=50)

customer = Customer('Kate')
customer.add_account(saving)
customer.add_account(cheking)

customer.transfer(saving, cheking, 200000)
customer = cheking.checking_accounts(customer)

saving2 = SavingAccount(500000, 'S4784')
print('Сравнение')
print(saving > saving2)
print(saving == saving2)
print(saving < cheking)

if isinstance(customer, VIPCustomer):
    customer.apply_interset()

print(customer.name)
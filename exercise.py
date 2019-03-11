class BankAccount:

 interest_rate = 1
accounts = []
def __init__(self):
    self.balance = 0

def deposit(self, amount):
    self.balance = amount

def withdraw(self,amount):
        if amount > self.balance:
            print("Cannot withdraw {},The current balance is {}".format(amount,self.balance))
        else:
            self.balance -= amount


@classmethod
def create(cls):
    account = BankAccount()
    cls.accounts.append(accounts)
    return account


@classmethod
def total_funds(cls):
    total_balance = 0
    for account in cls.accounts:
        total_balance += account.balance
    return total_balance

@classmethod
def interest_time(cls):
    for account in cls.accounts:
        account.balance *= cls.interest_rate
    return account.balance            

class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, 'r') as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):
    """Generates checking account"""
    type="chcking"
    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def trasfer(self, amount):
        self.balance = self.balance - amount - self.fee

jacks_checking = Checking("jack.txt", 1)
jacks_checking.trasfer(100)
jacks_checking.commit()
print(jacks_checking.balance)

johns_checking = Checking("john.txt", 1)
johns_checking.trasfer(100)
johns_checking.commit()
print(johns_checking.balance)

# print(johns_checking.type)
# print(johns_checking.__doc__)






# account = Account("balance.txt")
# account.deposit(500)
# account.commit()
# print(account.balance)

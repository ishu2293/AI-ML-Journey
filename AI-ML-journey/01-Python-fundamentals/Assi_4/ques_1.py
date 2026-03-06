#1
class bankAccount:
    def __init__(self, acc_no, owner_name, balance):
        self.acc_no = acc_no
        self.owner_name = owner_name
        self.balance = balance

    def display(self):
        print(f"The account with Account number {self.acc_no} is created with owner name {self.owner_name} and current balance {self.balance}")    

    def deposit(self, amt):
        print(f"Current balance is {self.balance} ")
        self.balance += amt
        print(f"The balance has became {self.balance} ")

    def withdraw(self, amt):
        print(f"Current balance is {self.balance} ")
        self.balance -= amt
        print(f"The balance has became {self.balance} ")    

    def check_balance(self):
        print(f"The current balance is {self.balance}")


acc1 = bankAccount(1, "ishwari", 10_000)
acc1.check_balance()

        
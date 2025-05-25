class BankAccount:
    def __init__(self, name, account, balance=0):
        self.name=name
        self.accno=account
        self.balance=balance

    def deposit(self, amount):
        self.balance+=amount
        print(amount,"is debited from your",self.accno,"accNo")

    def withdraw(self,amount):
        if self.balance<=amount:
            print("Insufficient Balance in your account")
        else:
            self.balance-=amount
            print(amount,"is debited from your",self.accno,"accNo")

    def display_balance(self):
        print("Current balance amount is",self.balance)

acc1=BankAccount("vinayak",7337687291,5000)
acc1.deposit(1000)
acc1.display_balance()
acc1.withdraw(3000)
acc1.display_balance()
acc1.withdraw(3001)
acc1.display_balance()
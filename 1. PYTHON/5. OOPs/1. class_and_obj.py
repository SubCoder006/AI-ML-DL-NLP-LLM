## modeling a bank account using class and object

class BankAccount:
    def __init__(self, account_number,account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Rs.{amount}. New balance: Rs. {self.balance}")
    
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew Rs.{amount}. New balance: Rs. {self.balance}")
            
    def bankInfo(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: Rs. {self.balance}")
        
# creating an object of BankAccount class
account1 = BankAccount("99301200457011", "Subayan Ghosh", 7000)
account1.bankInfo()
account1.deposit(3100)
account1.withdraw(2070)
class BankAccount:
    def __init__(self, int_rate, balance):
        self.rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: " + str(self.balance))
        return self

    def yield_interest(self):
        self.balance = self.balance + self.balance * self.rate
        return self



a = BankAccount(0.1, 10)
a.display_account_info()
print(a.balance)

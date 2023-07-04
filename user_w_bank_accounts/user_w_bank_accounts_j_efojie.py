class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if(self.balance - amount) >= 0:
            self.balance -= amount
        else:
            print("Not enought funds: Chraging $5 fee")
            self balance -= amount

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self


    def make_withdrawl(self, amount):
    self.account.withdraw(amount)
    return self


    def display_user_balance(self):
    print(self.name)
    self.account.display_account_info()









user1 = User("Joshua", "ee@gmail.com")
user1.make_deposit(100).make_deposit(250).display_user_balance()
print(user1.account.balance) 

user2 = User("Bob", "fafa234@gmail.com")
user2.make_depoit(1000).display_user_balance().make_withdrawl(450).display_user_balance()


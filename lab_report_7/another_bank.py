class bank_account:
    def __init__(self, account_number, customer_name, balance=0, email=""):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance
        self.email = email

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited Tk. {amount}. New Balance: Tk. {self.balance}"
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrew Tk. {amount}. New Balance: Tk. {self.balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount."
        else:
            return "Insufficient funds."


class savings_account(bank_account):
    def __init__(self, account_number, customer_name, balance=0, interest_rate=0.05, email=""):
        super().__init__(account_number, customer_name, balance, email)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest calculated: +Tk. {interest}. New Balance: Tk. {self.balance}"
    
    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: Tk. {self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")

class current_account(bank_account):

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: Tk. {self.balance}")
        print(f"Email: {self.email}")


class fixed_deposit_account(savings_account):
    def __init__(self, account_number, customer_name, balance=0, interest_rate=0.05, term_years=0, email=""):
        self.term_years = term_years
        super().__init__(account_number, customer_name, balance, interest_rate, email)
        

    def display_details(self):
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.customer_name}")
        print(f"Balance: Tk. {self.balance}")
        print(f"Interest Rate: {self.interest_rate * 100}%")
        print(f"Term (Years): {self.term_years}")


savings_account = savings_account(
    "Savings123",
    "Bishwajit",
    balance=10000,
    interest_rate=0.05
)
print(savings_account.deposit(500))
print(savings_account.withdraw(200))
print(savings_account.calculate_interest())
savings_account.display_details()
print(f"Email: {savings_account.email}")

current_account = current_account(
    "Current456",
    "Shah Alom"
)
current_account.display_details()

fixed_deposit_account = fixed_deposit_account(
    "Fixed Deposit789",
    "Bishwajit",
    balance=10000,
    interest_rate=0.10
)
print(fixed_deposit_account.deposit(500))
print(fixed_deposit_account.withdraw(200))
print(fixed_deposit_account.calculate_interest())
fixed_deposit_account.display_details()
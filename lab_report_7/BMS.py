from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, interest_rate=0.05):
        super().__init__(account_number, initial_balance)
        self.interest_rate = interest_rate

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Tk. {amount:.2f} into Savings Account {self.account_number}")
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance in Savings Account")
            return None
        self.balance -= amount
        print(f"Withdrew Tk. {amount:.2f} from Savings Account {self.account_number}")
        return self.balance

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Applied interest of Tk. {interest:.2f} to Savings Account {self.account_number}")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, transaction_limit=1000):
        super().__init__(account_number, initial_balance)
        self.transaction_limit = transaction_limit

    def deposit(self, amount):
        if amount > 0:
            print(f"Deposited Tk. {amount:.2f} into Checking Account {self.account_number}")
            return self.balance + amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= self.transaction_limit:
            if amount > 0:
                print(f"Withdrew Tk. {amount:.2f} from Checking Account {self.account_number}")
                return self.balance - amount
            elif amount == 0:
                raise ValueError("Withdrawal amount cannot be zero")
            else:
                print("Transaction limit exceeded for Checking Account")
                return None
        else:
            raise ValueError(f"Transaction limit exceeded for Checking Account")


# Example usage:

savings_account = SavingsAccount(9999, 1111)
print(savings_account.balance)  

checking_account = CheckingAccount(1111, 111)
print(checking_account.balance)  

checking_account.withdraw(111)
print(checking_account.balance)  

savings_account.apply_interest()
print(savings_account.balance)
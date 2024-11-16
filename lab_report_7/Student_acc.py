from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    @abstractmethod
    def withdraw(self, amount):
        pass


class StudentAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, student_id=None):
        super().__init__(account_number, initial_balance)
        self.student_id = student_id

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance in Student Account")
            raise ValueError("Insufficient balance")
        elif self.balance < 100:  
            print(f"No fee for withdrawal of Tk. {amount} from Student Account {self.account_number}")
        else:
            self.balance -= amount
            print(f"Withdrew Tk. {amount} from Student Account {self.account_number}")


class BusinessAccount(BankAccount):
    def __init__(self, account_number, initial_balance=0, overdraft_limit=500):
        super().__init__(account_number, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            print(f"Overdraft limit exceeded for Business Account {self.account_number}. Available balance: Tk. {self.balance}")
            raise ValueError("Overdraft limit exceeded")
        elif amount <= 0:
            print(f"No withdrawal allowed for Business Account {self.account_number}")
        else:
            if self.balance + self.overdraft_limit < amount:
                overdraft_amount = amount - (self.balance + self.overdraft_limit)
                self.balance -= self.overdraft_limit
                print(f"Withdrew Tk. {self.overdraft_limit} from overdraft for Business Account {self.account_number}")
            else:
                self.balance -= amount
                print(f"Withdrew Tk. {amount} from Business Account {self.account_number}")


# Example usage:

student_account = StudentAccount(999990, 9999)
print(student_account.balance)

business_account = BusinessAccount(999991, 9999, 99)
print(business_account.balance)

student_account.withdraw(999)
print(student_account.balance)

business_account.withdraw(999)
print(business_account.balance)

business_account.withdraw(999)
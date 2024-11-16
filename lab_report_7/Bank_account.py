class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

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


class LoanAccount:
    def __init__(self, loan_number, balance=0, interest_rate=0.05):
        self.loan_number = loan_number
        self.balance = balance
        self.interest_rate = interest_rate

    def make_payment(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Paid Tk. {amount}. Remaining Balance: Tk. {self.balance}"
        elif amount <= 0:
            return "Invalid payment amount."
        else:
            return "Payment exceeds loan balance."

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest calculated: +Tk. {interest}. New Balance: Tk. {self.balance}"


class CustomerAccount(BankAccount, LoanAccount):
    def __init__(self, account_number, customer_name, loan_number=None, balance=0, interest_rate=0.05):
        super().__init__(account_number)
        self.customer_name = customer_name
        if loan_number is not None:
            self.loan = LoanAccount(loan_number, balance, interest_rate)

    def display_customer_info(self):
        return f"Customer Name: {self.customer_name}\nAccount Number: {self.account_number}"

    def make_transaction(self, transaction_type, amount):
        if transaction_type == "deposit":
            return self.deposit(amount)
        elif transaction_type == "withdrawal":
            return self.withdraw(amount)
        else:
            raise ValueError("Invalid transaction type.")

    def make_loan_payment(self, payment_amount):
        if isinstance(self.loan, LoanAccount):
            return self.loan.make_payment(payment_amount)
        else:
            raise ValueError("No loan associated with this account.")


# Example usage:

customer = CustomerAccount("1414", "Bishwajit")

print(customer.display_customer_info())

balance_transaction = customer.make_transaction("deposit", 9999)
print(balance_transaction)

withdrawal_transaction = customer.make_transaction("withdrawal", 999)
print(withdrawal_transaction)

loan_number = "LN123"
customer.loan = LoanAccount(loan_number, balance=99999)

interest_calculation = customer.loan.calculate_interest()
print(interest_calculation)

payment_amount = 999
payment_result = customer.make_loan_payment(payment_amount)
print(payment_result)

balance_after_payment = customer.balance + (customer.loan.balance - payment_amount)
print(f"Balance after loan payment: Tk. {balance_after_payment:.2f}")
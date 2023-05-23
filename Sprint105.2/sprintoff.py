class BankAccount:
    def __init__(self, name: str, balance: float):
        self.name = name
        self.balance = balance

    def check_balance(self):
        print(self.name, "has an account balance of:", self.balance)

    def withdraw_money(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        if self.balance < amount:
            raise ValueError("Insufficient funds.")
        self.balance -= amount
        print(f"Withdrew {amount} from {self.name}'s account.")

    def add_money(self, amount: float):
        if amount <= 0:
            raise ValueError("Amount must be a positive number.")
        self.balance += amount
        print(f"Added {amount} to {self.name}'s account.")


def bank_transactions(account):
    print(f"***{account.name}'s Transactions***")
    account.check_balance()
    account.add_money(100.00)
    account.check_balance()
    account.withdraw_money(50.00)
    account.check_balance()


def main():
    account1 = BankAccount("Tyler", 100.00)
    account2 = BankAccount("John", 200.00)
    account3 = BankAccount("Jane", 300.00)

    bank_transactions(account1)
    bank_transactions(account2)
    bank_transactions(account3)


if __name__ == '__main__':
    main()
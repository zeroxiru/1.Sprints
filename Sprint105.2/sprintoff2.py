class BankAccount:
    def __init__(self, name: str, balance: float, birthdate: str = '', password: str = ''):
        self.name = name
        self.balance = balance
        self.birthdate = birthdate
        self.password = password

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

    @classmethod
    def change_user_info(cls, account, new_name: str = '', new_password: str = '', new_birthdate: str = ''):
        if new_name:
            account.name = new_name
            print(f"Name updated for {account.name}")
        if new_password:
            account.password = new_password
            print(f"Password updated for {account.name}")
        if new_birthdate:
            account.birthdate = new_birthdate
            print(f"Birthdate updated for {account.name}")


def bank_transactions(account):
    try:
        print(f"***{account.name}'s Transactions***")
        account.check_balance()
        account.add_money(100.00)
        account.check_balance()
        account.withdraw_money(50.00)
        account.check_balance()
    except ValueError as e:
        print("Transaction failed:", str(e))


def main():
    account1 = BankAccount("Tyler", 100.00, "1990-01-01", "password123")
    account2 = BankAccount("John", 200.00, "1995-05-10", "abc123")
    account3 = BankAccount("Jane", 300.00, "1988-12-25", "pass456")

    bank_transactions(account1)
    bank_transactions(account2)
    bank_transactions(account3)

    # Changing user information
    BankAccount.change_user_info(account1, new_name="Tyler Durden")
    BankAccount.change_user_info(account2, new_password="newpass321", new_birthdate="1995-05-11")
    BankAccount.change_user_info(account3, new_name="Jane Smith", new_birthdate="1990-01-01")


if __name__ == '__main__':
    main()

import csv
import os
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../support/accounts.csv")

class Account:
    def __init__(self, id, balance, open_date, owner=None):
        self.id = id
        if balance < 0:
            raise ValueError("Invalid balance")
        self.balance = balance
        self.open_date = open_date
        self.owner = owner

    def __str__(self):
        return (f"Account ID: {self.id}, Balance = {self.balance}")

    def set_owner(self, owner):
        if self.owner is not None:
            raise Exception("Can not change owner of an account")
        self.owner = owner

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if (self.balance - amount) > 0:
            self.balance -= amount
        else:
            print(f"Your current balance is ${self.balance}.")
            raise ValueError("INSUFFICIENT FUNDS")
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    @classmethod
    def all_accounts(cls):
        with open(path) as accounts_file:
            reader = csv.DictReader(accounts_file)
            accounts_list = []
            for row in reader:
                new_account = cls(
                    int(row["id"]), 
                    int(row["balance"]), 
                    row["open_date"]
                    )
                accounts_list.append(new_account)
        return accounts_list

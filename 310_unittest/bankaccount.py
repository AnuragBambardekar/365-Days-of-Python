class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount

    def get_balance(self):
        return self.balance

import unittest

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        # Create a bank account with an initial balance of $1000
        self.account = BankAccount("12345", 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_invalid_withdraw(self):
        # Attempt to withdraw more than the balance
        self.account.withdraw(1500)
        self.assertEqual(self.account.get_balance(), 1000)  # Balance should remain unchanged

    def test_negative_deposit(self):
        # Attempt to deposit a negative amount
        self.account.deposit(-200)
        self.assertEqual(self.account.get_balance(), 1000)  # Balance should remain unchanged

if __name__ == "__main__":
    unittest.main()

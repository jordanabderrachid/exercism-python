class BankAccount:
    def __init__(self):
        self.balance = 0
        self.is_open = False

    def _assert_open(self):
        if not self.is_open:
            raise ValueError("account not open")

    def get_balance(self):
        self._assert_open()
        return self.balance

    def open(self):
        if self.is_open:
            raise ValueError("account already open")

        self.balance = 0
        self.is_open = True

    def deposit(self, amount):
        self._assert_open()
        if amount < 0:
            raise ValueError("amount must be greater than 0")
        self.balance += amount

    def withdraw(self, amount):
        self._assert_open()
        if self.balance < amount:
            raise ValueError("amount must be less than balance")
        if amount < 0:
            raise ValueError("amount must be greater than 0")

        self.balance -= amount

    def close(self):
        self._assert_open()
        self.is_open = False

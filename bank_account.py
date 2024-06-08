class BalanceException(Exception):
    pass


# ===== Account Name =====


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\n'{self.name}' Account created.\nBalance = ${self.balance:.2f}")

    # ===== Account Balance =====

    def getBalance(self):
        print(f"\n'{self.name}' Account balance = ${self.balance:.2f}")

    # ===== Account Deposits =====

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()

    # ===== Account Transactions =====

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, {self.name} account only has a balance of ${self.balance:.2f}"
            )

    # ===== Account Withdraw =====

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    # ===== Account Transfer =====

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer.......")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!! ✅\n\n **********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")


# ===== Account Reward =====


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()


# ===== Account Saving =====


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, intialAmount, acctName):
        super().__init__(intialAmount, acctName)
        self.fee = 5

    # ===== Savings Withdraw =====

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw completed.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

from bank_account import *

Jason = BankAccount(1000, "Jason")
Lisa = BankAccount(2000, "Lisa")

Jason.getBalance()
Lisa.getBalance()

Lisa.deposit(500)

Jason.withdraw(10000)
Jason.withdraw(10)

Jason.transfer(10000, Lisa)
Jason.transfer(100, Lisa)

Jim = InterestRewardsAcct(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)

Jim.transfer(100, Jason)


Brielle = SavingsAcct(1000, "Brielle")
Brielle.getBalance()
Brielle.deposit(100)

Brielle.transfer(200, Jason)

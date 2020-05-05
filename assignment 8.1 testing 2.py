
class Bank_Account(object):
    def __init__(self, account_number, balance, withdrawl, deposit):
        self.account = account_number
        self.balance = account_balance
        self.withdrawl = withdrawl
        self.deposit = deposit

    def __sub__(self, other):
      return self.balance - other
    
    def __add__(self, other):
      return self.balance + other
        
     
    def withdrawl(self, balance):
        #withdraw funds from Bank Account
        try:
  		    return self.balance - withdrawl
      	except:
            print(f"{withdrawl} is not a valid number")
        	

    def deposit(self, balance):
        #deposit funds into Bank Account
        try:
        	return self.balance + balance
        except:
            print(f"{balance} is not a valid number.")
      			

class Checking_Account(Bank_Account):
    def __init__(self, fees, minimum_balance, checking_account_balance):
        super().__init__(self, account_number, balance, withdrawl, deposit)
        self.fees = fees 
        self.minimum = minimum_balance
        self.checking_account_balance = checking account balance 

    def deduct_fees(self): 
        #deduct $5
        return self.checking_account_balance - fees

    def check_minimum_balance(self):
        #minimum balance is $50
    if balance > 50
        return print(balance)
    else:
        print(f"Your balance is below the minimum balance.  Please deposit funds.")

class Savings_Account(Bank_Account):
    def __init__(self, interest)
        super.__init__(self, account_number, balance, withdrawl, deposit)
        self.interest = interest
      
    def add_interest(self):
        #add 2% interest   return self.interest * self.balance
        return self.interest * balance

BankAcc = Bank_Account(123456, 100, 75, 5)
print(BankAcc.account_number)
print(BankAcc.balance)
print(BankAcc.withdrawl)
print(BankAcc.deposit)

BankAcc.account_number()
BankAcc.balance()
BankAcc.withdrawl()
BankAcc.deposit()

checking = Checking_Account(5, 50, 25)
print(checking.fees)
print(checking.minimum_balance)
print(checking.checking_account_balance)

checking.fees()
checking.minimum_balance()
checking.checking_account_balance(

savings = Savings_Account(1.02)
print(savings.add_interest)

savings.add_interest()
#defining class name
class Bank_account:
#initializing account
    def __init__(self,acc_holder,acc_type,balance=0):
        self.acc_holder=acc_holder
        self.acc_type=acc_type
        self.balance=balance

    def __str__(self):
        return f"{self.acc_holder} ({self.acc_type} account): balance={self.balance}"
    
    def __repr__(self):
        return f"Bank_account(acc_holder='{self.acc_holder}',acc_type='{self.acc_type}',balance={self.balance})"
#Deposit
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"amount deposited successfully.current balance is {self.balance}.")
        else:
            print("deposit amount must be positive.")

#withdraw
    def withdraw(self,amount):
        if amount>0 and amount<=self.balance:
            self.balance-=amount #subtracts the amount from the balance
            print(f"withdraw amount is successfull.current balance is {self.balance}.")
        else:
            print("insufficient amount")

#display balance
    def display_balance(Self):
        print(f"{Self.acc_holder}account balance:{Self.balance}.")

#change account type
    def change_account(self,new):
        self.acc_type=new #updates the old type
        print(f"account changed to {self.acc_type}.")

#coversion USD to INR
    def usd_to_inr(self,usd_amount): 
        conversion_rate=83.96
        inr_amount=usd_amount*conversion_rate
        print(f"{usd_amount}usd is equal to {inr_amount}inr.")
        return inr_amount

#trasfer money
    def transfer(self,other_account,amount):
        if amount <= 0:
            print("Tranfer amount should be positive")
        elif self.balance>=amount:
            self.withdraw(amount)
            other_account.deposit(amount)
            print(f"transferred{amount} to {other_account}.")
        else:
            print("insufficient amount to transfer.")

#fixed deposit
    def fd(self,amount,years):
        interest_rate=0.8 #fixed interest  8% per year
        final_amount=amount*((1+interest_rate)**years)
        print(f"the matured amount after {years} year for  a fd of {amount} at 8% per year is {final_amount}")
        return final_amount
    
def main():
        
    #creating instances
    account1=Bank_account("Noel","savings",2000)
    account2=Bank_account("bob","savings",5000)
    account3=Bank_account("ben","current",500)
    account4=Bank_account("jen","current",1000)

    #performing the operations

    #deposit money
    account1.deposit(200)
    account2.deposit(400)
    account3.deposit(1000)
    account4.deposit(300)

    #withdraw money
    account1.withdraw(100)
    account2.withdraw(600)
    account3.withdraw(400)
    account4.withdraw(50)

    #display balance
    account1.display_balance()
    account2.display_balance()
    account3.display_balance()
    account4.display_balance() 

    #change the account type
    account2.change_account("current")
    account4.change_account("fd")

    #convert USD to INR
    account2.usd_to_inr(400)

    #transfer money 
    account3.transfer(account4,50)

    #fixed deposit
    account1.fd(1500,3)

if __name__ == "__main__":
    main()
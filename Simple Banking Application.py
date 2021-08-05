class BankAccount:

    #constructor
    def __init__(self, bal):
        self.balance = bal
        self.transCount = 0 
    
    #function to get deposit
    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transCount = self.transCount + 1

    #funtion for withdraw
    def withdrawal(self, amount):
        if self.balance >= amount:
            if amount % 10 == 0:
                self.balance = self.balance - amount
                self.transCount = self.transCount + 1
            else:
                print("Error: Withdrawal amount must be in denominations of $10")
        else:
            print("Error: Insufficient funds")
    
   #function to get trans count
    def numofTrans(self):
        return self.transCount
    #function to get balance
    def getBalance(self):
        return self.balance

#function for atm menue
def menu():
    print("1. Check Balance")
    print("2. Make a Deposit")
    print("3. Make a Withdrawal")
    print("4. Display Number of Transactions")
    print("5. Exit")
    print("")
    choice = int(input("Select an Option: "))
    while choice != 1 and choice != 2 and choice != 3 and choice != 4 and choice != 5 :# while loop to make sure user makes a valid choice
        choice = int(input("Invalid Option, Try Again: "))
    return choice #returns user choice
    
def main():
    #initial account balance
    initialBal = float(0)

    CheckingAcc = BankAccount(initialBal) #instance for BankAccount Class
    userchoice = menu()

    while userchoice != 5:
        if userchoice == 1:
            print("Account Balance: ", "$" + format(CheckingAcc.getBalance(), ",.2f"))
            print("")
            userchoice = menu()
        elif userchoice == 2:
            depAmount = float(input("Deposit Amount: "))
            CheckingAcc.deposit(depAmount)
            print("")
            userchoice = menu()
        elif userchoice == 3:
            withdrawalAmount = float(input("Withdrawal Amount: "))
            CheckingAcc.withdrawal(withdrawalAmount)
            print("")
            userchoice = menu()
        elif userchoice == 4:
            print("Transactions completed: ", CheckingAcc.numofTrans())
            print("")
            userchoice = menu()

    if userchoice == 5:
        print("Have a good day.")
main()

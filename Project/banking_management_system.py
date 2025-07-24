# Banking Management System
# store account holder name
# his initial balance
# wants to create account
# wants to deposit
# wants to withdraw
# wants to check balance
# last is exit


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance):
        if account_number in self.accounts:
            return "Account already existed."
        
        if initial_balance < 0:
            return "Initial balance should not be negative."
        
        self.accounts[account_number] = {
            "account_holder" : account_holder,
            "balance" : initial_balance
        }
        return "Account created successfully."

    
    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist."
        
        if amount < 0:
            return "Amount should be more than 0"
        
        self.accounts[account_number]["balance"] += amount
        return f"Deposited ₹{amount} successfully.\nBalance : ₹{self.accounts[account_number]["balance"]}"
    
    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            return "Account does not exist."
        
        if amount < 0:
            return "Amount should be more than 0"
        
        if self.accounts[account_number]["balance"] < amount:
            return "Insufficient Balance"
        
        self.accounts[account_number]["balance"] -= amount
        return f"Withdrawl of ₹{amount} successful.\nBalance : ₹{self.accounts[account_number]["balance"]}"
    
    def check_balance(self, account_number):
        if account_number not in self.accounts:
            return "Account does not exist."
        
        return f"Account Holder : {self.accounts[account_number]["account_holder"]}\nBalance : ₹{self.accounts[account_number]["balance"]}"
    

obj_bank = Bank()

print("-" * 10, "Banking Management System", "-" * 10)
print("\n1. Create Account")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Check Balance")
print("5. Exit")

def show_options():
    
    while True: 
        choice = input("\nEnter your Choice (1 to 5): ")
    
        if choice == "1":
            account_number = input("Enter Account Number : ")
            account_holder = input("Enter Account Holder's Name : ")
            initial_balance = float(input("Enter Initial Balance : "))
            result = obj_bank.create_account(account_number, account_holder, initial_balance)
            print(result)

        elif choice == "2":
            account_number = input("Enter Account Number : ")
            amount = float(input("Enter Amount to Deposit : "))
            result = obj_bank.deposit(account_number, amount)
            print(result)

        elif choice == "3":
            account_number = input("Enter Account Number : ")
            amount = float(input("Enter Amount to Withdraw : "))
            result = obj_bank.withdraw(account_number, amount)
            print(result)

        elif choice == "4":
            account_number = input("Enter Account Number : ")
            result = obj_bank.check_balance(account_number)
            print(result)

        elif choice == "5":
            print("Exit")
            break

        else:
            print("Invalid Choice. Please Try Again !!!")

show_options()
# Banking Management System
# store account holder name
# his initial balance
# wants to withdraw
# wants to check balance
# wants to deposit

class Account:
    def __init__(self, acc_num, name, balance=0.0):
        self.__acc_num = acc_num
        self.__name = name
        self.__balance = balance

    def deposit(self, amnt):
        if amnt > 0:
            self.__balance += amnt
            return True
        else:
            return False

    def withdraw(self, amnt):
        if amnt > self.__balance:
            return False
        else:
            self.__balance -= amnt
            return True

    def check_balance(self):
        return self.__balance   
    
class Bank:
    def __init__(self):
        self.customers = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")

    def make_deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    def make_withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    def check_balance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")   

def main():
    bank = Bank()
    while True:
        print("\nMAIN MENU")
        print("1. NEW ACCOUNT")
        print("2. DEPOSIT AMOUNT")
        print("3. WITHDRAW AMOUNT")
        print("4. BALANCE ENQUIRY")
        print("5. ALL ACCOUNT HOLDER LIST")
        print("6. CLOSE AN ACCOUNT")
        print("7. MODIFY AN ACCOUNT")
        print("8. EXIT")
        ch = input("Select Your Option (1-8): ")

        if ch == '1':
            account_number = input("Enter the account no : ")
            name = input("Enter the account holder name : ")
            initial_balance = float(input("Enter The Initial amount : "))
            bank.create_account(account_number, initial_balance)
        elif ch == '2':
            account_number = input("Enter The account No. : ")
            amount = float(input("Enter the amount to deposit : "))
            bank.make_deposit(account_number, amount)
        elif ch == '3':
            account_number = input("Enter The account No. : ")
            amount = float(input("Enter the amount to withdraw : "))
            bank.make_withdrawal(account_number, amount)
        elif ch == '4':
            account_number = input("Enter The account No. : ")
            bank.check_balance(account_number)
        elif ch == '5':
            # Implement display all accounts
            pass
        elif ch == '6':
            account_number = input("Enter The account No. : ")
            # Implement delete account
            pass
        elif ch == '7':
            account_number = input("Enter The account No. : ")
            # Implement modify account
            pass
        elif ch == '8':
            print("Thanks for using bank management system")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()   
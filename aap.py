# Class to represent the user's bank account
class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be greater than zero!")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Successfully withdrew {amount}. New balance: {self.balance}")
            else:
                print(f"Insufficient balance! Your balance is {self.balance}.")
        else:
            print("Withdrawal amount must be greater than zero!")

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")
        return self.balance

# Class to represent the ATM
class ATM:
    def __init__(self, account):
        self.account = account

    def display_menu(self):
        print("\n--- ATM Interface ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

    def start(self):
        while True:
            self.display_menu()
            choice = input("Choose an option (1-4): ")
            
            if choice == '1':
                self.account.check_balance()

            elif choice == '2':
                amount = float(input("Enter the amount to deposit: "))
                self.account.deposit(amount)

            elif choice == '3':
                amount = float(input("Enter the amount to withdraw: "))
                self.account.withdraw(amount)

            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid option! Please select a valid option.")

# Main program
if __name__ == "__main__":
    # Create a bank account with an initial balance
    account = BankAccount(initial_balance=1000)  # Example starting balance
    atm = ATM(account)
    
    # Start the ATM interface
    atm.start()

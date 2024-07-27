class ATM:
    def __init__(self, pin):
        """
        Initializes the ATM instance with an initial balance, PIN, and empty transaction history.
        """
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, input_pin):
        """
        Checks if the input PIN matches the stored PIN.
        """
        return self.pin == input_pin

    def inquire_balance(self):
        """
        Returns the current balance.
        """
        return self.balance

    def deposit_cash(self, amount):
        """
        Deposits the specified amount into the balance if the amount is positive.
        Logs the transaction if successful.
        """
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return True
        return False

    def withdraw_cash(self, amount):
        """
        Withdraws the specified amount from the balance if the amount is valid.
        Logs the transaction if successful.
        """
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return True
        return False

    def change_pin(self, old_pin, new_pin):
        """
        Changes the PIN if the old PIN is correct.
        Logs the transaction if successful.
        """
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            return True
        return False

    def get_transaction_history(self):
        """
        Returns the transaction history.
        """
        return self.transaction_history

# Example usage
def main():
    # Create an ATM instance with an initial PIN
    atm = ATM(pin="1234")

    while True:
        # Display the menu
        print("\nWelcome to the ATM Machine!")
        print("1. Balance Inquiry")
        print("2. Cash Deposit")
        print("3. Cash Withdrawal")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        # Get user's choice
        choice = input("Please choose an option: ")

        if choice == "1":
            # Balance Inquiry
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                print(f"Your current balance is: ${atm.inquire_balance()}")
            else:
                print("Incorrect PIN.")

        elif choice == "2":
            # Cash Deposit
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                amount = float(input("Enter amount to deposit: "))
                if atm.deposit_cash(amount):
                    print(f"Deposited ${amount} successfully.")
                else:
                    print("Invalid amount.")
            else:
                print("Incorrect PIN.")

        elif choice == "3":
            # Cash Withdrawal
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                amount = float(input("Enter amount to withdraw: "))
                if atm.withdraw_cash(amount):
                    print(f"Withdrew ${amount} successfully.")
                else:
                    print("Insufficient funds or invalid amount.")
            else:
                print("Incorrect PIN.")

        elif choice == "4":
            # Change PIN
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            if atm.change_pin(old_pin, new_pin):
                print("PIN changed successfully.")
            else:
                print("Incorrect old PIN.")

        elif choice == "5":
            # Transaction History
            pin = input("Enter your PIN: ")
            if atm.check_pin(pin):
                history = atm.get_transaction_history()
                if history:
                    print("Transaction History:")
                    for transaction in history:
                        print(transaction)
                else:
                    print("No transactions found.")
            else:
                print("Incorrect PIN.")

        elif choice == "6":
            # Exit
            print("Thank you for using the ATM Machine. Goodbye!")
            break

        else:
            # Invalid option
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

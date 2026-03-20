import json
import os


class Bank:

    def __init__(self):

        self.file = "account.json"

        if not os.path.exists(self.file):
            with open(self.file, "w") as f:
                json.dump({}, f)

        self.menu()

    # FILE FUNCTIONS

    def storage_read(self):

        try:
            with open(self.file, "r") as file:
                data = json.load(file)
        except:
            data = {}

        return data

    def storage_write(self, data):

        with open(self.file, "w") as file:
            json.dump(data, file, indent=4)

    # MAIN MENU 

    def menu(self):

        while True:

            print("\n***** Bank Management System *****")
            print("1. Create New Account")
            print("2. Login")
            print("3. Exit")

            choose = input("Enter your choice: ")

            if choose == "1":
                self.new_account()

            elif choose == "2":
                self.login()

            elif choose == "3":
                print("\n***** Thank you for using Bank System *****")
                break

            else:
                print("Enter valid number")

    # CREATE ACCOUNT 

    def new_account(self):

        data = self.storage_read()

        print("\n***** Create New Account *****")

        name = input("Enter your name: ")

        account_number = name + str(1000 + len(data) + 1)

        print("Your account number:", account_number)

        while True:

            pin = input("Enter 4 digit pin: ")

            if len(pin) == 4 and pin.isdigit():
                break
            else:
                print("Pin must be 4 digits")

        data[account_number] = {
            "name": name,
            "pin": pin,
            "balance": 0,
            "transactions": []
        }

        self.storage_write(data)

        print("***** Account created successfully *****")

    # LOGIN 

    def login(self):

        data = self.storage_read()

        print("\n***** Login *****")

        account = input("Enter account number: ")
        pin = input("Enter pin: ")

        if account in data and data[account]["pin"] == pin:

            print("***** Login successful *****")
            self.account_menu(account)

        else:
            print("Invalid account or pin")

    # ACCOUNT MENU 

    def account_menu(self, account):

        while True:

            print("\n***** Account Menu *****")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Reset Pin")
            print("5. Passbook")
            print("6. Logout")

            choice = input("Enter choice: ")

            if choice == "1":
                self.check_balance(account)

            elif choice == "2":
                self.deposit(account)

            elif choice == "3":
                self.withdraw(account)

            elif choice == "4":
                self.reset_pin(account)

            elif choice == "5":
                self.passbook(account)

            elif choice == "6":
                print("***** Logged out successfully *****")
                break

            else:
                print("Invalid choice")

    # BALANCE 

    def check_balance(self, account):

        data = self.storage_read()

        print("\n***** Balance Details *****")
        print("Balance:", data[account]["balance"])

    # DEPOSIT 

    def deposit(self, account):

        data = self.storage_read()

        print("\n***** Deposit Money *****")

        amount = input("Enter amount to deposit: ")

        if amount.isdigit():

            amount = int(amount)

            if amount <= 0:
                print("Amount must be greater than 0")
                return

            data[account]["balance"] += amount

            data[account]["transactions"].append(f"[+] Deposit : +{amount}")

            self.storage_write(data)

            print(f"***** ₹{amount} deposited successfully *****")
            print(f"Updated Balance: ₹{data[account]['balance']}")

        else:
            print("Invalid amount")

    # WITHDRAW 

    def withdraw(self, account):

        data = self.storage_read()

        print("\n***** Withdraw Money *****")

        amount = input("Enter amount to withdraw: ")

        if amount.isdigit():

            amount = int(amount)

            if amount <= 0:
                print("Amount must be greater than 0")

            elif amount > data[account]["balance"]:
                print("Insufficient balance")

            else:
                data[account]["balance"] -= amount

                data[account]["transactions"].append("[-] Withdraw : -" + str(amount))

                self.storage_write(data)

                print("***** Withdrawal successful *****")
                print("Remaining Balance:", data[account]["balance"])
        else:
            print("Invalid amount")

    # RESET PIN 

    def reset_pin(self, account):

        data = self.storage_read()

        print("\n***** Reset Pin *****")

        current_pin = input("Enter current pin: ")

        if current_pin != data[account]["pin"]:
            print("Wrong pin")
            return

        new_pin = input("Enter new 4 digit pin: ")

        if len(new_pin) == 4 and new_pin.isdigit():

            data[account]["pin"] = new_pin

            self.storage_write(data)

            print("***** Pin changed successfully *****")

        else:
            print("Invalid pin")

    # PASSBOOK 

    def passbook(self, account):
        data = self.storage_read()

        print("\n***** Passbook *****")

        print("Account Number:", account)
        print("Name:", data[account]["name"])
        print("Balance:", data[account]["balance"])

        print("\nTransactions:")
        
        if len(data[account]["transactions"]) == 0:
            print("No transactions yet")

        else:
            count = 1
            for t in data[account]["transactions"]:
                print(str(count) + ".", t)
                count += 1


Bank()
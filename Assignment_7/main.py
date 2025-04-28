# Importing Modules
import msvcrt

# Bank Class
class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        print("\nProcedure of creating an account will take 5 to 10 minutes...\n")

        def user_details():
            print("User Details:")
            name = input("Enter your Full Name (as per CNIC): ")
            gender = input("Enter your Gender (M/F/O): ")
            CNIC = input("Enter your CNIC (00000-0000000-0): ")
            mobile_number = input("Enter your Mobile Number: ")
            email_address = input("Enter your Email Address: ")
            marital_status = input("Enter your Marital Status (M/U): ")
            father_name = input("Enter your Father Name: ")
            mother_name = input("Enter your Mother Name: ")
            spouse_name = input("Enter your Spouse Name: ")
            DOB = input("Enter your Date of Birth (DD/MM/YYYY): ")
            POB = input("Enter your Place of Birth: ")
            religion = input("Enter your Religion: ")

            return {
                "Name": name,
                "Gender": gender,
                "CNIC": CNIC,
                "Mobile Number": mobile_number,
                "Email Address": email_address,
                "Marital Status": marital_status,
                "Father Name": father_name,
                "Mother Name": mother_name,
                "Spouse Name": spouse_name,
                "Date of Birth": DOB,
                "Place of Birth": POB,
                "Religion": religion
            }

        def account_info():
            print("\nAccount Details:")
            account_title = input("Please enter Account Title: ")

            while True:
                try:
                    account_number = int(input("Please enter Account Number (only digits): "))
                    break
                except ValueError:
                    print("Invalid input! Account Number must be an integer.")

            currency = input("Please enter Currency (e.g., PKR, USD): ")

            pin = self.input_pin_creation()

            print("\nYour PIN is stored securely!\n")
            balance = 0

            return {
                "Account Title": account_title,
                "Account Number": account_number,
                "Currency": currency,
                "PIN": pin,
                "Balance": balance
            }

        while True:
            UserDetails = user_details()
            print("\nYour details:")
            for key, value in UserDetails.items():
                print(f"{key}: {value}")

            confirmation = input("\nIs this correct? (Y/N): ").lower()
            if confirmation == 'y':
                print("\nAlmost done...")
                break
            elif confirmation == 'n':
                print("\nPlease re-enter your correct details!\n")
            else:
                print("Invalid input! Please enter again.\n")

        AccountDetails = account_info()

        # Merge details
        merged_details = {**UserDetails, **AccountDetails}
        self.accounts.append(merged_details)

        print("\n✅ Your account has been created successfully!")
        print("\nAccount Summary: -")
        for key, value in merged_details.items():
            print(f"{key}: {value}")

    def input_pin_creation(self):
        print("\nCreate your 4-digit PIN:")
        pin = ""
        while len(pin) < 4:
            ch = msvcrt.getch()
            if ch.isdigit():
                pin += ch.decode()
                print("*", end="", flush=True)
        print()
        return pin

    def find_account(self, account_number, pin):
        for account in self.accounts:
            if account["Account Number"] == account_number and account["PIN"] == pin:
                return account
        return None

    def remove_account(self, account):
        print("\nAccount Removal Process Initialized.")
        while True:
            confirm = input("Are you sure you want to delete this account? (Y/N): ").lower()

            # Search for the account
            if confirm == 'y':
                if account in self.accounts:
                    self.accounts.remove(account)
                    print("\n✅ Your account has been successfully removed!")
                else:
                    print("\n⚠️ Error! Account not found in system.")
                break
            elif confirm == 'n':
                print("\n❌ Account removal cancelled.")
                break
            else:
                print("Invalid Input!\nPlease select valid option.\n")

# ATM Class
class ATM:
    def __init__(self, bank):
        self.bank = bank
        self.current_account = None
        self.logged_in_account = None

    def login(self):
        while True:
            login_menu = input("\nLogin (L)\nDon't have an account? Create Account (C)\nExit (E)\nSelect any: ").lower()

            if login_menu == 'l':
                try:
                    account_number = int(input("\nEnter your Account Number: "))
                except ValueError:
                    print("Account number must be an integer!")
                    continue

                print("Enter your PIN: ", end="", flush=True)
                pin = self.input_pin()

                account = self.bank.find_account(account_number, pin)
                if account:
                    print("\n✅ Login Successful!")
                    self.current_account = Account(account)
                    self.logged_in_account = account
                    self.show_menu()
                else:
                    print("\n❌ Incorrect Account Number or PIN!")
            elif login_menu == 'c':
                self.bank.create_account()
            elif login_menu == 'e':
                print("\nThank you for using our ATM!\n")
                break
            else:
                print("\nInvalid Input!")

    def input_pin(self):
        pin = ""
        while True:
            ch = msvcrt.getch()
            if ch == b'\r':
                break
            elif ch == b'\x08':
                if len(pin) > 0:
                    pin = pin[:-1]
                    print('\b \b', end="", flush=True)
            elif ch.isdigit():
                pin += ch.decode()
                print('*', end="", flush=True)
        return pin

    def show_menu(self):
        while True:
            print("""
ATM Menu:
1. Check Balance
2. Deposit
3. Withdraw
4. Remove Account
5. Logout
""")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.current_account.check_balance()
            elif choice == '2':
                self.current_account.deposit()
            elif choice == '3':
                self.current_account.withdraw()
            elif choice == '4':
                bank.remove_account(self.logged_in_account)
                break
            elif choice == '5':
                print("\nLogged out successfully.\n")
                break
            else:
                print("\nInvalid choice!\nPlease select a valid option")

# Account Class
class Account:
    def __init__(self, account_info):
        self.account_info = account_info

    def check_balance(self):
        print(f"\nYour Current Balance: {self.account_info['Balance']} {self.account_info['Currency']}")

    def deposit(self):
        try:
            amount = float(input("\nEnter amount to deposit: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            else:
                self.account_info['Balance'] += amount
                print(f"✅ {amount} deposited successfully!\nNew Balance: {self.account_info['Balance']} {self.account_info['Currency']}")
        except ValueError:
            print("Invalid amount!")

    def withdraw(self):
        try:
            amount = float(input("\nEnter amount to withdraw: "))
            if amount <= 0:
                print("Amount must be greater than zero.")
            elif amount > self.account_info['Balance']:
                print("Insufficient Balance!")
            else:
                self.account_info['Balance'] -= amount
                print(f"✅ {amount} withdrawn successfully!\nNew Balance: {self.account_info['Balance']} {self.account_info['Currency']}")
        except ValueError:
            print("Invalid amount!")

# Main Code
if __name__ == "__main__":
    print("{:-^50}".format(" Welcome to the ATM "))

    bank = Bank()
    atm = ATM(bank)

    atm.login()
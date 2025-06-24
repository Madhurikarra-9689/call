import time

print("Please insert your CARD")
time.sleep(5)

# ATM pin and initial balance
password = 1234
balance = 5000

# Get user input for PIN
pin = int(input("Enter your ATM pin: "))

if pin == password:
    while True:
        print("""
        1 - Check Balance 
        2 - Withdraw Balance
        3 - Deposit Balance
        4 - Exit
        """)

        try:
            option = int(input("Please enter your choice: "))

            if option == 1:
                print(f"Your current balance is: {balance}")

            elif option == 2:
                withdraw_amount = int(input("Please enter amount to withdraw: "))
                if withdraw_amount <= balance:
                    balance -= withdraw_amount
                    print(f"{withdraw_amount} has been debited from your account.")
                else:
                    print("Insufficient funds.")

            elif option == 3:
                deposit_amount = int(input("Please enter amount to deposit: "))
                balance += deposit_amount
                print(f"{deposit_amount} has been credited to your account.")
                print(f"your updated balance is {balance}")

            elif option == 4:
                print("Exiting...")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Please enter a valid option.")

else:
    print("Wrong PIN. Please try again.")

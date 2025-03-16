def show_balance(balance):
    print("**********************")
    print(f"your balance is ${balance:.2f}")
    print("**********************")


def deposit():
    amount = float(input("Enter the amount to deposit :"))

    if amount < 0:
        print("**********************")
        print("That is not a valid amount")
        print("**********************")
        return 0
    else :
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to withdraw"))
    if amount > balance:
        print("**********************")
        print("insufficient balance")
        print("**********************")
        return 0
    elif amount < 0:
        print("**********************")
        print("Not a valid amount")
        print("**********************")
        return 0
    else :
        return amount

def main():

    balance = 0
    is_running = True

    while is_running:
        print("**********************")
        print("    Banking Program    ")
        print("**********************")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Quit")
        print("**********************")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else :
            print("**********************")
            print("That is not a valid choice ")
            print("**********************")
    print("**********************")
    print("Thank you have a nice day :) !")
    print("**********************")

if __name__ == '__main__':
   main()


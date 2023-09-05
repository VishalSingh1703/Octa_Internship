pin=int(input("Enter your 4 digit pin: "))    # Default pin set is 1010
balance=5000

def banking(pin):
    global balance
    if pin==1010:
        io=int(input("----------------------Enter a number from menu----------------------- \n1: check balance \n2: withdraw cash \n3: deposit cash \n4: exit\n"))
        if io==1:   # Check Balance
            print("Balance: ",balance)
            banking(pin)

        elif io==2: # Withdraw
            withdrawal=int(input("Enter the amount: "))
            if balance>0 and withdrawal<=balance:
                balance-=withdrawal
            else:
                print("Insufficient Balance left ")
            banking(pin)

        elif io==3: # Deposit
            amount=int(input("Enter the amount you want to deposit: "))
            balance+=amount
            banking(pin)

        elif io==4: # Exit
            print("Thank you")
        else:
            print("Invalid number input, please enter 1,2,3 or 4 only")
            banking(pin)

    else: # Incase of incorrect pin. Enter again
        print("Incorrect pin!!")
        pin = int(input("Please enter your 4 digit pin again: "))
        banking(pin)

banking(pin)
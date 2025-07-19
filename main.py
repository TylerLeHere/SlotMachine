def deposit():
    # Responsible for collecting user input that gets deposit from the user
    while True:
        amount = input("What would you like to deposit? $")
        #Check amount if it is an actual number
        if amount.isdigit():
            amount = int(amount)
            if amount >= 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    
    return amount

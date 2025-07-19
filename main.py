MAX_LINES = 3
def deposit():
    # Responsible for collecting user input that gets deposit from the user
    while True:
        amount = input("What would you like to deposit? $")
        #Check amount if it is an actual number
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0")
        else:
            print("Please enter a number")
    
    return amount

# I want to collect the bet from user, determine how much they want to bet and how many lines
def getNumberOfLines():
    while True:
        lines = input("Enter the number of lines you want to be on (1-)" + str(MAX_LINES) + ")? ")
        if lines.isDigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number. ")

def main():
    balance = deposit()
    lines = getNumberOfLines()
    print(balance, lines)
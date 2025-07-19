MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

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
        lines = input("Enter the number of lines you want to be on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number. ")
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between {MIN_BET} - {MAX_BET}. ")
        else:
            print("Please enter a number")
    return amount

def main():
    balance = deposit()
    lines = getNumberOfLines()
    while True:

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Total bet is equal to ${total_bet}")

if __name__ == "__main__":
    main()

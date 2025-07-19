import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_values = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # Just need to look at the rows
    for line in range(lines):
        #Check every symbol is the same
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break # Break out, check the next line because they did not win
        else:
            winnings += values[symbol] * bet
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbol = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    
    columns = [] #Each of the nest lists represents columns
    for _ in range(cols):
        column = []
        current_symbols = all_symbol[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
        # Want to add the value into the column
    return columns
            
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()



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


def spin(balance):
    lines = getNumberOfLines()
    while True:

        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Total bet is equal to ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winning, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won {winning}. ")
    print(f"You won on lines: ", *winning_lines)
    return winning - total_bet #Tell how much the client wins or loss


def main():
    balance = deposit()
    while True: 
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")

if __name__ == "__main__":
    main()

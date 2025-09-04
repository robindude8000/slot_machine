
import random


# Define Global Variables
MAX_LINES = 10
MAX_BET = 500
MIN_BET = 10
MIN_DEPOSIT = MIN_BET

ROWS = 3
COLS = 3

SYMBOL_DICT = {
	# Chances of occurence
	"A": 2, 
	"B": 4,
	"C": 6,
	"D": 8,
	"E": 10
}

SYMBOL_VALUE = {
	# The lower the number, the higher the multiplier of score
	"A": 10, 
	"B": 8,
	"C": 6,
	"D": 4,
	"E": 2
}


# Create game logic
def deposit():
	while True:
		try:
			amount = int(input("How much would you like to deposit? $ "))
			if amount < MIN_DEPOSIT:
				print(f"Minimum deposit value is ${MIN_DEPOSIT}.")
				continue
			else:
				break
		except ValueError:
			print("Please enter a number.")
	
	return amount



def get_number_of_lines():
	while True:
		lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ") ")
		if lines.isdigit():
			lines = int(lines)
			if MAX_LINES >= lines > 0:
				break
			else:
				print("Number of lines should not exceed to " + str(MAX_LINES) + ".")
		else:
			print("Please enter a number.")

	return lines



def get_bet():
	while True:
		bet = input("How much would you like to bet? $ ")
		if bet.isdigit():
			bet = int(bet)
			if MAX_BET >= bet >= MIN_BET:
				break
			else:
				print(f"Bet amount should be between ${MIN_BET} and ${MAX_BET}.")
		else:
			print("Please enter a number.")

	return bet



def get_slot_machine_spin(rows, cols, symbols):
	# create a list that contains the all different values we could select from our dictionary
	all_symbols = []
	for symbol, count in symbols.items():
		for i in range (count):
			all_symbols.append(symbol)

	# pick 3 symbols from all_symbols
	spin_result = []
	for _ in range(cols):
		layer = []
		spin_result.append(layer)
		for _ in range(rows):
			value = random.choice(all_symbols)
			layer.append(value)

	return spin_result



def print_slot_machine(spin_result):
	for row in spin_result:
		print("| " + " | ".join(row) + " |")



def check_winnings(row, bet):
    line_won = 0
    winnings = 0

    for each_row in row:
        # Check if all symbols in the row are the same
        if len(set(each_row)) == 1:
            line_won += 1
            symbol = each_row[0]  # all are the same, so take the first
            multiplier = SYMBOL_VALUE[symbol]
            winnings += bet * multiplier  # apply symbol multiplier

    if line_won == 0:
        print("\nThe odds are not in your favor. Try again!\n")
    else:
        print(f"\nCongratulations! You won ${winnings} on {line_won} line(s)!\n")

    return winnings


# Main Game
def main():
    print("IT'S SCATTER TIME!!!")
    print("====================")
    balance = deposit()

    while True:
        print(f"\nYour current balance is: ${balance}")

        # Ask for lines and bet again each round
        lines = get_number_of_lines()

        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > balance:
                print(f"Not enough balance to bet that amount. Your current balance is ${balance}.")
            else:
                break

        print(f"You are betting ${bet} on {lines} line(s). Total bet = ${total_bet}. Good luck!")

        # Deduct total bet
        balance -= total_bet

        # Spin loop
        roll = input("Roll the slot machine? (y/n): ").lower()
        if roll == "y":
            slots = get_slot_machine_spin(ROWS, lines, SYMBOL_DICT)

            print("\n=============")
            print_slot_machine(slots)
            print("=============\n")

            # Check winnings and update balance
            winnings = check_winnings(slots, bet)
            balance += winnings
            print(f"Your new balance is: ${balance}")

            if balance < MIN_BET:
                print("\nYou don’t have enough balance to continue. Game over!")
                break

        elif roll == "n":
            print(f"Thank you for playing! You are leaving with ${balance}.")
            break
        else:
            print("Invalid response.")
            continue
	

	

# Run the game
main()


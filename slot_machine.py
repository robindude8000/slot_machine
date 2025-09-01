
import random


# Define Global Variables
MAX_LINES = 3
MAX_BET = 500
MIN_BET = 10
MIN_DEPOSIT = MIN_BET

ROWS = 3
COLS = 3

SYMBOL_DICT = {
	# The lower the number, the higher the multiplier of score
	"A": 2, 
	"B": 3,
	"C": 4,
	"D": 5
}


def check_winnings(row):
	line_won = 0
	for each_row in row:
		if len(set(each_row)) == 1:
			line_won += 1
		else:
			continue

	if line_won == 0:
		print("The odds are not in your favor. Try again!")
	else:
		print(f"Congratulations! You won {line_won} line(s)! ")



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


def main():
	balance = deposit()
	lines = get_number_of_lines()
	
	# Validate the balance
	while True:
		bet = get_bet()
		total_bet = bet * lines

		if total_bet > balance:
			print(f"Not enough balance to bet that amount. Your current balance is ${balance}.")
		else:	
			print(f"You are betting ${bet} on {lines} line(s). Total bet is equal to: ${total_bet}! Goodluck!")
			break
	
	# Roll the slot machine
	while True:	
		roll = str(input("Roll the slot machine? (y/n): "))
		if roll == 'y':
			slots = get_slot_machine_spin(ROWS, lines, SYMBOL_DICT)

			print("=============")
			print_slot_machine(slots)
			print("=============")
			print("")

			break
		elif roll == 'n':
			print("Thank you for playing! Come back again! ")
			break
		else:
			print("Invalid Response.")
			continue

	# Check winnings
	check_winnings(slots)
	

	

# Run the game
main()


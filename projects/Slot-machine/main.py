MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

def deposit():
    while True:
        amount = input("What ever you want $")
        if amount.isdigit():
           amount = int(amount)
           if amount > 0:
               break
           else:
               print("The amount is greater than zero.")
        else:
            print("Please Enter a number")
    return amount
deposit()

def get_number_of_lines():
    while True:
        lines = input("Enter the nuber of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
           lines = int(lines)
           if 1 < lines <= MAX_LINES:
               break
           else:
               print("Enter Valid Number of Lines")
        else:
            print("Please Enter a number")
    return lines

    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()
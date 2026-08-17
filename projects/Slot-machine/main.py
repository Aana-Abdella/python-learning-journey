MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

def deposit():
    while True:
        amount = input("How much would you like to deposit$")
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
def get_bet():
    while True:
            amount = input("What would you like to bet on each line? $")
            if amount.isdigit():
               amount = int(amount)
               if MIN_BET <=amount <= MAX_BET:
                   break
               else:
                   print(f"Amount is must be between ${MIN_BET} - ${MAX_BET}.")
            else:
                print("Please Enter a number")
    return amount
    

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet >= balance:
            print(f"you dont have enough balance to bet that amount, your current balance is: ${balance}")

        else:
            break

    print(f"you are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

main()
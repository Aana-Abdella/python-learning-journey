
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
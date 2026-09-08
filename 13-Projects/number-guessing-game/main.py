import random

print("Welcome to the number guessing game")

top_of_range = input("Type a Number: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <=  0 :
        print("Please Enter a Number larger that 0 Next time ")
        quit() 
else: 
    print("pleare enter a number next time.")
    quit()

random_number = random.randint(0, top_of_range)
number_of_guesses = 0

while True:
    number_of_guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit() :
        user_guess = int(user_guess)
    else:
        print("Please enter a number next time.")
        continue

    if user_guess == random_number :
        print("You got it right!")
        break
    else:
        print("You got it wrong!")

print("You got it in " + str(number_of_guesses) + " guesses")
     


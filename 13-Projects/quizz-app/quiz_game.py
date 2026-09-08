print("Welcome to The guizz game")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print('Let lets start quizz')

answer = input('what is CPU stands for ? ')
score = 0 
if answer.lower() == 'central processing unit' :
    print('correct')
    score += 1

else:
    print('incorrect')

answer = input('what is GPU stands for ? ')

if answer.lower() == 'graphical processing unit' :
    print('correct')
    score += 1

else:
    print('incorrect')

answer = input("What RAM stands for ? ")

if answer.lower() == 'random access memory' :
    print("Correct!")
    score += 1

else :
    print("Incorrect")

answer = input("What USB stands for ? ")

if answer.lower() == "universal serial bus" :
    print("Correct!")
    score += 1
else :
    print("Incorrect")


print(f"you scored {score} . ")
print("you got " + str(score) + " questions correct!")
print("you got " + str(4 - score) + " questions incorrect!")
print("you got " + str((score / 4) * 100) + "%")

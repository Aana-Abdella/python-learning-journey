age = int(input("Please enter your age ?"))

student = int(input("Please enter 1 if you are student or 0 if not student"))

if age >= 18 and student == 1 :

    print("You are adult student")
else:
    print("You are younger student")




num1 = int(input("The first number"))

selct_operation = str(input("select operation"))

num2 = int(input("input the second number"))

if select_operation == + :
        print(num1 + num2)
elif select_operation == '-' :
        print(num1 - num2)
elif selct_operation == '*' :
        print(num1 * num2)
else:
        print(num1/num2)
    




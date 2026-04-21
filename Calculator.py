# Simple calculator program in Python

# This program takes two numbers and an operation choice from the user, then performs the selected operation and displays the result.

firstNum = int(input("Enter the first number: "))
secondNum = int(input("Enter the second number: "))
operation = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, and 4 for division: "))
if operation == 1:
    print("The sum of the two numbers is: ", firstNum + secondNum)
elif operation == 2:
    print("The difference of the two numbers is: ", firstNum - secondNum)
elif operation == 3:
    print("The product of the two numbers is: ", firstNum * secondNum)
elif operation == 4:
    if secondNum == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("The quotient of the two numbers is: ", firstNum / secondNum)
else:
    print("Invalid operation choice.")
print("Thank you for using the calculator!")    
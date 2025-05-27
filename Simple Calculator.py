#Lets make a simple calculator that can add, subtract, multiply, and divide two numbers. The user will be prompted to enter two numbers and the operation they want to perform. The program will then display the result of the operation.
#The program will also handle invalid inputs and display an error message if the user enters an invalid operation.

#Lets show the available operations to the user
print("Welcome to the simple calculator!")
print("The available operations are:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

#ask the user which operation they want to perform
operation = input("Please enter the operation you want to perform (+, -, *, /): ")

#ask the user to enter two numbers
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))

#perform the operation based on user input
if operation == "+":
    result = num1 + num2
    print(f"The result of {num1} + {num2} is: {result}")
elif operation == "-":
    result = num1 - num2
    print(f"The result of {num1} - {num2} is: {result}")
elif operation == "*":
    result = num1 * num2
    print(f"The result of {num1} * {num2} is: {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Error: Can't divide by zero!")
else:
    print("Invalid input, please enter +, -, *, or /")

#This is a simple calculatornum1, op, num2 = input().split()  
try:
    # Prompt the user for input
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")

    # Convert input to float
    num1, num2 = float(num1), float(num2)

    # Perform calculations
    result = num1 + num2
    print("The result is:", result)
except ValueError:
    print("Invalid input! Please enter numeric values.")


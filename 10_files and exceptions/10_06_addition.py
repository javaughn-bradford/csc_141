#10_06_addition 


try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))

    # addition equation
    result = num1 + num2
    print("The total of the two numbers is:", result)

except ValueError:
    # (Error)When the input is not a number
    print("Oops! You didn't enter a valid number. Please enter numeric values.")

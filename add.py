def calculate_factorial(number):
    factorial = 1

    # Check if the number is negative, positive, or zero
    if number < 0:
        print("Factorial is not defined for negative numbers.")
    elif number == 0:
        print("The factorial of 0 is 1.")
    else:
        # Loop to calculate factorial
        for i in range(1, number + 1):
            factorial *= i

        print(f"The factorial of {number} is {factorial}.")

# Example: Calculate factorial of a given number
user_input = int(input("Enter a number to calculate its factorial: "))
calculate_factorial(user_input)

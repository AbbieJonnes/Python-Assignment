import math  # Import math library for sqrt()

# Ask for a number
number = float(input("Enter a number to find its square root: "))

# Check for negative input
if number < 0:
    print("Error: Cannot compute square root of a negative number.")
else:
    # Calculate and print the square root
    sqrt_value = math.sqrt(number)
    print(f"The square root of {number} is {sqrt_value}")
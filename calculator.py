# Perform all basic arithmetic operations on two numbers

# Get user inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
print(f"\nResults for numbers {num1} and {num2}:\n")

print(f"Addition (+): {num1 + num2}")
print(f"Subtraction (-): {num1 - num2}")
print(f"Multiplication (*): {num1 * num2}")

if num2 != 0:
    print(f"Division (/): {num1 / num2}")
    print(f"Modulus (%): {num1 % num2}")
    print(f"Floor Division (//): {num1 // num2}")
else:
    print("Division (/): Error - Cannot divide by zero.")
    print("Modulus (%): Error - Cannot divide by zero.")
    print("Floor Division (//): Error - Cannot divide by zero.")

print(f"Exponentiation (**): {num1 ** num2}")

#%%
# Task 1: Arithmetic Operations
# The performs basic arithmetic operations on two numbers entered by the user.

# Taking two numbers as input from the user
num1 = float(input("Enter the first number: "))  # First number
num2 = float(input("Enter the second number: "))  # Second number

# Performing arithmetic operations
addition = num1 + num2  # Adding the numbers
subtraction = num1 - num2  # Subtracting the second number from the first
multiplication = num1 * num2  # Multiplying the numbers

if num2 != 0:
    division = num1 / num2  # Division if num2 is not zero
else: 
    print("Undefined (division by zero)")  # Handling division by zero

# Displaying the results
print("\nResults:")
print(f"Addition: {addition}")  # Display sum
print(f"Subtraction: {subtraction}")  # Display difference
print(f"Multiplication: {multiplication}")  # Display product
print(f"Division: {division}")  # Display quotient


#%%
# Task 2: Temperature Converter
# The converts temperatures between Celsius and Fahrenheit.

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    F = celsius * 9/5 + 32  # Formula: F = C * 9/5 + 32
    return F

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    C = fahrenheit - 32 * 5/9  # Formula: C = F - 32 * 5/9
    return C

# Prompting the user to choose the type of conversion
print("Choose conversion type:")
print("1: Celsius to Fahrenheit")
print("2: Fahrenheit to Celsius")
choice = input("Enter your choice (1 or 2): ")

# Performing the selected conversion
if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))  # Input Celsius
    print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(celsius)}")  # Display Fahrenheit
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))  # Input Fahrenheit
    print(f"Temperature in Celsius: {fahrenheit_to_celsius(fahrenheit)}")  # Display Celsius
else:
    print("Invalid choice!")  # Handle invalid input

# %%

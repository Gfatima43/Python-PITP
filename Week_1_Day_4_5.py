# Week 01 Day-4 Practice

#%%
# Basic variable assignment and printing
name = 'Alice'
age = 25
favorite_food = 'Pizza'
print('Name:', name)
print('Age:', age)
print('Favorite Food:', favorite_food)

#%%
# Checking the type of a string variable
myname = 'Alice'

print(f"The type of the variable myname is {type(myname)}")

#%%
# Using single quotes inside double quotes
myname = "Alice's"

print(f"The type of the variable myname is {type(myname)}")

#%%
# Using double quotes inside single quotes
myname = 'Alice"s'

print(f"The type of the variable myname is {type(myname)}")

#%%
# Escape characters in strings
print("Alic\es")
print("Alic/es")

#%%
# String containing only digits
myname = "4567897676"

print(f"The type of the variable myname is {type(myname)}")

#%%
# Converting string to integer and checking type
myname = "457698089"

print(f"The type of the variable myname is {type(int(myname))}")

# %%
# Converting string to int and float, checking types
myname = "2341.86"
print(type(myname))
print(type(int(myname)))
print(type(float(myname)))

#%% 
# Taking user input and printing it
name = input('Enter your name: ')
age = input('Enter your age: ')
print('Hello ' + name + '! You are ' + age + ' years old.')

#%%
# Taking multiple inputs and calculating year of birth
name = input('Enter your full name: ')
age = int(input('Enter your age: '))
favorite_color = input('What is your favorite color? ')
current_year = int(input('Enter the current year: '))

year_of_birth = current_year - age

print(f'Hello, {name}!')
print(f'You were born in {year_of_birth}.')
print(f'Your favorite color is {favorite_color}.')

#%%
# Incorrect usage: 'string' function does not exist in Python
# No use string type
mynumber = 3.1416
print(type(string(mynumber)))
print(string(mynumber))

# %%
# Printing user input in different ways
myinput = input("Enter something:")

print("You entered the string:", myinput)
print(f"You enetered the string {myinput}")
print("printing your string", myinput,"print your string")
print(f"printing your string {myinput} ")
# %%
# Showing that input is always a string
myinput = input("Enter a number:")

print(f"You enter {myinput} and its datatype is {type(myinput)}")

#%%
# Week 01 Day-5 Practice
# Converting input to integer and showing type
myinput = input("Enter a number:")
myinput = int(myinput)

print(f"You enter {myinput} and its datatype is {type(myinput)}")

# %%
# Arithmetic Operators

myinput1 = input("Enter a number:")
myinput1 = int(myinput1)

myinput2 = input("Enter a number:")
myinput2 = int(myinput2)

print(f"The first number is {myinput1}")
print(f"The second number is {myinput2}")

print('Addition:', myinput1 + myinput2)
print('Subtraction:', myinput1 - myinput2)
print('Multiplication:', myinput1 * myinput2)
print('Division:', myinput1 / myinput2)
print('Modulus:', myinput1 % myinput2)
print('Exponentiation:', myinput1 ** myinput2)
print('Floor division:', myinput1 // myinput2)

# %%
# Comparison Operators

myinput1 = input("enter a number:")
myinput1 = int(myinput1)

myinput2 = input("Enter a number:")
myinput2 = int(myinput2)

print(f"The first number is {myinput1}")
print(f"The second number is {myinput2}")

print("Equal:", myinput1 == myinput2)
print("Not equal:", myinput1 != myinput2)
print("Greater than:", myinput1 > myinput2)
print("Less than:", myinput1 < myinput2)
print("Greater than or equal to:", myinput1 >= myinput2)
print("Less than or equal to:", myinput1 <= myinput2)

# %%
# Arithmetic and Comparison Operators

myinput1 = input("100")
myinput1 = int(myinput)
print(f"You entered {myinput} and its data type")

# %%

myinput1 = input("Enter first number:")
myinput1 = int(myinput1)
myinput2 = input("Enter second number:")
myinput2 = int(myinput2)
print(f"the first number is {myinput1} and the second number is {myinput2}")
print(f"the sum of the two numbers is {myinput1 + myinput2}")
print(f"the product of the two numbers is {myinput1 - myinput2}")
print(f"the multiplication of the two numbers is {myinput1 * myinput2}")
print(f"the division of the two numbers is {myinput1 / myinput2 }")
print(f"the sum of the two numbers is {myinput1 == myinput2 }")
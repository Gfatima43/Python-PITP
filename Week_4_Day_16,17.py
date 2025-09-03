#%%
# Week 04 Day-16
# Error Handling: Try to get integer input from user, handle non-integer input
try:
    mychar = int(input("Enter temperature:"))

    print(f"You entered {mychar}")

except ValueError:
    print("You didn't enter an integer.")

# %%
# Loop: Keep asking for temperature until user enters 0
mytemp = 1
while(mytemp != 0):

    mytemp = int(input("Enter temperature:"))

    print(f"You entered {mytemp}")

# %%
# Loop with Error Handling: Keep asking for integer temperature until user enters 0
mytemp = 1
while(mytemp != 0):
    try:
        mytemp = int(input("Enter temperature:"))

        print(f"You entered {mytemp}")

    except ValueError:
        print("You didn't enter an integer.")

#%%
# String Manipulation: Convert input string to upper or lower case based on user choice
mytext = input("Enter strng:")

text = input("Enter case to convert 'u' for upper & 'l' for lower ")

if(text == "u"):
    print(mytext.upper())
elif(text == "l"):
    print(mytext.lower())
else:
    print("Incorrect value")

#%%
# Week 04 Day-17
# Split string into words and join without spaces
string = "Hello   world!"
word = string.split()
print(word)
joined_string ="".join(word)
print(joined_string)

# %%
# Replace a word in string and join without spaces
string = "Hello world!"
word = string.replace("world", "Amna")
print(word)
joined_string ="".join(word)
print(joined_string)

# %%
# Remove leading and trailing spaces from string
string = "Hello     world!"
word = string.strip()
print(word)

# %%
# Remove all spaces from user input string
mystring = input("Enter a string with spaces")
print(f"The string without spaces is {mystring.replace(' ','')}")
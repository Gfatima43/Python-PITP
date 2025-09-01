#%%
# Week 03 Day-12
# while loop to find numbers <= 100 that are even and divisible by 5
sum = 0
i = 1
num_list = []
while sum <= 100:
    if(i % 2 == 0 and i % 5 == 0):
        sum = sum + i
        num_list.appened(i)  # Typo: should be 'append'
    i += 1
print(f" list of even number and divisible by 5 is {num_list}")

#%%
# while loop to find numbers <= 100 that are even and divisible by 5, but stops if i == 40
sum = 0
i = 1
num_list = []
while sum <= 100:
    if(i % 2 == 0 and i % 5 == 0):
        if(i == 40):
            break  # Stop loop when i reaches 40
        else:
            sum = sum + i
            num_list.appened(i)  # Typo: should be 'append'
    i += 1
print(f" list of is {num_list}")

#%%
# Week 03 Day-13
# Dictionary example: storing and accessing data
person = {
    'Name': "Sana",
    'Professtion': "Engineer",
    'Phone': 92345678,
    'Address': "Hyderabad"
    }

print(person) # store data
print(person['Phone']) # get value 

#%%
# Dictionary: updating values and adding new keys
person = {
    'Name': "Sana",
    'Professtion': "Engineer",
    'Phone': 92345678,
    'Address': "Hyderabad"
    }

person['Name'] = ['Ali','Rabia','Sami','Rafia'] # Update 'Name' key with a list
person['Age'] = 32 # Add new key 'Age'
person['Test'] = 1 # Add new key 'Test'
person.keys() # Get all keys in dictionary
print(person)

#%%
# Tuple example: creating and accessing elements
mytuple = (1,2,3,4,5)
print(mytuple)
mytuple[3] # Access element at index 3

#%%
# Tuple: checking type of variable
mytuple = (1,2,3,4,5)
print(type(mytuple)) # Print type of 'mytuple'

# %%
# List example: creating and multiplying lists
mylist1 = [1,2,3,4,5]
mylist2 = [1,2,3,4,5]*2 # Repeat list twice
print(mylist2)
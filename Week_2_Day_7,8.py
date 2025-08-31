# %%
# Week 02 Day-6
# For loop from 0 to 10, printing a message with the loop index

for i in range(0,11):
    print(f"Hello World! {i}")
#%%
# For loop showing modulus operation (even/odd check)
for i in range(0,11,):
    print(f"i%2 result in {i%2}")

# %%
# Week 02 Day-7
# For loop with two print statements, demonstrating loop and modulus

for i in range(0,11,):
 print(f"Hello World! {i}")
 print(f"i%2 result in {i%2}")

#%%
# For loop with indented print statements
for i in range(0,11,):
  print(f"Hello World! {i}")
  print(f"i%2 result in {i%2}")

#%%
# Demonstrates indentation error in Python
for i in range(0,11,):
  print(f"Hello World! {i}")
   print(f"i%2 result in {i%2}") # indentation error 
  
#%%
# For loop with print outside the loop (shows scope)
for i in range(0,11,):
 print(f"Hello World! {i}")
print(f"i%2 result in {i%2}")

#%%
# Simple variable assignment and modulus operation
i = 5
print(f"Hello World! {i}")
print(f"i%2 result in {i%2}")

# %%
# For loop with if-else to check even/odd
for i in range(0,11,):
    print(f"i%2 result in {i%2}")

    if(i % 2 == 0):
      print(f"{i} is even")
    else:
      print(f"{i} is odd")

print("Program execution has ended.")

#%%
# For loop with if-else and logical AND, checking if i > 5 and even
for i in range(0,11,):
    print(f"i>5 result in {i>5}")

    if(i > 5 and i % 2 == 0):
      print(f"{i} is even")
    else:
      print(f"{i} is odd")

print("Program execution has ended.")

#%%
# For loop with modulus 3 and conditional logic
for i in range(0,11,):
    print(f"i%3 result in {i%3}")

    if(i % 2 == 0):
      print(f"{i} is longer than 5 and divisble by 3")
    else:
      print(f"{i} is longer than 5 and not divisble by 3")

print("Program execution has ended.")

#%%
# For loop with multiple conditions (i > 5 and divisible by 3)
for i in range(0,11,):
    print(f"i%2 result in {i%2}")

    if(i > 5 and i % 3 == 0):
      print(f"{i} is less than 5")
    else:
      print(f"{i} is longer than 5")

print("Program execution has ended.")

#%%
# Week 02 Day-8
# For loop with logical OR, printing if i > 5 or divisible by 3
sum=0
for i in range(0,50):

  if(i > 5 or i % 3 == 0):
    print(f"{i} is greater than 5")
print("Program execution has ended.")

# %%
# For loop to sum odd numbers from 0 to 49
sum=0
for i in range(0,50):

  if(i % 2 == 1):
    sum=sum+i
print(f"The sum of odd numbers is {sum}")

#%%
# For loop to sum even numbers from 0 to 49
sum=0
for i in range(0,50):

  if(i % 2 == 0):
    sum=sum+i
print(f"The sum of odd numbers is {sum}")

#%%
# For loop to sum even numbers not divisible by 3
sum=0
for i in range(0,50):

  if(i % 2 == 0 and i % 3 != 0):
    sum=sum+i
print(f"The sum of odd numbers not division by 3 is {sum}")
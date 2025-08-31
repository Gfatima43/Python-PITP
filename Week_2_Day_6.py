# %%
# Week 02 Day-6
# Logical Operators

myinput1 = input("Enter first number:")
myinput1 = int(myinput1)
myinput2 = input("Enter second number:")
myinput2 = int(myinput2)
print(f"The result for testing(x>x & x%2==0) is {(myinput1 > myinput2) and (myinput1%2==0)}")

# %%
# Divided by 2
myinput1 = input("Enter first number:")
myinput1 = int(myinput1)
myinput2 = input("Enter second number:")
myinput2 = int(myinput2)

print(f"myinput1 is longer than myinput2 is {myinput1>myinput2}")
print(f"myinput1 is divisible by 2 is {myinput1%myinput2}")
print(f"The result for testing 'and' operator(x>x & x%2==0) is {(myinput1>myinput2 and (myinput1%2==0))}")
print(f"the result for testing 'or' operator(x>x or x%2==0) is {((myinput1>myinput2) or (myinput1%2==0))}")
print(f"The result for testing 'not' operator not(x>x & x%2==0) is {not((myinput1>myinput2) and (myinput1%2==0))}")

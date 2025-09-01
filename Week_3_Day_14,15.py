#%%
# Week 03 Day-14
# Create a list and repeat its elements
mylist1 = [1,2,3,4,5]
mylist2 = [1,2,3,4,5]*2
print(mylist2)

# Use numpy to multiply each element by 2 and convert back to list
import numpy as np  # import library
mylist3 = (np.array(mylist1)*2).tolist()
print(mylist3)

#%%
# Temperature conversion function: Celsius to Fahrenheit
def C_to_F(temp_C):
    temp_F = temp_C * 1.8 + 32
    return temp_F

# Get temperature input from user and convert to Fahrenheit
mytemp = float(input("Enter the temperature in Celsius: "))
print(f"{mytemp} in Fahrenhiet is {C_to_F(mytemp)}")

# %%
# Week 03 Day-15
# Temperature conversion function: Fahrenheit to Celsius (incorrect formula)
def F_to_C(temp_F):
    temp_C = temp_F - 32 * 0.5
    return temp_C

# Get temperature input from user and convert to Celsius
mytemp = float(input("Enter the temperature in Celsius: "))
print(f"{mytemp} in Fahrenhiet is {F_to_C(mytemp)}")

#%%
# Functions for temperature conversion both ways
def C_to_F(temp_C):
    temp_F = temp_C * 1.8 + 32
    return temp_F

def F_to_C(temp_F):
    temp_C = temp_F - 32 * 0.5
    return temp_C

# Get temperature and conversion choice from user
mytemp = float(input("Enter the temperature is: "))
mychar = input("Enter either F to C convert temperature.")

# Perform conversion based on user choice
if(mychar == "F"):
    F_to_C(mytemp)
elif(mychar == "C"):
    C_to_F(mytemp)
else:
    print("You have own choice.")

# Print both conversions for reference
print(f"{mytemp} in Celsius is {F_to_C(mytemp)}")
print(f"{mytemp} in Fahrenhiet is {C_to_F(mytemp)}")
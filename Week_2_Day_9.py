#%%
# Week 02 Day-9
sum=0
for i in [0,1,2,3,4,5,6,7,8,9,10]:
    if(i % 2 and i % 3 != 0):
        sum=sum+i
print(f"The sum is {sum}")

#%%
# List
mylist = [1,2,3,4,5,6]
print(mylist)

#%%
mylist = [1,2,3,4,5,6]
print(mylist[3])

#%%
mylist = [1,2,3,4,5,6]
mylist.append(7)
print(mylist)

#%%
mylist = [1,2,3,4,5,6]
mylist.pop()
print(mylist)

#%%
mylist = []
for i in range(0,50):
    if(i % 2 == 0):
        mylist.append(i)
print(f"The list of even numbers is {mylist}")

#%%
mylist = []
for i in range(0,50):
    if(i % 2 == 1):
        mylist.append(i)
print(f"The list of odd numbers is {mylist}")

#%%
mylist = []
myinput = int(input("Enter a number:"))

for i in range(0, myinput):
    if(i % 2 == 0):
        mylist.append(i)
print(f"The list of even numbers is {mylist}")

#%%
mylist = [1,2,3,4,5,6]
print(mylist*2) 

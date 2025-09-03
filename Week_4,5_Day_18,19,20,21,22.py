#%%
# Week 04 Day-18
# Calculate factorial using a while loop (basic version)
n = int(input())
factor = 1
while(n > 1):
    factor=factor*n
    n=n-1

print(f"Factorial is {factor}")

# %%
# Calculate factorial with input validation for negative and zero
n = int(input("Enter a number: "))
factor = 1
while(n >= 1):
    factor = factor * n
    n = n - 1
if(n < 0):
    print("Factorial not negative number.")
elif(n == 0):
    print("Factorial of 0 is 1")
else:
    print("No vaild")
print(f"Factorial is {factor}")

#%%
# Calculate factorial using a temporary variable
n = int(input("Enter a number to calculate factorial for : "))
temp = n
fact_product = 1

while(temp != 1):
    fact_product = fact_product * temp
    temp = temp - 1

print(f"The factorial {n} is {fact_product}")

#%%
# Filter names starting with 'A' or 'a' from a list
list1 = ['Ali', 'Apple', 'Amazon', 'Zubada', 'Muniba', 'Misbha', 'Abbas']
list2 = []

for x in range(len(list1)):
    if (list1[x].lower().startswith('a') or list1[x].startswith('A')):
        list2.append(list1[x])

print(list2)

#%%
# Find palindromic words in a list (case-insensitive)
frist = ['Ali', 'Apple','oppo', 'level', 'mom', 'madam',  'Amazon', 'Zubada', 'Muniba', 'Misbha', 'Abbas']
flist = []

for word in frist:
    if word.lower() == word[::-1].lower():
        flist.append(word)
print(flist)

#%%
# Week 04 Day-19 
# Practice Day
# Consider a list that has the numbers 3, 4,5,6,7,8,9, 12, 13, 15, 16 . 
# Write a program that checks which numbers are even, adds them to a list 
# called evenlist, for odd it creates a list called oddlist, for numbers 
# divisible by 3, it creates a list called threelist.


# List of numbers
num = [3, 4, 5, 6, 7, 8, 9, 12, 13, 15, 16]

evenlist = []
oddlist = []
threelist = []

for x in num:
    if num % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)
    if num % 3 == 0:
        threelist.append(x)

print(f"Even numbers:", evenlist)
print(f"Odd numbers:", oddlist)
print(f"Numbers divisible by 3:", threelist)

#%%
# Create a program that takes an input of a word. It then finds that word 
# in a sentence/paragraph and outputs the count for the time the word appears in it.

paragraph = input("Enter a sentence/paragraph: ")
word = input("Enter the word you want to count: ")

count = paragraph.count(word)

print(f"The word '{word}' appears {count} times in the given paragraph.")

#%%
# Week 04 Day-20
# Set behavior (removes duplicates)
mylist = {"a", "b", "b", "Bb", "c", "d", "c", "a", "a", "C"}

print(mylist)

# %%
# Traverse directories and files using os.walk
import os

# Travers all the branch of a specified path
for (root,dirs,files) in os.walk(r'c:\Users\DELL\Desktop\HTML Notes_2',topdown=True):
  print("Directory path: %s"%root)
  print("Directory Names: %s"%dirs)
  print("Files Names: %s"%files)

# %%
# Week 05 Day-21
# Classes OOP
# Define a simple Person class with name and phone attributes

class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

def display_content(self):
    print(f"Name is {self.name}")

#%%
# Attempt to print class attribute (incorrect usage)
class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

def display_content(self):
    print(f"Name is {self.name}")

Person1 = Person('Ali', 92315646)
print(Person.name)

#%%
# Create Person objects and call method (method not bound correctly)
class Person:
  def __init__(self, name, phone):
    self.name = name
    self.phone = phone

def display_content(self):
    print(f"Name is {self.name}")

Person1 = Person('Ali', 92315646)
print(Person1.name)
Person2 = Person('Aliba', 9231896546)
Person2.display_content()

#%%
# Employee class with address printing method
class employee:
    def __init__(self, name, age, street, city, country, phone, salary):
        self.name = name
        self.age = age
        self.street = street
        self.city = city
        self.country = country
        self.phone = phone
        self.salary = salary

    def print_address(self):
        print(f"{self.street}, {self.city}, {self.country}")

employee1 = employee("Jamal", 30, "123 Main St", "Karachi", "Pakistan", "123456789", 50000)
employee1.print_address()

#%%
# Employee class with yearly salary and tax calculation, Teacher subclass
class employee:
    def __init__(self, name, age, street, city, country, phone, salary):
        self.name = name
        self.age = age
        self.street = street
        self.city = city
        self.country = country
        self.phone = phone
        self.salary = salary

    def print_address(self):
        print(self.street + "," + self.city + "," + self.country)

    def yearly_salary(self):
        print(f"Yearly Salary: {self.salary * 12}")

    def tax_due(self):
        print(f"Tax Due: {self.salary * 0.1}")


class teacher(employee):
    def __init__(self, name, age, street, city, country, phone, salary, dept):
        super().__init__(name, age, street, city, country, phone, salary)
        self.dept = dept

    def display_teacher_info(self):
        print(f"Department is {self.dept}")


teacher1 = teacher("Jamal", 30, "123 Main St", "Hyderabad", "Pakistan", "123456789", 5000, "Mathematics")
teacher1.print_address()
teacher1.yearly_salary()
teacher1.tax_due()
teacher1.display_teacher_info()

#%%
# Demonstrate inheritance: Parent and Child classes
class ParentClass:
    def __init__(self,name):
        self.name = name

    def display_name(self):
        print(f"Name: {self.name}")

class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def display_age(self):
        print(f"Age: {self.age}")

child = ChildClass('Alice', 25)
child.display_name()
child.display_age()

# %%
# Week 05 Day-22
# Demonstrate method overriding in inheritance
class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def sound(self):
        print("The cat meows.")

# Creating objects and calling the overridden method
my_dog = Dog()
my_cat = Cat()

my_dog.sound()  
my_cat.sound()

# %%
# Demonstrate incorrect method overriding in Cat class
class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self):
        print("The dog barks.")

class Cat(Animal):
    def soundcat(self):
        print("The cat meows.")

# Creating objects and calling the overridden method
my_dog = Dog()
my_cat = Cat()

my_dog.sound()
my_cat.sound()

# %%
# Polymorphism example with Shape, Circle, Rectangle classes
class Shape:
    def area(self): 
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

# Polymorphism
shapes = [Circle(5), Rectangle(4,6)]

for shape in shapes:
    print(f'Area: {shape.area()}')

# %%
# Write a string to a file
file = open('example.txt','w')
file.write("Hello, World!")
file.close()

# %%
# Write "Hello, World!" 10 times to a file
file = open('example.txt','w')
for _ in range(10):
    file.write("Hello, World!\n")
file.close()

# %%
# Calculate area of a circle and write result to a file
import math

r = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(r, 2)

string = (f"Area of circle with radius {r} is: {area}\n")

file = open('circle_area.txt','w')
file.write(string)
file.close()

print(string)

# %%
# Calculate area of a circle, write result to a file using 'with' statement
import math

r = float(input("Enter the radius of the circle: "))

area = math.pi * math.pow(r, 2)

result = (f"The area of the circle with radius {r} is: {area}\n")

print(result)

with open("circle_area.txt", "w") as file:
    file.write(result)

print("Result 'circle_area.txt'.")

# %%
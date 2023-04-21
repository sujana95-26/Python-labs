# Selection_part1

import math


person = int(input("Enter Age: ")

if person >= 18:
    print("You are in category A")
if person >= 16 and person >18:
    print("You are in category B")
if person <= 16:
    print("You are in category C")
             
person = int(input("Enter Age:"))
             
if person >= 18:
    print("You are in category A")
elif person >= 16:
    print("you are in category B")
else:
    print("You are in category C")

# Calculator on separate file

# Task 2 - Calculate exam grades
# Exam grade

exam_mark = float(input("Please enter the mark (Between 1 and 100): "))
if exam_mark < 1 or exam_mark > 100
    print("Error: Please enter between 1 and 100")         
elif exam_mark <= 50.60:
    print("fail")
elif exam_mark <= 61.70:
    print("pass")
elif exam_mark <= 71.100:
    print("merit")
elif exam_mark <= 100:
    print("Distinction")
else:
    print("Distinction")

# Task 3
# Exam grade2

level = float(input("please enter your level(1 or 2): "))
marks = float(input("please enter your marks(Between 1 and 100): "))

if exam_mark < 1 or exam_mark > 100
    print("Error: Please enter between 1 and 100")
             
elif(level == 1):
    if ( marks <= 50.60):
        print("fail")
    elif ( marks <= 61.70):
        print("pass")
    elif ( marks >=71.100):
        print("Distinction")
    else:
        print("Distinction")

elif (level == 2):
    if (marks < 40):
        print("fail")
    elif ( marks <= 40.50):
        print(Pass)
    elif ( marks <= 51.65):
        print("merit")
    elif ( marks >= 66.100):
        print("Distinction")
    else:
        print("Distinction")
else:
    print("Error: choose level 1 or 2")

# Task 4
# Pythagoras

print("Pythagoras Calculator")
print("1. Find the length of A given B and C ")
print("2. Find the length of B given A and C ")
print("3. Find the length of C given A and B ")

result = int(input("Please enter 1, 2 or 3: "))

if result == 1:
    B = float(input( "Please enter value for B: "))
    C = float(input( "Please enter value for C: "))
    A = math.sqrt(B **2 - C**2) 
    print(f"Side A is equal to {A}.")

elif result == 2:
    A = float(input("Please enter value for A: "))
    C = float(input("Please enter value for C: "))
    B = math.sqrt(C**2 - A**2)
    print(f"Side B is equal to {B}.")

elif result == 3:
    A = float(input("Please enter value for A: "))
    B = float(input("Please enter value for B: "))
    C = math.sqrt( A ** 2 + B ** 2)
    print(f"Side C is equal to {C}.")
else:
    print("Error: Please choose 1, 2 or 3")
















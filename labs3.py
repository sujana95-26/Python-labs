# Task 1
# Squares

x = 1
while 0 < x <= 100:
    print(x)
    x += 1

while x<=100:
    square = x ** 2
    if square > 2000:
        break
    print(square)

# Task 2

num = int(input("Enter a number: "))

factorial = 1
while num > 1:
    factorial *= num
    num-=1

print("factorial is:", factorial)

#Task 3

initialinv = float(input("Initial investment: £ "))
targetinv = float(input("Target investment: £ "))
interestrate = float(input("Interest rate: %"))/100
years = 0
while initialinv < targetinv:
    initialinv *= (1+interestrate)
    years+=1
print (f"It takes {years} year(s)to grow to £{targetinv}.")

# Task 4
min = 1
max = 100

tries = 0

while tries < 3:
    guess = int(input(f"guess a value between {min} and {max}: "))
    if min<= guess >= max:
        print("correct!")
        break
    else:
        print("incorrect!")
        tries+=1
    
if tries ==3:
    print("none")

# Task 5

word = input("Please enter a word: ")
counter = 0
vowel_count = 0

while counter < len(word):
    x= word[counter]
    if x in "aeiou":
        vowel_count+=1
    counter +=1
print(f"the number of vowels in{word} is {vowel_count}")


#Task 6
math_mark = 191
english_mark = 191
ict_mark = 191

while (math_mark < 0 or math_mark >100):
    math_mark = int(input("enter math marks(0-100): "))
while (english_mark < 0 or english_mark >100):
    english_mark= int(input("enter english marks(0-100): "))
while (ict_mark <0 or ict_mark>100):
    ict_mark = int(input("enter ict marks: "))

average = (math_mark +english_mark + ict_mark)/3

if average > 65:
    result ="pass"
else:
    result = "fail"

print(f"the average mark is {average}, {result} ")

    










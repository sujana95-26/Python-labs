ages = [12, 2 ,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,
        11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,
        72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
length = len(ages)
print(length)

for item in ages:
    print(item)

new_age = [x + 1 for x in ages]
print(new_age)
for item in new_age:
    print(item)
print("The length is", len(new_age))
#for i in range(len(ages)):
    #ages[i] += 1

range = [i for i in new_age if 16<= i <= 65]
range.sort()
print(range)

count = 0 
for i in new_age:
    if i >= 16 and i <=25:
        count += 1
print(f"there are {count} 16-65 year olds.")

    

# Part 2
# Count vowels

word = input("Please enter word: ")
vowels = "aeiou"
counter = 0
for x in word:
    if x in vowels:
        counter+=1

print(f"There are {counter} vowels in {word}")

#Task 2
#Time calculator

while True:
    print("Time Calculator")
    print("1 - Add 2 times")
    print("2 - Find the difference betweeen 2 times")
    print("3 - Convert datetime to hours")
    print("4 - Convert datetime to minutes")
    print("5 - Convert Minutes to date time")
    print("6 - convert Hours to date time")
    print("7 - Convert Days to date time")
    print("8 - Exit")

    choice = (input("Please choose an option(1-8): "))

    if choice == "1":
        value1 = (input("Please enter first value in DD.HH.MM"))
        value2 = (input("Please enter second value in DD.HH.MM"))
        result = value1 + value2
        print("The time is ",result)
    elif choice == "2":
        value1 = (input("Please enter first value in DD.HH.MM"))
        value2 = (input("Please enter first value in DD.HH.MM"))
        result = value1 - value2
        print("The time is", result)
    elif choice == "3":
        value1 = (input("Please enter time value: "))
        answer = value1 / 60
        print(f"it is {value1} hour(s).")
    elif choice == "4":
        value1 = float(input("please enter time value: "))
        answer = value1 *60
        print(answer)
    elif choice == "5":
        value1 = (input("Please enter minutes"))
        answer = value1 * 60
        print(answer)
    elif choice == "6":
        value1 = (input("Please enter hours"))
        answer = value1 / 60
    elif choice == "7":
        value1 = (input("Please enter days"))
        answer = value1 * 24
    elif choice == "8":
        break
    else:
        break



    







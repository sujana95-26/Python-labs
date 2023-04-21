# Weight-converter app, convert a user inputted weight (float) and user to select
#either kgs or lbs from a prompt. write an if statement that checks if the unit entered  is kg or lbs
# if kgs convert to lbs and print converted weight
# else if lbs convert kg
# error handling for upper/lowercase

weight = float(input("enter your weight: "))
unit = input("convert to kgs or lbs? ")

if unit in ("lbs", "lb", "pound", "pounds"):
    weight = weight * 2.2 
    print(f"your weight is {weight} in lbs.")

elif unit in ("kg", "kgs", "kilo", "kilograms"):
    weight = weight /2.2
    print(f"your weight is {weight} in kgs")
else:
    print("incorrect format, try again")

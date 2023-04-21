# exercise - ask for an unput from user for a grade/mark
# if the mark is greatere than 85 print distinction
#if between 65 and 85 print pass
#anything else print fail
# if + elifs

Grade = int(input("Enter your grade: "))

if Grade > 85:
    print("distiction")
elif Grade >= 65:
    print("pass")
else:
    print("fail")
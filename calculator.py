num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

print(" Menu")
print("1. Add        +")
print("2. Subtract   -")
print("3. Multiply   x")
print("4. Divide     /")
print("5. Square     s")

choice = (input("please anter function: "))
                
if choice == "+": 
    answer = num1 + num2
    print(f"answer is {answer}.")
if choice == "-":
    answer = num1 - num2
    print(f"answer is {answer}.")
if choice == "x":
    answer = num1 * num2
    print(f"the answer is {answer}.")
if choice == "/":
    answer = num1 / num2
    print(f"the answer is {answer}.")
if choice == "s":
    answer = num1 ** num2
    print(f"answer is {answer}.")
    




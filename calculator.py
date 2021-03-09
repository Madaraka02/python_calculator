def add(num1,num2):
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    return num1 / num2

print("select operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = input("enter choice(1/2/3/4) ")

num1 = int(input("enter first number "))
num2 = int(input("enter second number "))

if choice == '1':
    print(add(num1, num2))
elif choice == '2':
    print(subtract(num1, num2))
elif choice == '3':
    print (multiply(num1, num2))
elif choice == '4':
    print(divide(num1, num2))
else:
    print("invalid choice")
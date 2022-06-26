def min(a, b, c):
    if a < b and a < c:
        print(a, " is lesser among them")
    elif b < a and b < c:
        print(b, " is lesser among them")
    elif a == b or b == c or a == b == c:
        print("numbers are equal")
    else:
        print(c, " is lesser among them")


num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
num3 = int(input("Enter number3 "))

min(num1, num2, num3)

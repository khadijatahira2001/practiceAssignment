def max(a, b, c):
        if a > b and a > c:
            print(a, " is greater between them")
        elif b > a and b > c:
            print(b, " is greater between them")
        elif a == b or b == c:
            print("numbers are equal")
        else:
            print(c, " is greater between them")


num1 = int(input("Enter number1 "))
num2 = int(input("Enter number2 "))
num3 = int(input("Enter number3 "))

max(num1, num2, num3)


num = int(input("Enter a number "))
a = int(0)
b = int(1)
next = a+b
print("Fibonacci series")
print(a)
print(b)
def Fibonacci(num):
    a = int(0)
    b = int(1)
    next = a+b
    i = 3
    for i in range(i, num+1):
        print(next)
        a = b
        b = next
        next = a + b
Fibonacci(num)

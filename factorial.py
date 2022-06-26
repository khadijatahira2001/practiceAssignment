def factorial(n):
    i = 1
    fac = 1
    for i in range(i, n+1):
        fac = fac*i

    print("factorial of ", n, "is ", fac)


num = int(input("Enter a number "))


factorial(num)
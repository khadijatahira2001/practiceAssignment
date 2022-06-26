def check_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            print("number is not prime")
            break
    else:
        print("number is prime")


num = int(input("Enter a positive number "))

check_prime(num)

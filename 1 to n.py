#recursive questions to print counting 1 to n

def recursive(n):
    if n > 0:
        # recursive function call
        recursive(n - 1)
        print(n)


# input limit of counting


number = int(input("Enter a number "))

#function call
recursive(number)
#recursive questions to print counting 1 to n

def recursive(n):
    if n > 0:
        print(n)
        # recursive function call
        recursive(n - 1)


# input limit of counting


number = int(input("Enter a number "))

#function call
recursive(number)
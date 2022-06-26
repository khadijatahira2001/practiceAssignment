def vote(a):
    if a >= 18:
        print("you are eligible to vote ")
    else:
        print("you are younger, not eligible to vote ")


year = int(input("enter your year of birth "))
i = year
b = 0
while i < 2022:
  i += 1
  b += 1

year = b
vote(year)

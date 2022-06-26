def grade(g):
    if g > 90 and g <=100 :
        print("you got AA Grade")
    elif g > 80 and g <=90 :
        print("you got AB Grade")
    elif g > 70 and g <=80 :
        print("you got BB Grade")
    elif g > 60 and g <=70 :
        print("you got BC Grade")
    elif g > 50 and g <=60 :
        print("you got CD Grade")
    elif g > 40 and g <=50 :
        print("you got DD Grade")
    elif g <= 40:
        print("You are fail, try your best for next time")
    else:
        print("invalid number")


marks = int(input("Enter a your marks "))

grade(marks)

import math
def circum(radius):
    pi = math.pi
    circumference = 2 * pi*radius**2
    print("Circumference of a circle = ",  circumference)


radius = float(input("Enter radius of a circle "))

circum(radius)

import math

def Area(rad):
    pi = math.pi
    area = pi*rad**2
    print("Area of a circle = ", area)


radius = input("Enter radius of a circle ")
rad = float(radius)

Area(rad)

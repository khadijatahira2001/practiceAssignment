import math

def volume(rad,height):
    pi = math.pi
    volume = pi*rad**2*height
    print("volume of a cylinder = ", volume)


radius = input("Enter radius ")
rad = float(radius)
h = input("Enter height ")
height = float(h)


volume(rad, height)
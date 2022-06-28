import math

def volume(rad):
    pi = math.pi
    volume = 4/3*pi*rad**3
    print("volume of a sphere = ", volume)


radius = input("Enter radius for sphere ")
rad = float(radius)

volume(rad)
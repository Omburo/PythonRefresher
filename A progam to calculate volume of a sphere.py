# A progam to calculate volume of a sphere
import math
# Ask user to input radius of a given sphere
radius = float(input("Enter radius of sphere: "))
pi = math.pi 
volume = (4/3) * pi * (radius ** 3)

print ("The volume of the sphere = ", volume)
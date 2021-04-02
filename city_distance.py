# Assignment 3:
# Write a python class that is able to return the flight distance between two cities given their
# latitude and longitude coordinates.

from math import sin, cos, sqrt, atan2, radians

# approximate radius of earth in km
R = 6371.01

city1_let, city1_long  = input("City 1: ").split(',')
city1_let  = radians(float(city1_let[:-1]))
city1_long = radians(float(city1_long[:-1]))

city2_let, city2_long  = input("City 2: ").split(',')
city2_let  = radians(float(city2_let[:-1]))
city2_long = radians(float(city2_long[:-1]))

result1 = city2_long - city1_long
result2 = city2_let - city1_let

f1 = sin(result2 / 2)**2 + cos(city1_let) * cos(city2_let) * sin(result1 / 2)**2
f2 = 2 * atan2(sqrt(f1), sqrt(1 - f1))

distance = R * f2

distance = "{:.2f}".format(distance)

print(f"City 1 and City 2 are {distance} km apart")

# > City 1: 51.5074 N, 0.1278 W
# > City 2: 48.8566 N, 2.3522 E

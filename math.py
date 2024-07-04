import math
def degrees_to_radians(degrees):
    radians = degrees * (math.pi / 180)
    return radians
degrees = int(input())
radians = degrees_to_radians(degrees)
print(radians) 


def trapezoid_area(height, base1, base2):
    return 0.5 * (base1 + base2) * height
height = int(input())
base1 = int(input())
base2 = int(input())
area = trapezoid_area(height, base1, base2)
print(area) 


import math
def polygon_area(num_sides, side_length):
    area = (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))
    return area
num_sides = int(input())
side_length = int(input())
area = polygon_area(num_sides, side_length)
print(area)  


def parallelogram_area(base, height):
    return base * height
base = int(input())
height = int(input())
area = parallelogram_area(base, height)
print(area) 

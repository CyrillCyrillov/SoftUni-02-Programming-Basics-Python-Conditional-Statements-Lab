import math
type_of_fugure = input()
if (type_of_fugure == "square"):
    side = float(input())
    print(f"{side * side:.3f}")
elif (type_of_fugure == "rectangle"):
    side_one = float(input())
    side_two = float(input())
    print(f"{side_one * side_two:.3f}")
elif (type_of_fugure == "circle"):
    radius = float(input())
    print(f"{math.pi * radius * radius:.3f}")
elif (type_of_fugure == "triangle"):
    side = float(input())
    high = float(input())
    print(f"{side * high / 2:.3f}")

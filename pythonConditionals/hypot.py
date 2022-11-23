def find_hypot(a, b):
    hypot = a ** 2 + b ** 2
    hypot = hypot ** 0.5
    print("hypotenuse is ", hypot)
    return hypot


response = input("Write length of the first side of the triangle....")
a1 = int(response)
response = input("Write length of the second side of the triangle....")
b1 = int(response)

find_hypot(a1,b1)

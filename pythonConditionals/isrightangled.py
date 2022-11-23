def find_hypot(a, b):
    hypot = a ** 2 + b ** 2
    hypot = hypot ** 0.5
    #print("hypotenuse is ", hypot)
    return hypot


def is_rightangled(a, b, c):
    h = find_hypot(a, b)
    if abs(c - h) < 0.0000001:
        return True
    else:
        return False


response = input("Write length of the first side of the triangle....")
a1 = int(response)
response = input("Write length of the second side of the triangle....")
b1 = int(response)
response = input("Write length of the third side of the triangle....")
c1 = int(response)

max_val = c1
if c1 < a1:
    max_val = a1
    a1=c1
    c1=max_val
if c1 < b1:
    max_val = b1
    b1=c1
    c1=max_val
else: pass


print(is_rightangled(a1,b1,c1))

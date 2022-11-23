def rectangle(sides):
    area = sides[0] * sides[1]
    circumference = sides[0] * 2 + sides[1] * 2
    return area, circumference


boki = (4, 5)
print(rectangle(boki))


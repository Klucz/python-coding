def circle_area(r):
    area = 0
    if r >= 0:
        area = 3.14*r**2
    else:
        print("Number can't be negative")
    print(area)
    return area


circle_area(10)
#response=input("Please type number to sum up to....")
#sum_to(int(response))
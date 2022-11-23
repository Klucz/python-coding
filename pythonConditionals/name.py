# response = input("Write a number from 0 to 6 to get a day name...")
# x = int(response)
def day_name(x):
    if x < 0 or x > 6:
        print("Wrong number")
    elif x == 0:
        print("Day is Sunday")
    elif x == 1:
        print("Day is Monday")
    elif x == 2:
        print("Day is Tuesday")
    elif x == 3:
        print("Day is Wednesday")
    elif x == 4:
        print("Day is Thursday")
    elif x == 5:
        print("Day is Friday")
    elif x == 6:
        print("Day is Saturday")

response = input("Write a starting day number...")
d = int(response)
day_name(d)
response = input("Write a number of days")
n = int(response)
n = n % 7

if (n + d) > 6:
    n = n+d
    n = n % 7
else:
    n = n + d

day_name(n)

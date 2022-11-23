def sum_to(n):
    suma = 0
    if n >= 0:
        for i in range(n + 1):
            suma = suma + i
    else:
        print("Number can't be negative")
    print(suma)
    return suma


sum_to(10)
#response=input("Please type number to sum up to....")
#sum_to(int(response))
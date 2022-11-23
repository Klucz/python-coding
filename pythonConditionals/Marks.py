xs = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]

for i in xs:
    if i>=75:
      print(i, " grade = First")
    elif 75 > i >= 70:
        print(i, "grade = Upper Second")
    elif 70 > i >= 60:
        print(i,"grade = Second")
    elif 60 > i >= 50:
        print(i,"grade = Third")
    elif 50 > i >= 45:
        print(i,"grade = F1 Supp")
    elif 45 > i >= 40:
        print(i,"grade = F2")
    elif 45 > i >= 0:
        print(i,"grade = F3")
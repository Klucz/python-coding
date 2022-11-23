vocabulary = ["apple", "cheese", "dog"]
numbers = [17, 123]
an_empty_list = []
print(vocabulary, numbers, an_empty_list)
print(numbers[0])

horsemen = ["war", "famine", "pestilence", "death"]

for h in horsemen:
    print(h)


students = [
    ("John", ["CompSci", "Physics"]),
    ("Vusi", ["Maths", "CompSci", "Stats"]),
    ("Jess", ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Zuki", ["Sociology", "Economics", "Law", "Stats", "Music"])]

# Count how many students are taking CompSci
counter = 0
for (name, subjects) in students:
    if "CompSci" in subjects:
           counter += 1

print("The number of students taking CompSci is", counter)
import csv

with open("../csv/employees.csv", newline = '') as file:
    reader = list(csv.reader(file))

data = reader[1:]
names = []

for row in data:
    names.append(row[1] + " " + row[2])

print("Names: ", names)
e = []

for name in names:
    if 'e' in name.lower():
        e.append(name)

print("Names with the letter 'e': ", e)

import csv
import traceback
import os 
import custom_module 
from datetime import datetime

#Task 2
def read_employees():
    values = {}
    rows = []
    try:
        with open("../csv/employees.csv", 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                values["fields"] = row
                break
            for row in reader:
                rows.append(row)
        values["rows"] = rows
        return values 
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
employees = read_employees()
print(employees)

#Task 3
def column_index(string):
    return employees["fields"].index(string)
employee_id_column = column_index("employee_id")

#Task 4
def first_name(number):
    firstName = column_index("first_name")
    row = employees["rows"][number]
    return row[firstName]

#Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

#Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"])) 
    return matches 

#Task 7
def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]

print(sort_by_last_name())

#Task 8
def employee_dict(row):
    keys = employees["fields"][1:]
    values = row[1:]
    return dict(zip(keys, values))

print(employee_dict(employees["rows"][1]))

#Task 9
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        id = row[employee_id_column]
        result[id] = employee_dict(row)
    return result

print(all_employees_dict())

#Task 10
def get_this_value():
    return os.getenv("THISVALUE")

#Task 11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("Hello")
print(custom_module.secret)

#Task 12
def createDict(csvfile):
    with open(csvfile, "r") as file:
        reader = csv.reader(file)
        fields = next(reader)
        rows = [tuple(row) for row in reader]
    return {"fields": fields, "rows": rows}

def read_minutes(): 
    return createDict("../csv/minutes1.csv"), createDict("../csv/minutes2.csv")

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13
def create_minutes_set():
    first = set(minutes1["rows"])
    second = set(minutes2["rows"])
    return first.union(second)

minutes_set = create_minutes_set()
print(minutes_set)

#Task 14
def create_minutes_list():
    minutes = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes))

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda x: x[1])
    convert = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    with open("./minutes.csv", "w", newline="") as file:
        write = csv.writer(file)
        write.writerow(minutes1["fields"])
        write.writerows(convert)
    return convert
print(write_sorted_list())
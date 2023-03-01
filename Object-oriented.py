# 2. Bölüm Makine Öğrenimi Dersi Kodları

'''class Employee():
    employee_name = "Ben"
    department = "sales"
    starting_year = 2020
    salary = 5000

myObject = Employee()

print(myObject.employee_name)
print(myObject.department)
print(myObject.starting_year)
print(myObject.salary)
'''

class Employee():
    def __init__(self,employee_name,department,starting_year,salary):
        self.employee_name = employee_name
        self.department = department
        self.starting_year = starting_year
        self.salary = salary

employee_1 = Employee("Ben","sales",2020,5000)

print(employee_1.employee_name)
print(employee_1.department)
print(employee_1.starting_year)
print(employee_1.salary)
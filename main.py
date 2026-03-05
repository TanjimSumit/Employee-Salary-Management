employees = []

while True:
    print("1.Add 2.View 3.Total 4.Exit")
    ch = input("Choice: ")
    if ch == '1':
        name = input("Name: ")
        salary = float(input("Salary: "))
        employees.append((name, salary))
    elif ch == '2':
        print(employees)
    elif ch == '3':
        print("Total Payroll:", sum(emp[1] for emp in employees))
    elif ch == '4':
        break

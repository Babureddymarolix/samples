def add_employee():
    employee = {
        'Domain': input("Enter the employee's domain: "),
        'Name': input("Enter the employee's name: "),
        'EmpID': input("Enter the employee's empid: "),
        'Email': input("Enter the employee's email: ")
    }
    return employee

def print_employee_details(employee):
    print("\nEmployee Details:")
    for key, value in employee.items():
        print(f"{key}: {value}")

n = int(input("Enter the number of employees: "))
employee_details_list = []

for _ in range(n):
    employee = add_employee()
    employee_details_list.append(employee)

for i, employee in enumerate(employee_details_list, start=1):
    print(f"Employee {i}:")
    print_employee_details(employee)
def employee_details():
    employee_dict = {}
    employ_entry = int(input("Enter the number of employees: "))
    
    for i in range(employ_entry):
        emp_name = input("Enter employee name: ")
        emp_domain = input("Enter domain: ")
        
        if emp_domain in employee_dict:
            employee_dict[emp_domain].append(emp_name)
        else:
            employee_dict[emp_domain] = [emp_name]
    
    print("Employee details:")
    print("*****************")
    for domain, names in employee_dict.items():
        print("Domain:", domain)
        print("Employee Names:", ", ".capitalize join(names))

employee_details()
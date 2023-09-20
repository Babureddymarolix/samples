def employee_details():
    d = {}
    employ_entry = int(input("Enter the number of employes: "))
    for i in range(employ_entry):
        emp_age = input("Enter employee age: ")
        emp_domain = input("Enter domain: ")
    if emp_domain in d:
        d[emp_domain].append[emp_age]
    else:
      d[emp_domain]=emp_age
    print("Employee details:")
    
    for domain, name in d.items():
        print("Domain:", domain)
        print("Employee Names:", emp_age)
employee_details()
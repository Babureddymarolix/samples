print('two numbers below:')
a=int(input('enter first number:'))
b=int(input('enter second number:'))
chr==0
while chr<4:
    print('calculator menu')
    print('1.add')
    print('2.substact')
    print('3.multiply')
    print('4.divide')
    chr==int(input('enter ur choice:'))
    if chr==1:
        c=a+b
        print('sum:',c)
    elif chr==2:
      c=a-b
      print('difference:',c)
    elif chr==3:
        c=a*b
        print('product:',c)
    elif chr==4:
         c=a/b
         print('quoient:',c)
    else:
        print('invalid choice')

      
       



def add_employee():
    emp_details = {}
    emp_details["Name"] = input("Enter employee name: ")
    emp_details["EmpID"] = input("Enter employee ID: ")
    emp_details["Designation"] = input("Enter employee designation: ")
    emp_details["Email"] = input("Enter employee email: ")
    employee_list.append(emp_details)
def filter_employee():
    filter_criteria = input("Enter filter criteria (Name/EmpID/Designation/Email): ").capitalize()
    filter_value = input(f"Enter {filter_criteria} to filter by: ")
    
    filtered_employees = [emp for emp in employee_list if emp.get(filter_criteria) == filter_value]
    
    if len(filtered_employees) == 0:
        print("No employees found with the specified criteria.")
    else:
        print("Filtered Employee Details:")
        for emp in filtered_employees:
            print("Name:", emp["Name"])
            print("EmpID:", emp["EmpID"])
            print("Designation:", emp["Designation"])
            print("Email:", emp["Email"])
            print("-----------------------------")

def get_patient_details():
    patient_details = {}  
    
    patient_details['name'] = input("Enter patient's name: ")
    patient_details['age'] = input("Enter patient's age: ")
    patient_details['gender'] = input("Enter patient's gender: ")
    patient_details['address'] = input("Enter patient's address: ")
    patient_details['phone'] = input("Enter patient's phone number: ")

    return  patient_details


def display_patient_details(patients):
    if not patients:
        print("No patient details to display.")
    else:
        print("Patient Details:")
        for i, patient in enumerate(patients, start=1):
            print(f"Patient {i}:")
            print(f"Name: {patient['name']}")
            print(f"Age: {patient['age']}")
            print(f"Gender: {patient['gender']}")
            print(f"Address: {patient['address']}")
            print(f"Phone: {patient['phone']}")
            print() 



patient1 = {'id': 1, 'name': 'John', 'age': 30, 'gender': 'Male', 'address': '123 Main St', 'phone': '555-1234'}
patient2 = {'id': 2, 'name': 'Alice', 'age': 25, 'gender': 'Female', 'address': '456 Elm St', 'phone': '555-5678'}
patient3 = {'id': 3, 'name': 'Bob', 'age': 40, 'gender': 'Male', 'address': '789 Oak St', 'phone': '555-9012'}

patient_list = [patient1, patient2, patient3]

search_id = 2  
found_patient = search_patient_by_id(patient_list, search_id)

if found_patient:
    print("Patient found:")
    print(f"Name: {found_patient['name']}")
    print(f"Age: {found_patient['age']}")
 
else:
    print(f"No patient found with ID {search_id}")
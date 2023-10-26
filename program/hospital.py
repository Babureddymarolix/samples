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
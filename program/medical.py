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
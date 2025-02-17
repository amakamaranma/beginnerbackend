from time import sleep

student_profile = []

def accept_input_dict():
    name = input("Enter the student name: ")
    age = int(input("Enter the student age: "))
    while age <= 0:
        age = int(input("Enter the student age. Age should be greater than 0: "))
    gender = input("Enter the student gender: ")
    while gender.lower() not in ["male", "female"]:
        gender = input("Enter the student gender. Gender should be male or female: ")
    qualification = input("Enter the student qualification: ")

    return {
        "name": name,
        "age": age,
        "gender": gender,
        "qualification": qualification
    }
    
def main():
    cont = True
    while cont:
        student_info = accept_input_dict()
        student_profile.append(student_info)
        sleep(2)
        response = input("Do you want to add another student profile? (y/n): ").lower()
        while response not in ["y", "n"]:
            response = input("Do you want to add another student profile? (y/n).Answer must be 'y' or 'n': ").lower()
        cont = response == "y"
        

    main()
    print(student_profile)
    sleep(1)
    print("Goodbye..")
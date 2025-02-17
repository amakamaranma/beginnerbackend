student_profile = []

def collect_data():
    name = input("enter the student name: ")
    age = input("enter the student age: ")
    gender = input("enter the student gender: ")
    qualification = input("enter the student qualification: ")
    
    student_info = {
        "name": name,
        "age": age,
        "gender": gender,
        "qualification": qualification  
    }
    
    student_profile.append(student_info)
    
def main():
    run = True
    while run:
        collect_data()
        response = input("would you like to add more student info? (y/n)").lower()
        run = response == "y"
        
main()
print(student_profile)


        
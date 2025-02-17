# accept information dynamically from the console
# take student information like name, age, gender, and qualification 
# store it in a  student info dictionary
# append the student info dictionary to a students' profile list

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
        response = ("would like to add more student info? (y/n)")
        run = response == "would like to add more student info? (y/n)"
        

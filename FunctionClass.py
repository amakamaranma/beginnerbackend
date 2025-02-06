# function with no parameter
print("FUNCTIONS\n")
def Ada():
    name = input()
    return name

#ada = Ada()
#print("her name is ", ada)

#peter = Ada()
#print("his name is ", peter)

#ginika = Ada()
#print("her name is ", ginika)

#Function with parameter

def AdaSecond(name):
    couple = "Mr and Mrs " + name
    return couple

#first_couple = AdaSecond("Nwakaibeya")
#second_couple = AdaSecond("Okonkwo")
#third_couple = AdaSecond("Nwakaibeya Okonkwo")

#print(first_couple)
#print(second_couple)
#print(third_couple)

#Function with no return

husband = "Joshua"

def Printsomething(Ada):
    couple = "Mr. and Mrs. " + husband + " " + Ada
    print(couple)
    
#Printsomething("Ada")
#Printsomething("Amaka")
#Printsomething(husband)

# Functions with Varags with multiple returns

def Varags(first_number, *group_numbers):
    mean = sum(group_numbers)/len(group_numbers)
    return first_number, mean, group_numbers

#result2 = Varags(56,78,43,60)
#first, mean, group = result2

#print(first)
#print(mean)
#print(group)

# Function with default argument

def MyName(myname=None):
    if myname is None:
        print("Unkown person")
    else:
        print(myname)

MyName()
MyName("Ada")

#Positional Parameter

def Person(name, age, gender, qualification, status):
    biograph = f""" 
             my name is {name}, i am {age} years old, 
             i am a {gender}, i have {qualification} in computer science. 
             online status:{status}
    """
    print(biograph)
    
Person("ada", 21, "female", "b.sc", True)

#Variable Length Arguement; Positional

def Add(*b):
    result = 0
    print(type(b))
    for i in b:
        print(i)
        result = result + i
        print(result)
        
    
Add(1, 2, 3, 4)

#Arbitrary Keyword Argument

def Fn(**a):
    #for i in a. items():
     print(a )
    #pri vcx r4ewa`nt(i)
        
Fn(name="james", age=23, gender="male")


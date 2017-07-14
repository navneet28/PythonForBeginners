from statistics import mean as avg  
gradeDict={"Dorothy":[98,88,82,78],"Sarah":[87,86,91]}
admins= {"admin":"admin@123","user":"user123"}
def enterGrades():
    
    name=input("Student Name: ")
    grade=input("Grade: ")
    if name in gradeDict:
        print("Adding Grade...")
        gradeDict[name].append(float(grade))
    else:
        print("Student does not exist")
    print(gradeDict)
        
def removeStudent():
    name=input("What student do you want to remove? ")
    if name in gradeDict:
        print("Removing student...")
        del gradeDict[name]
    print(gradeDict)
    
def studentsAvg():
    for i in gradeDict:
        avgGrade=avg(gradeDict[i])
        print(i,"has an average grade of ",avgGrade)
        
def main():
    print("""
        Welcome to grade central!
        [1] - Enter Grades
        [2] - Remove Student
        [3] - Student Average Grades
        [4] - Exit
        """)
    x=input("What would you like to do today?: ")
    if x=='1':
        enterGrades()
    elif x=='2':
        removeStudent()
    elif x=='3':
        studentsAvg()
    else:
        if x!='4':
            print("Invalid Choice")
        print("Exiting the program...")
        exit()
username=input("Enter username: ")
password=input("Enter password: ")

if username in admins:
    if admins[username]==password:
        print("Welcome, "+username)
        while True:
            main()
    else:
        print("Invalid password")
else:
    print("Invalid username")

student = {
    "id" : 101,
    "name": "Aanaa" ,
    "age" : 23 ,
    "department": "SWE",
    "course" : {
        'python': 49 ,
        'maths': 78,
        'dsa' : 99,
        'logic' : 100
    } 
}
students = []
students.append(student)

def add_student():
    student_id = int(input("Enter Student ID: "))
    name = input("name: ")
    age = int(input("age: "))
    department = input("department: ")

    course = {}
    number_of_courses = int(input("How many courses? "))

    for i in range(number_of_courses):
         course_name = input("Enter course name: ")
         grade = float(input("Enter grade: "))

         course[course_name] = grade

    # get course and grade

    student = {
        "id" : student_id ,
        "name" : name ,
        "age" : age ,
        "department" : department,
        "courses" : course
        }
    students.append(student)

def view_student():
    student_id = int(input("Enter Student Id: "))
    for student in students :
        if student["id"] == student_id :

             print("Student Name: ", student["name"])
             print("Student ID: ",   student["id"])
             print("Student Age: ",  student["age"])
             print("Student Dep: ",  student["department"])

             average = calculate_average(student)
             result = check_pass_fail(student)

             print("Average:", average)
             print("Result:", result)

             return
         
    print("Student Not found")

def calculate_average(student):
    grades = student["courses"].values()
    total = sum(grades)
    number_of_courses = len(grades)
    return total / number_of_courses

def check_pass_fail(student):
    average = calculate_average(student)
    if average >= 50 :
        return "PASS"
    else :
        return "FAIL"

def search_student():
    student_id = int(input("Enter Student ID: "))
    for student in students :
        if student["id"] == student_id :
             print("Student Name:", student["name"])
             print("Student ID:", student["id"])
             print("Student Age:", student["age"])
             print("Student Department:", student["department"])
             return
    print("Student Not found")


def update_student():
    student_id = int(input("Enter a student id"))
    for student in students:
        if student["id"] == student_id :
            print("1, id")
            print("2, name")
            print("3, age")
            print("4, department")

            choice = input("Choose: ")

            if choice == "1" :
                student["id"] = int(input("New id: "))
            elif choice == "2" :
                student["name"] = input(("New Name: "))
            elif choice == "3" :
                student["age"] = int(input("New Age: "))
            elif choice == "4" :
                student["department"] = input("New Department")

            return
    print("Student not found")

while True :
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")

    choice = input("Choose : ")

    if choice == "1" :
        add_student()
    elif choice == "2" :
        view_student()
    elif choice == "3" :
        search_student()
    elif choice == "4" :
        update_student()
    elif choice == "5" :
        break
    else:
        print("Invalid choice")
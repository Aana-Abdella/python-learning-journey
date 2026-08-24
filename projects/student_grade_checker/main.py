student ={
    "StudentId": "UGPR1014",
    "name" : "Aana Abdella",
    "age" : 22 ,
    'department' : 'software',
    "maths_score": 98 ,
    'python_score' : 78 ,
    'java_score' : 69 ,
    'english' : 88,
    'skills' : {"Java", "Python" ,"Linux" , "Github", "Git"}

}
print("Student :", student['name'])
print("department :", student['department'])

if student["age"] >= 18 and student["age"] <= 25 :
    print("Academic Stutus : Eligable ")
else:
    print("Academic Stutus: Not eligable")

Total = student["python_score"] + student["java_score"] + student["maths_score"] + student["english"]
Average = Total/4

if Average >= 90 :
    print("Performance Exelent")
elif Average >= 80:
    print("Performance Very Good")
elif Average >= 70:
    print("Performance Good")
elif Average >= 60 :
    print("Performance Pass")
else:
    print("Performance failed")

print("Total :", Total)
print("Average :", Average)

#student[keys] = keys
if "Python" in student['skills']["Python"] :
print("Python enrolled")
#else:
print("Python not enrolled")

values = student.values('skills')
print(values) 
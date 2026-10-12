def calculate_average(scores):
    aver = sum(scores) / len(scores)
    return aver

def get_grade(scores):
    average = calculate_average(scores)

    if 70 > average >= 50:
        return "C"
    elif 80 > average >= 70:
        return "B"
    elif 100 >= average >= 80:
        return "A"
    else:
        return "F"

def create_student(name, scores):
    grade = get_grade(scores)
    average=calculate_average(scores)
    return {
        "name": name,
        "scores": scores,
        "average": average,
        "grade": grade
    }

student = create_student("Chala", [80, 90, 100])
print(student)

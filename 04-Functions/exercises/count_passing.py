students = [
    {'name': 'Chala', 'scores': [80, 90, 100]},
    {'name': 'Aanaa', 'scores': [33, 46, 43]},
    {'name': 'Mimi', 'scores': [75, 85, 95]}
]
def get_av(student):
    return sum(student["scores"]) / len(student["scores"])

def passing(students):
    total_passing = 0
    for student in students :
        current_average = get_av(student)
        if current_average >= 50  :
            total_passing += 1
    return total_passing
print(passing(students))
name = "Aanaa"
def calculate_average ( Maths, English , Programming):
	return  ( Maths + English + Programming ) / 3
	
def get_grade(average ): 
	
	if average >= 85 and average <=100 :
		return "A"
	elif average >= 75 and average < 85  : 
		return "B"
	elif average >= 70 and average < 75 :
		return "C"
	elif average >= 60 and average < 70 : 
		return "D" 
	elif average < 60 :
		return "F" 
	else : 
		return "Invalid  point"

def is_passed(grade):

	if grade != "F" :
		return "Passed"
	else: 
		return "failed"

average = calculate_average(100, 85, 95)
grade = get_grade(average)
status = is_passed(grade)

print("Name:", name)
print("Average:", average)
print("Grade:", grade)
print("Status:", status)
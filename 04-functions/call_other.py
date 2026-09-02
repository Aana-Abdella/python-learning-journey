def square(number):
	return number * number
	
def add_ten(number):
	result = square(number)
	return result + 10


print(add_ten(10))
print(add_ten(5))

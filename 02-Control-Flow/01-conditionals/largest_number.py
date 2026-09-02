def find_largest(a, b, c):
	if a >= b and a >= c :
		return a
	elif b >= a and b >= c :
		return b
	else:
		return c


print(find_largest(10, 20, 5) ) 
print(find_largest(50, 30, 40) )
print(find_largest(7, 7, 3) )
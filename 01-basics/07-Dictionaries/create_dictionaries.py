# Using dict() when key are valid name

person = dict(name ="Aanaa", age=21, career="software Engeneering")

print(person)

# Using list pairs

pairs = [("Name", "Aanaa"), ("age", 21), ("career", "Software Engeeneer")]
print(dict(pairs))

#By joining two pair or list

key = ["Name", "age", "career"]
values = ["Chala", 26, "leacture"]

teach = dict(zip(key, values))
print(teach)
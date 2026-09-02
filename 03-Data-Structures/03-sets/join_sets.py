# Using union()

set1 = {"Aanaa","chala"}
set2 = {"Obsa", "Fahmi"}

set3 = set1.union(set2)
print(set3)

# Use update()

set1.update(set2)
print(set1)

# use intersection

set4 = {"Badhe","Mage","Game"}
set5 = {"Badhe","Gamme","Ana"}

set6 = set5.intersection(set4)
print(set6)

# use difference 
set7 = set4.difference(set6)
print(set7)

# Use symetric_difference

set8 = set4.symmetric_difference(set5)
print(set8)
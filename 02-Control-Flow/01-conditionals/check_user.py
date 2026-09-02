users = {'Aanaa': 'Active', 'Chala': 'Inactive','Obsaa' : 'Inactive', 'Gamme' : 'Active'}

for user, status in users.copy().items():
    if status == 'Inactive' :
        del users[user]

active_user = {}
for user in users.items():
    if status == 'Active':
        active_user[user] = status
        print(active_user)
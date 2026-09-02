def create_account(username, email, active=True):
    return {
        "username": username,
        "email": email,
        "active": active,
    }

account = create_account(
    email="ana@devenest.com",
    username="devnest", )

newusername=create_account(
    email=str(input("Enter your email: ")),
    username=str(input("Enter your username: ")),
)

print(newusername)
print(account)
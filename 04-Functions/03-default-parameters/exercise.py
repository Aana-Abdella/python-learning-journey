# default parameter values
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greeting_message = greet("Aanaa")
greeting_message_with_custom_greeting = greet("Aanaa", "Hi")

print(greeting_message) 
print(greeting_message_with_custom_greeting) 
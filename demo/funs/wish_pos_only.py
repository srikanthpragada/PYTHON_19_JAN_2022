# positional-only arguments

def wish(user, message, /):
    print(message, user)


#wish(user="Abc", message="Hi")
wish("Abc", "Hi")

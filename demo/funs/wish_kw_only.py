# Keyword-only arguments

def wish(*, message, user):
    print(message, user)


wish(user="Abc", message="Hi")
# wish("Abc", "Hi")

def wish(user: str, msg: str) -> None:
    print(msg, user)


wish("Roberts", "Hi")  # Positional parameters
wish(msg="Hello", user="Steve")  # Keyword parameters

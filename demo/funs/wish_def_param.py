def wish(user='Guest', msg='Hi') -> None:
    print(msg, user, sep='-', end='\n\n')


wish("Roberts")
wish("Scott", "Hello")
wish(user="Andy", msg="Hello")
wish(user="Bob")
wish()
wish(msg="Good Morning")

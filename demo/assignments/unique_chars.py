def unique_chars(*values):
    chars = set()
    for n in values:
        chars = chars | set(n)   # chars |= set(n)

    return "".join(sorted(chars))


print(unique_chars("abc", "xyz", "aq"))
print(unique_chars("Python", "Java", "JavaScript"))

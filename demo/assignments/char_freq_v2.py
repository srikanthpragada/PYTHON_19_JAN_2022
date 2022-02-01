st = "Hello"

chars = ""
for c in st:
    if c not in chars:
        print(f"{c} occurs {st.count(c)} times")
        chars += c

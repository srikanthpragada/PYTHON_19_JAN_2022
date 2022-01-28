# Count unique digits
st = "How do you do"
ss = "o"
pos = -1
while True:
    pos = st.find(ss, pos + 1)
    if pos == -1:  # not found
        break

    print(pos)

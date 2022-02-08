def isvalidpan(s):
    return len(s) == 10 and s[:5].isalpha() and s[5:9].isdigit() and s[-1].isalpha()


pans = ['ABCDE3939X', 'AHBCD8383', 'ABCDE83838', 'ABCDE3939K']

for p in filter(isvalidpan, pans):
    print(p)

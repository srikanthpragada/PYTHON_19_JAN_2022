import re

with open("old_man.txt", "rt") as f:
  contents = f.read()

words = {}
for word in re.findall(r"\w+", contents):
    if word in words:
        words[word] = words[word] + 1  # Increment count
    else:
        words[word] = 1   # start with 1 for new word

for word, count in sorted(words.items()):
    print(f"{word:15} {count:3}")








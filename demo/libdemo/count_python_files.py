
import os

entries = os.walk(r"d:\classroom\jan19\demo")
count = 0
for (foldername, folders, files) in entries:
    for filename in files:
        if filename.endswith(".py"):
            print(foldername + "\\" + filename)
            count += 1


print(f"Count = {count}")

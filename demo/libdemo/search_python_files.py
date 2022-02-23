import os


def file_has_string(filename, string):
    with open(filename, "rt") as f:
        contents = f.read()
        return string in contents


entries = os.walk(r"d:\classroom\jan19\demo")
search_string = input("Enter search string : ")
for (foldername, folders, files) in entries:
    for filename in files:
        if filename.endswith(".py"):
            fullpath = foldername + "\\" + filename
            if file_has_string(fullpath, search_string):
                print(fullpath)

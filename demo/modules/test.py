import sys

#print(sys.path)

sys.path.insert(0, r'C:\batches\jan19\demo\mylib')

import num_funs as nf

print(nf.iseven(11))
print(nf.PI)

# dir(module) returns list of members
for name in dir(nf):
    if not name.startswith("__"):
        print(name)

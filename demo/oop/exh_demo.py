
try:
    num = int(input("Enter number :"))
    res = 100 / num
    print(res)
except Exception as ex:
    print(type(ex))
    print('Sorry! ', ex)

print("The End")

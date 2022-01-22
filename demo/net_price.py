# Calculate net price

data = input("Enter price :")
price = int(data)     # convert string to int
discount = price * 10 / 100
net_price = price - discount
print("Net price = ", net_price)

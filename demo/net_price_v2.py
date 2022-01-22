# Calculate net price
data = input("Enter price :")
price = int(data)  # convert string to int

if price > 5000:
    discount = price * 20 / 100
else:
    discount = price * 10 / 100

net_price = price - discount

print(f"Price        {price:8.2f}")
print(f"- Discount   {discount:8.2f}")
print(f"Net price    {net_price:8.2f}")

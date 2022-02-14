class Product:
    taxrate = 12

    @staticmethod
    def change_taxrate(newrate):
        Product.taxrate = newrate

    def __init__(self, id, name, price, disrate=0):
        self.id = id
        self.name = name
        self.type = type
        self.price = price
        self.disrate = disrate

    def print_details(self):
        print(f"Product Id     :   {self.id}")
        print(f"Name           :   {self.name}")
        print(f"Price          :   {self.price}")
        print(f"Discount Rate  :   {self.disrate}%")

    def get_net_price(self):
        baseprice = self.price
        discount = baseprice * self.disrate / 100
        baseprice -= discount
        tax = baseprice * Product.taxrate / 100
        return baseprice + tax


p1 = Product(101, 'iphone11', 50000, 15)
p1.print_details()
Product.change_taxrate(15)
print(p1.get_net_price())

# Design a class Product with attributes name, price.
# Create a class DiscountedProduct that inherits from Product and 
# adds a method to calculate price after discount.
# Tasks:
# Accept a discount percentage as input.
# Calculate and return the final price after discount.
# Print a bill showing original and discounted price.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class DiscountedProduct(Product):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    def calculate_price_after_discount(self):
        discount_amount = self.price * (self.discount / 100)
        self.price_after_discount = self.price - discount_amount
        return self.price_after_discount

    def show_bill(self):
        return f"Name of Product: {self.name}\nOriginal Price: {self.price}\nDiscount Applied: {self.discount}%\nPrice After Discount: {self.price_after_discount}"

product = DiscountedProduct("Pen", 100, 20)
product.calculate_price_after_discount()
print(product.show_bill())
print("")

product2 = DiscountedProduct("Notebook", 50, 10)
product2.calculate_price_after_discount()
print(product2.show_bill())



        
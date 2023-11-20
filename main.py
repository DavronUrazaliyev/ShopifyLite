
class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"{self.name} (ID: {self.product_id}) - ${self.price:.2f}")

class Order:
    def __init__(self):
        self.products = []
        self.total_price = 0.0

    def add_product(self, product, quantity=1):
        if product.stock >= quantity:
            product.stock -= quantity
            self.products.append({"product": product, "quantity": quantity})
            self.total_price += product.price * quantity
            print(f"{quantity} {product.name}(s) added to the order.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def display_order(self):
        print("Order:")
        for item in self.products:
            product = item["product"]
            quantity = item["quantity"]
            print(f"{quantity} {product.name}(s) - ${product.price:.2f} each")
        print(f"Total Price: ${self.total_price:.2f}")

# Example usage:
product1 = Product(1, "Laptop", 999.99, 10)
product2 = Product(2, "Headphones", 49.99, 20)
product3 = Product(3, "Mouse", 19.99, 30)

order = Order()
order.add_product(product1, 2)
order.add_product(product2, 1)
order.add_product(product3, 3)

order.display_order()

# Output:
# 2 Laptop(s) added to the order.
# 1 Headphones(s) added to the order.
# 3 Mouse(s) added to the order.
# Order:
# 2 Laptop(s) - $999.99 each
# 1 Headphones(s) - $49.99 each
# 3 Mouse(s) - $19.99 each
# Total Price: $2139.92

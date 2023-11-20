from src.product import Product
from src.order import Order

p1 = Product(name="Iphone 12", price=450.00, quantity=67)
p2 = Product(name="Samsung s21", price=750.00, quantity=42)

order1 = Order()
order1.add_product(p1, 3)
order1.add_product(p2, 6)

print(order1.display())
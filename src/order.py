
from .product import Product


class Order:
    """
    class: Order

    attributes: 
        1. order_id (int) unique
        2. products (list)
    
    mathods:
        1. add_product 
        2. display - report
    """
    id = 1

    def __init__(self):
        self.order_id = Order.id
        self.products = []

        Order.id += 1

    def add_product(self, product: Product, quantity: int):
        product.quantity -= quantity

        self.products.append({
            "product": product,
            "quantity": quantity
        })

    def display(self) -> str:
        report = f"#{self.order_id} Your Order:\n\n"

        count = 1
        total = 0
        for item in self.products:
            sub_total = item['quantity'] * item['product'].price
            total += sub_total

            report += f"{count}. #{item['product'].product_id}-{item['product'].name} X {item['quantity']} = {sub_total}\n"

            count += 1

        return report + f"\n\nTotal: {total}"
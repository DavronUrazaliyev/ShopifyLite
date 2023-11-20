# ShopifyLite - Object-Oriented Programming (OOP) Shop Project

## Description

PyMarket is a simple online shop project designed for learning and practicing Object-Oriented Programming (OOP) concepts in Python. It includes two main classes, `Product` and `Order`, to simulate the basic functionality of an online store.

## Features

- **Product Class:** Represents a product with attributes such as product ID, name, price, and stock.
- **Order Class:** Represents an order that can contain multiple products with quantities.
- **Add Products to Order:** Users can add products to their order, considering available stock.
- **Display Order:** View the details of the order, including products, quantities, and total price.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/PyMarket.git
   ```

2. Navigate to the project directory:

   ```bash
   cd PyMarket
   ```

3. Run the example script:

   ```bash
   python main.py
   ```

## Usage

1. Create instances of the `Product` class with specific details (product ID, name, price, stock).
2. Create an instance of the `Order` class to start a new order.
3. Use the `add_product` method to add products to the order.
4. Display the order details using the `display_order` method.

Example:

```python
product1 = Product(1, "Laptop", 999.99, 10)
product2 = Product(2, "Headphones", 49.99, 20)
product3 = Product(3, "Mouse", 19.99, 30)

order = Order()
order.add_product(product1, 2)
order.add_product(product2, 1)
order.add_product(product3, 3)

order.display_order()
```

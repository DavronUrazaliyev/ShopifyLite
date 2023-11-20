class Product:
    """
    class: Product

    attributes:
        1. product_id (int)
        2. name (str)
        3. price (float)
        4. quantity (int)

    methods:
        1. info - information about product
    """
    id = 1

    def __init__(self, name: str, price: float, quantity: int):
        self.product_id = Product.id
        self.name       = name
        self.price      = price
        self.quantity   = quantity

        Product.id += 1

    def info(self) -> str:
        return f"{self.product_id}. {self.name} costs {self.price}. total: {self.quantity}"

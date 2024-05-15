class MobileFactory:
    PRICES = {
        'A': 10.28, 'B': 24.07, 'C': 33.30,
        'D': 25.94, 'E': 32.39,
        'F': 18.77, 'G': 15.13, 'H': 20.00,
        'I': 42.31, 'J': 45.00,
        'K': 45.00, 'L': 30.00
    }

    COMPONENTS = {
        'A': 'LED Screen', 'B': 'OLED Screen', 'C': 'AMOLED Screen',
        'D': 'Wide-Angle Camera', 'E': 'Ultra-Wide-Angle Camera',
        'F': 'USB-C Port', 'G': 'Micro-USB Port', 'H': 'Lightning Port',
        'I': 'Android OS', 'J': 'iOS OS',
        'K': 'Metallic Body', 'L': 'Plastic Body'
    }

    def __init__(self):
        self.order_id = None

    def create_order(self, components):
        if len(components) != 5 or len(set(components)) != 5:
            return 400, "Invalid order: must contain one and only one part of each type."

        total_price = sum(self.PRICES[component] for component in components)
        parts = [self.COMPONENTS[component] for component in components]

        self.order_id = "some-id"  # You can implement your own order ID generation logic here

        return 201, {"order_id": self.order_id, "total": total_price, "parts": parts}


# Example usage
factory = MobileFactory()
status, response = factory.create_order(["I", "A", "D", "F", "K"])
print(status)
print(response)

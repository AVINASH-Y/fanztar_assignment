# fanztar_assignment

Mobile Factory
This code represents a simple mobile phone factory simulation where orders for mobile phones are created based on specific components. Each component has a corresponding price, and the factory can create orders with a combination of different components.

Features
Order Creation: The factory can create orders for mobile phones with a specified set of components.
Validation: The code ensures that each order contains exactly one part of each type.
Price Calculation: The total price of an order is calculated based on the selected components.
Order ID Generation: An order ID is generated for each created order.
Usage
To use the MobileFactory class:

Instantiate the factory: factory = MobileFactory().
Create an order by providing a list of component codes to the create_order method: status, response = factory.create_order(components).
The method returns a status code and a response dictionary containing the order ID, total price, and selected parts.
Example:

python
Copy code
factory = MobileFactory()
status, response = factory.create_order(["I", "A", "D", "F", "K"])
print(status)  # Output: 201 (Created)
print(response)  # Output: {'order_id': 'some-id', 'total': 146.3, 'parts': ['Android OS', 'LED Screen', 'Wide-Angle Camera', 'USB-C Port', 'Metallic Body']}
Constants
PRICES: Dictionary mapping component codes to their prices.
COMPONENTS: Dictionary mapping component codes to their descriptions.
Error Codes
400: Invalid order - must contain one and only one part of each type.
Customization
You can implement your own order ID generation logic in the create_order method.

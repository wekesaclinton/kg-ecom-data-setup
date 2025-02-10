import json
from typing import List, Optional, Dict, Any

class Product:
    def __init__(self, product_name: str, product_cost: str):
        self.product_name = product_name
        self.product_cost = product_cost
    def __repr__(self):
        return f"product(name='{self.product_name}', cost='{self.product_cost}'"
class Order:
    def __init__(self, total_cost: int, products: List[Product], state: str):
        self.total_cost = total_cost
        self.products = products
        self.state = state
        # self.destination = destination
    def __repr__(self):
        return f"order(total_cost='{self.total_cost}', state='{self.state}', destination='{self.destination}'"
class Customer:
    def __init__(self, customer_id: str, customer_name: str, gender: str, orders: List[Order]):
        self.customer_id = customer_id
        self.customer_name = customer_name
        self.gender = gender
        self.orders = orders

    def __repr__(self):
        return f"customer(name='{self.customer_name}', gender='{self.gender}'"
def load_data_from_json(filepath: str) -> List[Customer]:
    """Loads data from a JSON file and returns a list of Person objects."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        customer_list: List[Customer] = []
        for person_data in data:

            order_list: List[Order] = []
            for order in person_data['orders']:

                product_list: List[Product] = []
                for products in order['products']:
                    product = Product(
                        product_name = products["product_name"],
                        product_cost = products["product_cost"]
                    )
                    product_list.append(product)
                order_det = Order(
                    products = product_list,
                    total_cost = order["total_cost"],
                    state = order["state"]
                )
                order_list.append(order_det)
            customer = Customer(
                customer_id = person_data["customer_id"],  # Required field, so access directly
                customer_name = person_data["customer_name"],
                gender = person_data["gender"],
                orders= order_list
            )
            customer_list.append(customer)
        return customer_list

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []  # Or raise the exception if you prefer
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filepath}")
        return []
    except KeyError as e:
        print(f"Error: Missing key {e} in JSON data")
        return []
    except TypeError as e:
        print(f"Error: Type mismatch in JSON data: {e}")
        return []

# Example usage:
filepath = 'datafiles/user_data.json'  # Replace with your file path
print("We are now printing data here...")
people_data = load_data_from_json(filepath)
if people_data:
    for person in people_data:
        print(person)

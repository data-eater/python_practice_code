from time import sleep

from pizza import Pizza
from utils import random_alpha_numeric_generator


class PizzaBuilder:
    def __init__(self):
        self.current_pizza = None

    def create_pizza(self):
        self.current_pizza = Pizza()

    def set_pizza_size(self, selected_size):
        self.current_pizza.size = selected_size

    def set_pizza_base(self, selected_base):
        self.current_pizza.base = selected_base

    def add_additional_topping(self, selected_topping):
        action = "add"
        self.current_pizza.additional_toppings = {
            "action": action,
            "name": selected_topping,
        }

    def remove_additional_topping(self, selected_topping):
        action = "remove"
        self.current_pizza.additional_toppings = {
            "action": action,
            "name": selected_topping,
        }

    def current_additional_toppings(self):
        return {
            index + 1: value
            for index, value in enumerate(self.current_pizza.additional_toppings)
        }

    def pizza_details(self):
        details = {
            "size": self.current_pizza.size if self.current_pizza.size else None,
            "base": self.current_pizza.base if self.current_pizza.base else None,
            "additional-toppings": self.current_pizza.additional_toppings
            if self.current_pizza.additional_toppings
            else None,
        }
        return details

    def is_pizza_completed(self):
        pizza = self.pizza_details()
        for key, value in pizza.items():
            if value == None and key != "additional-toppings":
                return False
        return True

    def pizza_order_confirm(self):
        print("\nYour pizza order has been confirmed\n")
        order_id = random_alpha_numeric_generator()
        print(f"Your Order ID is : {order_id}\n")
        sleep(5)

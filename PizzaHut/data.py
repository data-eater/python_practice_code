from enum import Enum

START_MENU = """
Welcome To Pizza Hut

Enter number with respect to your choice : 

1) Create Your Pizza
2) To View Analytics Of Additional Toppings
3) Quit

"""

PIZZA_CREATION_MENU = """

Enter number with respect to your choice : 

1) Select Pizza Size
2) Select Pizza Base
3) Select Additional Toppings To Add
4) Select Additional Toppings To Remove
5) Review Pizza
6) Confirm Order
7) Quit

"""

PIZZA_SIZE_MENU = """

Enter number with respect to your choice : 

Select Pizza Size

1) Small
2) Medium
3) Large

"""

PIZZA_SIZES = {
    1: "small",
    2: "medium",
    3: "large",
}

PIZZA_BASE_MENU = """

Enter number with respect to your choice : 

Select Pizza Base

1) Thin
2) Thick

"""

PIZZA_BASES = {
    1: "thin",
    2: "thick",
}


PIZZA_ADD_ADDITIONAL_TOPPING = """

Enter number with respect to your choice : 

Select Additional Toppings To ADD

1) Pepperoni
2) Chicken
3) Extra Cheese
4) Mushrooms
5) Spinach
6) Olives

"""


PIZZA_ADDITIONAL_TOPPINGS = {
    1: "pepperoni",
    2: "chicken",
    3: "extra_cheese",
    4: "mushrooms",
    5: "spinach",
    6: "olives",
}


PIZZA_REMOVE_ADDITIONAL_TOPPING = """
Enter number with respect to your choice : 
                
Select Additional Toppings To ADD
                
Current Toppings : 
                
"""

PIZZA_SIZES = [
    "small",
    "medium",
    "large",
]
PIZZA_BASES = [
    "thick",
    "thin",
]
STANDARD_TOPPINGS = [
    "tomato",
    "cheese",
]
ADDITIONAL_TOPPINGS = [
    "pepperoni",
    "chicken",
    "extra_cheese",
    "mushrooms",
    "spinach",
    "olives",
]


class MenuChoicesCount(Enum):
    MAIN = 3
    CREATE = 7
    PIZZA_SIZE = 3
    PIZZA_BASE = 2
    PIZZA_ADDITIONAL_TOPPINGS = 6


class MainMenuChoices(Enum):
    CREATE_PIZZA = 1
    ANALYSIS = 2
    QUIT = 3


class CreateMenuChoices(Enum):
    SET_SIZE = 1
    SET_BASE = 2
    SET_ADDITIONAL_TOPPINGS = 3
    REMOVE_ADDITIONAL_TOPPINGS = 4
    PIZZA_REVIEW = 5
    ORDER_CONFIRM = 6
    QUIT = 7

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


class Pizza:
    def __init__(self):
        self._size = ""
        self._base = ""
        self._standard_toppings = STANDARD_TOPPINGS
        self._additional_toppings = []

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, new_size):
        if new_size in PIZZA_SIZES:
            self._size = new_size
        else:
            print(
                f"Please enter valid pizza size. Available Sizes are : {', '.join(PIZZA_SIZES)}"
            )

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, new_base):
        if new_base in PIZZA_BASES:
            self._base = new_base
        else:
            print(
                f"Please enter valid pizza base. Available Bases are : {', '.join(PIZZA_BASES)}"
            )

    @property
    def additional_toppings(self):
        return self._additional_toppings

    @additional_toppings.setter
    def additional_toppings(self, topping):
        action = topping.get("action")
        topping_name = topping.get("name")
        if topping_name in ADDITIONAL_TOPPINGS:
            if action == "add":
                if topping_name in self.additional_toppings:
                    print("\n[!] Topping already added, add another one.")
                    return
                if len(self.additional_toppings) < 3:
                    self._additional_toppings.append(topping_name)
                else:
                    print("You can only add maximum of 3 additional toppings")
            elif action == "remove":
                if topping_name in self.additional_toppings:
                    self._additional_toppings.remove(topping_name)
                else:
                    print(
                        f"You can only remove a topping that is present on the pizza. Currently f{', '.join(self.additional_toppings) if self.additional_toppings else 'no'} toppings are on the pizza"
                    )
        else:
            print(
                f"Please enter valid additional topping. Available Additional Toppings are : {', '.join(ADDITIONAL_TOPPINGS)}"
            )

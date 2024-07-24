import os
import time
from enum import Enum

from data import *
from pizza_builder import PizzaBuilder
from utils import menu_input
from recorder import Recorder


while True:
    user_choice = menu_input(menu_text=START_MENU, choices_count=MenuChoicesCount.MAIN)
    pizza_builder = PizzaBuilder()
    recorder = Recorder()
    if user_choice == MainMenuChoices.QUIT:
        break
    elif user_choice == MainMenuChoices.ANALYSIS:
        recorder.analysis()
    elif user_choice == MainMenuChoices.CREATE_PIZZA:
        os.system("clear")
        pizza_builder.create_pizza()
        while True:
            user_choice = menu_input(
                menu_text=PIZZA_CREATION_MENU, choices_count=MenuChoicesCount.CREATE
            )
            if user_choice == CreateMenuChoices.QUIT:
                break
            elif user_choice == CreateMenuChoices.SET_SIZE:
                user_choice = menu_input(
                    menu_text=PIZZA_SIZE_MENU, choices_count=MenuChoicesCount.PIZZA_SIZE
                )
                pizza_builder.set_pizza_size(PIZZA_SIZES.get(user_choice))
            elif user_choice == CreateMenuChoices.SET_BASE:
                user_choice = menu_input(
                    menu_text=PIZZA_BASE_MENU, choices_count=MenuChoicesCount.PIZZA_BASE
                )
                pizza_builder.set_pizza_base(PIZZA_BASES.get(user_choice))
            elif user_choice == CreateMenuChoices.SET_ADDITIONAL_TOPPINGS:
                user_choice = menu_input(
                    menu_text=PIZZA_ADD_ADDITIONAL_TOPPING,
                    choices_count=MenuChoicesCount.PIZZA_ADDITIONAL_TOPPINGS,
                )
                pizza_builder.add_additional_topping(
                    PIZZA_ADDITIONAL_TOPPINGS.get(user_choice)
                )
            elif user_choice == CreateMenuChoices.REMOVE_ADDITIONAL_TOPPINGS:
                current_toppings = pizza_builder.current_additional_toppings()
                number_current_toppings = len(current_toppings)
                if number_current_toppings == 0:
                    print("[!] No Toppings Added Yet")
                    time.sleep(4)
                    continue
                user_choice = menu_input(
                    menu_text=(
                        PIZZA_REMOVE_ADDITIONAL_TOPPING
                        + " ".join(
                            [
                                f"{key}) {value.replace('_',' ').capitalize()}"
                                for key, value in current_toppings.items()
                            ]
                        )
                    ),
                    choices_count=number_current_toppings,
                )
                pizza_builder.remove_additional_topping(
                    current_toppings.get(user_choice)
                )
            elif user_choice == CreateMenuChoices.PIZZA_REVIEW:
                print("\nPizza Review\n")
                for key, value in pizza_builder.pizza_details().items():
                    print(
                        f"{key} : {value if value else f'No {key.capitalize()} selected for pizza yet'}"
                    )
                time.sleep(3)
            elif user_choice == CreateMenuChoices.ORDER_CONFIRM:
                # For order confirmation
                order_info = pizza_builder.pizza_details()
                if not pizza_builder.is_pizza_completed():
                    print(
                        "\n[!] Necessary components not added yet. Size and base are compulsory to select, to order your pizza."
                    )
                    time.sleep(4)
                    continue
                recorder.add_order()
                recorder.add_order_record(order=order_info)
                pizza_builder.pizza_order_confirm()
                break

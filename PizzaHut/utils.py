from random import choices
from string import ascii_letters, digits


def custom_input(message):
    try:
        return int(input(message))
    except:
        print("\n [!] Enter Numbers Only\n")
        return 0


def random_alpha_numeric_generator():
    return "".join(choices(ascii_letters + digits, k=8))


def str_to_int_list(new_list):
    list_to_return = []
    for item in new_list:
        list_to_return.append(int(item))
    return list_to_return


def int_to_str_list(new_list):
    list_to_return = []
    for item in new_list:
        list_to_return.append(str(item) + "\n")
    return list_to_return


def menu_input(menu_text, choices_count):
    print(menu_text)
    user_choice = custom_input(" > ")
    if user_choice <= choices_count and user_choice > 0:
        return user_choice
    while True:
        print(menu_text)
        user_choice = custom_input(
            f"Enter valid choice between 1 and {choices_count} >"
        )
        if user_choice <= choices_count and user_choice > 0:
            return user_choice

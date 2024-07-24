from enum import Enum

from utils import int_to_str_list, str_to_int_list
from pizza import ADDITIONAL_TOPPINGS


class RecordMapping(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3
    THIN = 4
    THICK = 5
    PEPPERONI = 6
    CHICKEN = 7
    EXTRA_CHEESE = 8
    MUSHROOMS = 9
    SPINACH = 10
    OLIVES = 11


class Recorder:
    def __init__(self):
        self.total_orders = 0

    def add_order(self):
        self.total_orders += 1

    def add_order_record(self, order):
        record_to_enter = []
        with open("./record.txt", "r+") as file:
            file_data = file.readlines()
            file_data = str_to_int_list(file_data)
            for pizza_item in order.values():
                print(type(pizza_item), pizza_item)
                if type(pizza_item) == list:
                    for item in pizza_item:
                        record_to_enter.append(item)
                else:
                    if pizza_item != None:
                        record_to_enter.append(pizza_item)
            if file_data:
                for record_item in record_to_enter:
                    file_data[(RecordMapping[record_item.upper()].value) - 1] += 1
            else:
                for item in RecordMapping:
                    if item.name.lower() in record_to_enter:
                        file_data.append(str(1))
                    else:
                        file_data.append(str(0))
            file_data = int_to_str_list(file_data)
            file.seek(0)
            file.writelines(file_data)

    def analysis(self):
        analysis_dict = {}
        with open("./record.txt", "r") as file:
            file_data = file.readlines()
            for item in RecordMapping:
                if item.name.lower() in ADDITIONAL_TOPPINGS:
                    analysis_dict[item.name.lower()] = file_data[item.value - 1]
        if file_data:
            list_for_analysis = str_to_int_list(analysis_dict.values())
            toppings_list = list(analysis_dict.keys())
            total_toppings_sold = sum(list_for_analysis)
            percentage_sold_toppings_list = [
                (value / total_toppings_sold) * 100 for value in list_for_analysis
            ]
            max_percentage = max(percentage_sold_toppings_list)
            min_percentage = min(percentage_sold_toppings_list)
            most_favourite_toppings = [
                index
                for index, value in enumerate(percentage_sold_toppings_list)
                if value == max_percentage
            ]
            least_favourite_toppings = [
                index
                for index, value in enumerate(percentage_sold_toppings_list)
                if value == min_percentage
            ]
            print("Most Favourite Toppings : ")
            for item in most_favourite_toppings:
                print(
                    f"{toppings_list[item]} : {round(percentage_sold_toppings_list[item],2)}%"
                )
            print("Least Favourite Toppings : ")
            for item in least_favourite_toppings:
                print(
                    f"{toppings_list[item]} : {round(percentage_sold_toppings_list[item],2)}%"
                )
        else:
            print("No toppings data present to perform analysis")

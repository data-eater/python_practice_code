import itertools


class List:
    def __init__(self, x=0):
        self.list = x

    def __str__(self):
        return "({0},{1})".format(self.list)

    def __add__(self, other: "List"):
        new_list = []
        for x, y in itertools.zip_longest(self.list, other.list, fillvalue=0):
            new_list.append(x + y)
        return new_list

    def __sub__(self, other: "List"):
        new_list = []
        for x, y in itertools.zip_longest(self.list, other.list, fillvalue=0):
            new_list.append(x - y)
        return new_list


list1 = List([1, 2, 3, 4, 5])
list2 = List([6, 7, 8, 9, 10, 11, 12, 13, 14])

print(list2 - list1)

print(list1)

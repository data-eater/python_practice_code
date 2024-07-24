
try:
    tuple1=(1,2,4,5,6)
    tuple1.appen(1)
except Exception as err:
    print(err)


tuple4 = (5, 10, 15, 20, 25, 30)
sliced_tuple = tuple4[1:4]
print("Sliced Tuple:", sliced_tuple)



tuple6a = (1, 2, 3)
tuple6b = (4, 5, 6)
concatenated_tuple = tuple6a + tuple6b
print("Concatenated Tuple:", concatenated_tuple)

list10 = [1, 2, 3, 4, 5]
tuple10 = tuple(list10)
print("Tuple:", tuple10)

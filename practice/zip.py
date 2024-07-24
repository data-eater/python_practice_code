import itertools


list1=[1,2,3,4,5,6,7,8,9]
list2=[10,11,12,13,14,15,16,17,18,19,20,21]


print(list(zip(list1,list2,strict=False)))


for x in itertools.zip_longest(list1,list2,fillvalue=0):
    print(x)
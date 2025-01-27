###List Comprehension ###

my_original_list = [32, 23, 23, 12, 33, 1, 31]
print(my_original_list)

my_range = range(8)
print(list(my_range))

#Definicion
my_list = [i +1 for i in range(8)]
print(my_list)

my_list = [i *2 for i in range(8)]
print(my_list)

my_list = [i * i for i in range(8)]
print(my_list)

def sum_five(number):
    return number + 5
my_list = [sum_five(i) for i in range(8)]
print(my_list)
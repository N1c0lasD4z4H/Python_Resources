### Higher Order Functions ###
#Funciones que son capaces de ejecutar funciones 
from functools import reduce

def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_value(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))

## Closures ##
#
def sum_ten(original_value):
    def add(value):
        return value+10 + original_value
    return add
add_closure = sum_ten(1)
print(add_closure(15))
print((sum_ten(5))(1))

## Built-in Higher Order Functions ## funciones de orden superior que ya existen en el propio lenguaje

numbers = [2, 5, 10 ,21, 3, 30]
#Map: recorre cada uno de los valores y ejecuta una función
def multiply_two(number):
    return number * 2
map(multiply_two, numbers)
print(list(map(multiply_two, numbers)))
# Lambda
print(list(map(lambda number:number * 2, numbers)))

# Filter: recorre los valores y filtra valores
def filter_greater_that_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_that_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce : Operar los valores que va recorriendo y va operando 
# con los valores que a medida va recorriendo el iterable es decir la lista
numbers = [2, 5, 10 ,21, 3, 30]

def sum_two_values(first_value,second_value):
    print(first_value)
    print(second_value)
    return first_value + second_value


print(reduce(sum_two_values, numbers))

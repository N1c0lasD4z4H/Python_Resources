### list ###Mutable

# Definición
my_list = list()

my_other_list = []

print(len(my_list))

my_list = [32, 23, 23, 12, 33, 1, 31]

print(my_list)
print(len(my_list))

my_other_list = [20, 1.75, "Nicolas", "Daza"]

print(type(my_list))
print(type(my_other_list))

# Acceso a elementos y búsqueda
print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-3])
print(my_list.count(23))
# print(my_other_list[4]) IndexError
# print(my_other_list[-5]) IndexError

age, height, name, surname = my_other_list
print(name)
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(age)


# Concatenación
print(my_list + my_other_list)
#print(my_list - my_other_list)

# Creación, inserción, actualización y eliminación
my_other_list.append("Daza.sas")
print(my_other_list)

my_other_list.insert(1,"Azul")
print(my_other_list)

my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(23)
print(my_list)

print(my_list.pop())
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

del my_list[2]
print(my_list)

# Operaciones con listas
my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

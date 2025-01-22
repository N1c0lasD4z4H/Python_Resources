### Dictionaries ###

# Definición
my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Nicolas","Apellido":"Daza","Edad":20, 1:"Python"}

my_dict = {# almacenar datos de tipo valor
    "Nombre":"Nicolas",
    "Apellido":"Daza",
    "Edad":20, 
    "Lenguajes":{"Python","Swift","Kotlin"},
    1:1.77
    }

print(my_other_dict)
print(my_dict)

print(len(my_other_dict))
print(len(my_dict))

# Búsqueda
print(my_dict[1])
print(my_dict["Nombre"])# Facilidad para acceder a un elemento

print("Moure" in my_dict)
print("Apellido" in my_dict)

# Actualización
my_dict["Nombre"] = "Pedro"#Actualizar datos
print(my_dict["Nombre"])

print(my_dict[1])

# Inserción
my_dict["Calle"] = "CALLE 69K"#Añadir otro campo
print(my_dict)

#Eliminar un valor
del my_dict["Calle"]
print(my_dict)


# Otras operaciones
print("Daza" in my_dict)
print("Apellido" in my_dict)#Comprobar que existe

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_list = ["Nombre",1, "Piso"]

my_new_dict = dict.fromkeys((my_list))
print(my_new_dict)

my_new_dict = dict.fromkeys(("Nombre",1, "Piso"))
print(my_new_dict)

my_new_dict = dict.fromkeys((my_dict))
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "SamFernz")
print((my_new_dict))

my_values = my_new_dict.values()
print(type(my_values))

print(my_new_dict.values())
print(dict.fromkeys(list(my_new_dict.values())))
print(tuple(my_new_dict))
print(set(my_new_dict))
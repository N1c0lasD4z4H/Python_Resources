### Loops ###

#While bucle
my_condition = 0
# El bucle while se repite varias veces en funcion de una condicion
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else: # Es opcional
    print("Mi condición es mayor o igual que 10")

print("La ejecución continua")

while my_condition < 20:
    my_condition += 1
    if my_condition == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition)

print("La ejecución continua")

#For Bucle

my_list = [35, 24, 62, 52, 30, 30, 17]
#Se ejecuta x veces segun el numero de elementos iterables que haya 
for element in my_list:
    print(element)

my_tuple = (35, 1.77, "Nicolas", "Daza", "Brais")
for element in my_tuple:
    print(element)
my_set = {"Nicolas","Daza",35}
for element in my_set:
    print(element)
my_other_dict = {"Nombre":"Nicolas","Apellido":"Daza","Edad":20, 1:"Python"}
for element in my_other_dict:
    print(element)
    if element == "Edad":
        break
    print("Se ejecuta")
else: 
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continua")

for element in my_other_dict: 
    print(element)
    if element == "Edad":
        continue#No recomendado a lenguajes  modernos
    print("Se ejecuta")
else: 
    print("El bucle for para diccionario ha finalizado")

print("La ejecución continua") 



### Conditionals ###

#if
my_condition = False
if my_condition: #Es lo mismo que if my_condition == True:
    print("Se ejecuta la condición del if")

my_condition = 5*5

if my_condition ==10: 
    print("Se ejecuta la condición del segundo if")
else:
    print("Es menor que 11")

#if , elif, else
if my_condition > 10 and my_condition < 20: 
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor que 10 y mayor que 20 o distinto que 25")


print("La ejecucion continúa")

#Condicional con inspección de valor
my_string = "Mi cadena de texto"
if my_string:
    print("Mi cadena de texto no es vacía")

if my_string =="Mi cadena de textoooo":
    print("Cadenas de texto coinciden")
##
my_string = ""
if not my_string:
    print("Mi cadena de texto  es vacía")

if my_string =="Mi cadena de textoooo":
    print("Cadenas de texto coinciden")
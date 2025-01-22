### Functions ###
##Simple
def my_function (): 
    print("Esto es una funcion")

my_function ()
my_function ()

##Con parametros
def sum_two_values (frist_value, second_value):
    print(frist_value - second_value)
# acepta cualquier tipo de dato cuando se suma
sum_two_values(33,12)
sum_two_values(3123123,2323123)
sum_two_values(333,12)

#Función con párametros de entrada/argumentos y retorno
def sum_two_values_with_return (frist_value, second_value):
    return frist_value + second_value

my_result = sum_two_values_with_return(10, 5)
print(my_result)

def print_name (name, surname):
    print(f"{name} {surname}")

print_name("Nicolas", "Daza")

def print_name_with_default (name, surname, alias="Sin alias" ):
    print(f"{name} {surname} {alias}")
print_name_with_default("Nicolas", "Daza","PAZASS")
print_name_with_default("Nicolas", "Daza")

##Se pueden ingresar datos ilimitados a usar el "*"
def print_texts(*texts):
    print(texts)
print_texts("Hola","MM","JSJS" )



def print_texts(*texts):
    for text in texts:
        print(text.upper())
print_texts("hola","mmhv","nicolás" )
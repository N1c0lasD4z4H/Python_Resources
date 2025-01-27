### Error Types ###

# SyntaxError#

#print " Mama Huevo !!"
print("Catador de Gallus gallus domesticus")


#NameError

#Descomentar para error
#NameError: name 'language' is not defined
#print(language)
language = "Spanish"
print(language)

# IndexError 

my_list = ["Python", "Swift", "Kotlin", "Dart", "JavaScript"]
print(my_list[1])
print(my_list[-1])
#Descomentar para error
#print(my_list[5])  #IndexError: list index out of range

#ModuleNotFoundError

#Descomentar para error
#import maths  #ModuleNotFoundError: No module named 'maths'
import math

# AttributeError

#Descomentar para error
#print(math.PI)  #AttributeError: module 'math' has no attribute 'PI'
print(math.pi)

# Key error


my_dict = {"Nombre":"Nicolas","Apellido":"Daza","Edad":20, 1:"Python"}
print(my_dict["Edad"])
#Descomentar para error
#print(my_dict["Apelido"]) #KeyError: 'Apelido'

#TypeError

#Descomentar para error
# print(my_list["Nombre"]) # TypeError: list indices must be integers or slices, not str
print(my_list[0])

#ImportError

#Descomentar para error
#from math import PI  #ImportError: cannot import name 'PI' from 'math' (unknown location)
from math import pi
print(pi)

#ValueError

#Descomentar para error
#my_int = int("10 años")#ValueError: invalid literal for int() with base 10: '10 años'
my_int = int("10")
print(type(my_int))

# ZeroDivisionError

#Descomentar para error
#print (4/0) #ZeroDivisionError: division by zero
print(4/2)

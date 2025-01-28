### Regular Expressions ### 
#Comprobar que una cadena de texto tiene ciertos elementos
import re

## Match ##
my_string = "Esta es la lección 7: lección llamada Expresiones regulares"
my_other_string = "Esta No es la lección 6: Manejo de ficheros"

match = re.match("Esta es la lección",my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start: end])

match = re.match("Esta No es la lección",my_other_string)
#if not(match == None): #Otra forma de comprobar el none
#if match != None : #Otra forma de comprobar el none
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start: end])

#print(re.match("Expresiones regulares",my_string))

## Search ##
search = re.search("lección",my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start: end])

## Findall ##

findall = re.findall("lección",my_string, re.I)
print(findall)

## Split ##
print(re.split(":", my_string))

## Sub ##
print(re.sub("[L|l]ección", "LECCIÓN",my_string))
print(re.sub("Expresiones regulares","Regular expressions", my_string))

### Classes ### 

class MyEmptyPerson:
    pass 
print(MyEmptyPerson)
print(MyEmptyPerson())

# Clase con constructor, funciones y propiedades privadas y públicas
class Person:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"# Propiedad publica
        self.__name = name # Propiedad privada
    def get_name (self):
        return self.__name
    def talk(self):
        print(f"{self.full_name} Está hablando monda")

my_person = Person("Nicolas","Daza")
print(my_person.full_name)
print(my_person.get_name())
my_person.talk()

my_other_person = Person("Armando","Casas","El ruso")
print(my_other_person.full_name)
my_other_person.talk()
my_other_person.full_name = "Hector Garcia (El fadeell)"
print(my_other_person.full_name)

#Se puede variar tipado debil
my_other_person.full_name = 69
print(my_other_person.full_name)
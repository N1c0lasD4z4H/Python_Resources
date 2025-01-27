### Exception Handling ###

numberOne = 5
numbertwo = 1
numbertwo = "1"

#Excepción base: try except
try: 
    print(numberOne+numbertwo)
    print("No se ha producido un error ")
except:
    # Se ejecuta si no se produce una excepcion
    print("Se ha liado")

#Flujo completo de una excepción: try except else finally
try: 
    print(numberOne+numbertwo)
    print("No se ha producido un error ")
except:
    print("Se ha liado")
else:#Opcional
    # Se ejecuta si no se produce una excepcion
    print("La ejecución continua correctamente")
finally:#Opcional
    #Se ejecuta siempre
    print("La ejecución continua")

#Excepciones por tipo
try: 
    print(numberOne+numbertwo)
    print("No se ha producido un error ")
except ValueError:
    print("Se ha producido un error con ValueError")
except TypeError:
    print("Se ha producido un error con TypeError")

# Captura de la información de la excepción
try: 
    print(numberOne+numbertwo)
    print("No se ha producido un error ")
except ValueError as error:
    print(error)
except Exception as exception_error:
    print(exception_error)
######################################
# Operaciones abreviadas para una rapida escritura
# ejemplos de suma y division
######################################

# x = 1
# x += 1
# x = 10/x
# x /= 10

# print(x)

#######################################
# Coversor de kilometros a miles y viceversa
# valor costante: 1 milla = 1.61 Km
#######################################

# kilometers = float(input('ingresar el valor entero o decimal de los Km a calcular = '))
# miles = float(input('ingresar el valor entero o decimal de las millas a calcular = '))
# k = float (1.61)

# miles_to_kilometers = (miles * k)
# kilometers_to_miles = (kilometers / k)

# print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
# print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")


########################################
# estos se usan en dentro de la funcion 
# print ()
# sep = " "   y end = " "
#####################################

print("Hola", "Mundo", sep="")  # sin espacio

print("Hola", "Mundo", sep=", ", end="!\n")
print("Adiós", "Python", sep="--", end=".\n")


############################################
# Creacion de figuras
# Con el uso de los caracteres especiales podemos crear figuras
# en este caso un cuadrado
############################################


print("+" + 10 * "-" + "+")
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")

# Type is a list:

fruits = ['Apple', 'Mango', 'Grapes', 'Cherry']

#print(type(fruits))

# la posicion inicial de la lista es el 0 y la posicion final inicia con -1
#print(fruits[3])
#print(fruits[-1])
#print(fruits[0])
#print(fruits[-4])

# Para imprimir un rango de la lista, entonces imprimiria las posiciones 0, 1, 2 (por eso se indica de 0:3)
print(fruits[0:3])
print(fruits[0], fruits[2])

# Hacer un reverso de la lista 
fruits.reverse()
print(fruits)

# Hacerle mayusculas la posicion 0
print(fruits[0].upper())

# Para add un nuevo string usamos APPEND
fruits.append('Kiwi')
print(fruits)

# Para insertar usamos INSERT
fruits.insert(0, 'Strawberry')
print(fruits)

# Para quitar usamos POP
fruits.pop()
print(fruits)
fruits.pop(0)
print(fruits)

# Otra forma de addicionar un string en la posicion 2
fruits[2]='strawberry'
print(fruits)

# Para realizar un swap
fruits[2], fruits[3] = fruits[3], fruits[2]
print (fruits)

# Listas anidadas
participants= ['Sanjeev', 'Balen', 'Yash', 'Ramesh', ['Harshad', 'Melissa', 'CBos'], 'Chetan', 'Pablo', ['Mark', 'Atif']]
participants[4].insert(1,'vijay')
print(participants)

# Con el metodo "append" se debe usar parentesis y no el sigo "=" ya que con el metodo y funciones requerimos del ingreso de argumentos; no es una variable
participants[7].append('Prateek')
print(participants)
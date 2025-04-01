# Uso de CONDITIONALS, ojo le indicamos que X debe ser un ENTERO con int

x = int(input('Enter the number: '))
if x > 0:
    print('X is positive value.')
elif x == 0:
    print('X is equals to zero.')
else:
    print('X is a negative vlue.')

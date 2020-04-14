#Creada por Pilar Sahonero Diaz
#Calculadora Basica de solo dos datos por Consola
# Se crea las funsiones de suma, resta, multiplicacion, division
def suma():
    a = int(input('Introduce el primer numero '))
    b = int(input('Introduce el segundo numero '))
    return a+b
def resta():
    a = int(input('Introduce el primer numero '))
    b = int(input('Introduce el segundo numero '))
    return a-b
def multiplicacion():
    a = int(input('Introduce el primer numero '))
    b = int(input('Introduce el segundo numero '))
    return a*b
def division():
    a = int(input('Introduce el primer numero '))
    b = int(input('Introduce el segundo numero '))
    if b == 0:
        return 'Error'
    return a/b
sw=True
#creamos el menu 
while sw:
    print('\033[1;32m')
    print('============Menu=========')
    print('1. Suma')
    print('2. Resta')
    print('3. Multiplicacion')
    print('4. Division')
    print('5. Exit')
    print('=========================')
    print('\033[1;34m')
    opcion=int(input('Introduzca una opcion: '))
    if opcion == 1:
        print('\033[3;33m',suma())
    elif opcion == 2:
        print('\033[3;33m',resta())
    elif opcion ==3:
        print('\033[3;33m',multiplicacion())
    elif opcion ==4:
        print('\033[3;33m',division())
    elif opcion == 5:
        print('\033[3;31m Gracias por participar en este menu')
        sw=False
    else:
        print('\033[1;31m Error: No existe esa opcion ')
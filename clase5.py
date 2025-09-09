""" usuario = input('Ingrese nombre de usuario: ')
clave = input('Ingrese la contraseña: ')
alumnos = {}
if usuario == 'admin' and clave == 'uni123':
    while True:
        print('1 - Añadir un alumno a la lista. ')
        print('2 - Ver la lista de alumnos. ')
        print('3 - Salir. ')
        valor = int(input('Ingrese el número de la operación que desea ejecutar: '))
        if valor == 3:
            print('Gracias por utilizar el programa')
            break
        elif valor == 1:
          nombre = input('Ingrese el nombre del alumno: ')
          cursos = int(input('Ingrese la cantidad de cursos: '))
          alumnos[nombre] = cursos
          print('El alumno fue añadido a la lista!')
        elif valor == 2:
            print('Lista de alumnos')
            for nombre,cursos in alumnos.items():
                print(nombre + " - " + str(cursos) + " cursos")
        else:
            print('La opción ingresada no es correcta, vuelva a intentarlo')
else:
    print('usuario o contraseña incorrecto')

 """
""" 
print('Bienvenido al carrito de compras')
carrito = []
while True:
    print('1 - Agregar al carrito. ')
    print('2 - Eliminar del carrito. ')
    print('3 - Terminar compra. ')
    valor = int(input('Ingrese el número de la operación que desea ejecutar: '))
    if valor == 3:
        print('Gracias por utilizar el programa')
        break
    elif valor == 1:
        producto = input('Ingrese el nombre del producto: ')
        carrito.append(producto)
        print('Producto agregado!')
    elif valor == 2:
        producto = input('Ingrese el nombre del producto a eliminar: ')
        if producto in carrito:
            carrito.remove(producto)
        else:
            print('El producto no se encuentra en el carrito')
        print('Producto eliminado!')
    else:
        print('La opción ingresada no es correcta, vuelva a intentarlo')
    print('Productos en el carrito:')
    for producto in carrito:
        print('* ' + producto)
   
    """

def sumar(a,b):
    return a + b
def restar(a,b):
    return a - b
def multiplicar(a,b):
    return a * b
def dividir(a,b):
    if b != 0:
        return a / b
    else:
        return 'No se puede dividir por cero'

def calculadora():
    print('Bienvenido a la calculadora')
    while True:
        print('1 - Sumar. ')
        print('2 - Restar. ')
        print('3 - Multiplicar. ')
        print('4 - Dividir. ')
        print('5 - Salir. ')
        valor = int(input('Ingrese el número de la operación que desea ejecutar: '))
        if valor == 5:
            print('Gracias por utilizar el programa')
            break
        elif valor in [1,2,3,4]:
            a = float(input('Ingrese el primer número: '))
            b = float(input('Ingrese el segundo número: '))
            if valor == 1:
                resultado = sumar(a,b)
                operacion = 'suma'
            elif valor == 2:
                resultado = restar(a,b)
                operacion = 'resta'
            elif valor == 3:
                resultado = multiplicar(a,b)
                operacion = 'multiplicación'
            elif valor == 4:
                resultado = dividir(a,b)
                operacion = 'división'
            print(f'El resultado de la {operacion} es: {resultado}')
        else:
            print('La opción ingresada no es correcta, vuelva a intentarlo')

calculadora()
""" 
Crear un programa para agregar productos a un carrito pero usando los productos de un diccionario
Cada producto que se agregue se debe sumar al total
Si el producto no existe infromarle al usuario
Las opciones del menu son:
1.- Agregar al carrito
2.- Ver carrito
3.- Finalizar compra
4.- Eliminar producto del carrito
Una vez que el usuario finalice la compra, mostrar el total de productos y el valor total y finalizar el programa
 """
""" 
productos = {
    "arroz": 850,
    "fideos": 650,
    "aceite": 1950,
    "azúcar": 870,
    "yerba mate": 3200,
    "café": 2800,
    "leche": 950,
    "huevos": 2200,
    "pan lactal": 1450,
    "mermelada": 1350,
    "galletitas": 1150,
    "harina": 700,
    "jabón en polvo": 2900,
    "detergente": 1100,
    "shampoo": 2700,
    "papel higiénico": 2300,
    "queso cremoso": 4500,
    "carne picada": 4800,
    "manzanas": 1800,
    "lechuga": 1000,
    "papas": 1300
}

carrito = []
total = 0

while True:
    print('''
        ######## BIENVENIDO AL CARRITO DE COMPRAS ########
        1.- Añadir producto al carrito
        2.- Ver carrito
        3.- Eliminar producto del carrito
        4.- Finalizar compra
        ''')
    opcion = input('Ingrese una opción: ')
    if opcion == '1':
        print('Lista de productos disponibles:')
        for producto, precio in productos.items():
            print(f'- {producto.capitalize()}: ${precio}')
        producto_elegido = input('Ingrese el nombre del producto que desea agregar al carrito: ').strip().lower()
        if producto_elegido in productos:
            carrito.append(producto_elegido)
            total += productos[producto_elegido]
            print(f'El producto {producto_elegido.capitalize()} ha sido agregado al carrito.')
        else:
            print('El producto no existe. Por favor, elija un producto de la lista.')
    elif opcion == '2':
        if carrito:
            print('Productos en el carrito:')
            for item in carrito:
                print(f'- {item.capitalize()}: ${productos[item]}')
            print(f'Total parcial: ${total}')
        else:
            print('El carrito está vacío.')
    elif opcion == '3':
        if carrito:
            producto_eliminar = input('Ingrese el nombre del producto que desea eliminar del carrito: ').strip().lower()
            if producto_eliminar in carrito:
                carrito.remove(producto_eliminar)
                total -= productos[producto_eliminar]
                print(f'El producto {producto_eliminar.capitalize()} ha sido eliminado del carrito.')
            else:
                print('El producto no está en el carrito.')
        else:
            print('El carrito está vacío.')
    elif opcion == '4':
        if carrito:
            print('Finalizando compra...')
            print('Productos comprados:')
            for item in carrito:
                print(f'- {item.capitalize()}: ${productos[item]}')
            print(f'Total a pagar: ${total}')
        else:
            print('El carrito está vacío. No hay nada para comprar.')
        print('Gracias por utilizar el programa. ¡Hasta luego!')
        break
    else:
        print('Opción no válida. Por favor, ingrese una opción del 1 al 4.')
         """

import matematicas.aritmetica as aritmetica

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
                resultado = aritmetica.sumar(a,b)
                operacion = 'suma'
            elif valor == 2:
                resultado = aritmetica.restar(a,b)
                operacion = 'resta'
            elif valor == 3:
                resultado = aritmetica.multiplicar(a,b)
                operacion = 'multiplicación'
            elif valor == 4:
                resultado = aritmetica.dividir(a,b)
                operacion = 'división'
            print(f'El resultado de la {operacion} es: {resultado}')
        else:
            print('La opción ingresada no es correcta, vuelva a intentarlo')

calculadora()
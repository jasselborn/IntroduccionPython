# # Laboratorio adicional
#
# Ejercicio 1
# def mostrar_estrella(cantidad):
#     for i in range(0,cantidad):
#         print('*' * (i + 1))
# mostrar_estrella(5)
from importlib.metadata import entry_points


# Ejercicio 2
# def sumar(a,b):
#     return a+b
# print(sumar(4,7))

# Ejercicio 3
# def rango(desde,hasta,intervalo):
#     lista = []
#     for i in range(desde,hasta,intervalo):
#          lista.append(i)
#     return lista
# print(rango(1,10,2))

# Ejercicio 4
# def es_palindromo(lista):
#     es = False
#     for i in lista:
#         if lista[i] == lista[-i -1]:
#             es= True
#         else:
#             es =False
#     return es
#
# lista1 = [1,2,3,3,2,1]
# if (es_palindromo(lista1)):
#     print('es polindromo')
# else:
#     print('no es polindromo ')

# ETAPA 2
#
usuario = input('Ingrese nombre de usuario: ')
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
          # alumno = {}
          nombre = input('Ingrese el nombre del alumno: ')
          cursos = int(input('Ingrese la cantidad de cursos: '))
          alumnos[nombre] = cursos
          print('El alumno fue añadido a la lista!')
        elif valor == 2:
            print('Lista de alumnos')
            # print(alumnos)
            for nombre,cursos in alumnos.items():
                print(nombre + " - " + str(cursos) + " cursos")
        else:
            print('La opción ingresada no es correcta, vuelva a intentarlo')
else:
    print('usuario o contraseña incorrecto')

# Desafio
# Ejercicio 1
# def es_numero(entrada):
#
#     while entrada.isdigit() == False:
#         print("noes nro")
#         entrada = input("Ingresa algo: ")
#     retorno = int(entrada)
#     return retorno
#
# entrada = input("Ingresa algo: ")
#
# es_numero(entrada)

# Ejercicio 1
def area_rectangulo(base,altura):
    return base * altura
print(area_rectangulo(10,30))
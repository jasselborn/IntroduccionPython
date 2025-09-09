# Laboratorio adicional

#Ejercicio 1

# 1
# cadena1 = input('Ingrese cadena uno: ')
# cadena2 = input('Ingrese cadena dos: ')
# if cadena1 == cadena2:
#     print('Ambas cadenas son iguales')
# else:
#     print('Ambas cadenas son distintas')

# 2
# nombre = input('Ingrese nombre de alumno: ')
# if nombre.strip() == '':
#     print('No se permite ingreso vacío')
# else:
#     print('Nombre ingresado correctamente')

# 3
# edad = int(input('Ingrese edad: '))
# if edad >= 18:
#     print('Es mayor de edad')
# else:
#     print('Es menor de edad')


#Ejercicio 2

# 1
# numero = 0
# while numero < 10:
#     print(numero)
#     numero= numero +1

# 2
# nombre = input('Ingrese nombre de alumno: ')
# while True:
#     if nombre.strip() == '':
#         nombre = input('No se permite ingreso vacío, ingrese nombre de alumno nuevamente: ')
#     else:
#         print(f'Saliudos! {nombre}')
#         break

#Ejercicio 3
#1
# nombre = ['Susana','Alejandro','Roberto']
# # nombre[2] = 'Paula'
# nombre.insert(2,'Paula')
# nombre.append('Silvina')
#2
# print(nombre)

#Ejercicio 4
#1
# nombres = ['Agustina','Marisa','Juan','Osvaldo']
# for nombre in nombres:
#     print(nombre)

#Ejercicio 5
#1
# matriz = [[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]
# print('[[3.3, 6.1, 4.0], [4.9, 5.7, 6.4]]')
#
# fila = int(input('Ingrese numero de fila: '))
#
# if fila == 0 or fila == 1:
#     columna = int(input('Ingrese numero de columna: '))
#     if columna ==0 or columna == 1 or columna ==2:
#         print(matriz[fila][columna])
#     else:
#         print('valor de columna fuera del rango')
# else:
#     print('valor de fila fuera del rango')

#Ejercicio 6
# 1
# edad = int(input('Ingrese edad: '))
# if edad >= 18:
#     if edad >= 65:
#         print('Jubilado')
#     else:
#         print('Es mayor con edad laboral')
# else:
#     print('Es menor de edad')


# 2
# m = [ [10,50,5], [20,30,70], [15,45,80] ]
# i = 0
# for f in m:
#     j = 0
#     for c in f:
#         print(f[j])
#         j = j +1
#     i = i +1

#Ejercicio 7
# 1
# print('Bienvenido al sistema de la Agencia TuViaje')
# codigo = input('Ingrese código de paquete: ').upper()
# if codigo.strip() == '':
#     print('No se permite ingreso vacío')
# elif codigo == 'A':
#     print('Paquete A: Cancún 7 noches + aéreos: u$s 1200 por persona.')
# elif codigo == 'B':
#     print('Paquete B: Miami 8 noches + aéreos + alquiler de auto: u$s 1500 por persona.')
# elif codigo == 'C':
#     print('Paquete C: Bariloche 10 noches + aéreos + excursiones: u$s 1300 por persona.')
# elif codigo == 'D':
#     print('Paquete D: Río de Janeiro 10 noches + aéreos + excursiones: u$s 1400 por persona.')
# else:
#     print('El código ingresado es incorrecto')

#
# print('Bienvenido al sistema de la Agencia TuViaje')
#
# while True:
#     codigo = input('Ingrese código de paquete, para finalizar ingrese X: ').upper()
#     if codigo.strip() == '':
#         print('No se permite ingreso vacío')
#     elif codigo == 'A':
#         print('Paquete A: Cancún 7 noches + aéreos: u$s 1200 por persona.')
#     elif codigo == 'B':
#         print('Paquete B: Miami 8 noches + aéreos + alquiler de auto: u$s 1500 por persona.')
#     elif codigo == 'C':
#         print('Paquete C: Bariloche 10 noches + aéreos + excursiones: u$s 1300 por persona.')
#     elif codigo == 'D':
#         print('Paquete D: Río de Janeiro 10 noches + aéreos + excursiones: u$s 1400 por persona.')
#     elif codigo == 'X':
#         break
#     else:
#         print('El código ingresado es incorrecto')
#
# print('Gracias por utilizar nuestro sistema')


# ETAPA 2
#
# usuario = input('Ingrese nombre de usuario: ')
# clave = input('Ingrese la contraseña: ')
# alumnos = []
# if usuario == 'admin' and clave == 'uni123':
#     while True:
#         print('1 - Añadir un alumno a la lista. ')
#         print('2 - Ver la lista de alumnos. ')
#         print('3 - Salir. ')
#         valor = int(input('Ingrese el número de la operación que desea ejecutar: '))
#         if valor == 3:
#             print('Gracias por utilizar el programa')
#             break
#         elif valor == 1:
#           alumno = []
#           nombre = input('Ingrese el nombre del alumno: ')
#           cursos = int(input('Ingrese la cantidad de cursos: '))
#           alumno.append(nombre)
#           alumno.append(cursos)
#           alumnos.append(alumno)
#           print('El alumno fue añadido a la lista!')
#         elif valor == 2:
#             print('Lista de alumnos')
#             for alumno in alumnos:
#                 print(alumno[0].capitalize(),'-', alumno[1], 'cursos')
#         else:
#             print('La opción ingresada no es correcta, vuelva a intentarlo')
# else:
#     print('usuario o contraseña incorrecto')


#####################
#     Desafios
#####################

# Ejercicio 1
# nota = int(input('Ingrese nota: '))
# if nota == 10:
#     print('Excelente')
# elif 7 <= nota <= 9:
#     print('Muy Bien')
# elif 4 <= nota <= 6:
#     print('Bien')
# else:
#     print('Mal')

# Ejercicio 2
# rol = input('Ingrese su rol en la institución (admin o profesor): ')
# if rol == 'admin' or rol == 'profesor':
#     clave = input('Ingrese su clave: ')
#     if clave == '1234':
#         nombre = input('Ingrese su nombre: ')
#         if  nombre.strip() != '':
#             print(f'Bienvenido {nombre}!')
#     else:
#         print('Clave erronea')
# else:
#     print('Rol erroneo')

# Ejercicio 3
# sueldo1 = 300 * 6
# sueldo2 = 500 * 4
# sueldo3 = 700 * 2
# sueldopromedio = (sueldo1 + sueldo2 + sueldo3) / 12
# if sueldopromedio >= 900:
#     print('sueldo mejor de lo normal')
# elif 300 <= sueldopromedio <= 900:
#     print('sueldo nomal')
# else:
#     print('sueldo bajo')
#
# print(sueldopromedio)

# Ejercicio 4
# dato = int(input('Ingrese año: '))
# if dato%4 ==0:
#     print('es bisiesto')
# elif dato%4 ==0 and dato%100 !=0:
#     print('no es bisiesto')
# else:
#     print('es bisiesto')

# Ejercicio 5
# cant = int(input('ingrese cantidad: '))
# nombres = []
# for i in range(0,cant):
#     nombre = input(f'Ingrese nombre nro {i+1}: ')
#     nombres.append(nombre)
# print(nombres)
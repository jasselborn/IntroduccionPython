# # Laboratorio adicional
#
# Ejercicio 1
import tkinter
from time import sleep


# def rango(a,b,i):
#     lista = []
#     for n in range(a,b,i):
#         lista.append(n)
#     return lista
# print(rango(1,20,3))

# Ejercicio 2
# for n in range(0,10):
#     sleep(1)
#     print(n)

# Ejercicio 3
# import random
# print('Menu Ejercicio 3')
# print('1- Tirar dado')
# print('2- Salir')
# opcion = int(input('Ingrese opción: '))
#
# while True:
#     opcion = int(input('Ingrese opción: '))
#     if opcion == 1:
#         dado = random.randint(1,6)
#         print(f'Ha salido el nro {dado}')
#     elif opcion == 2:
#         print('Gracias por utilizar el programa')
#         break
#     else:
#         print('Usted ha ingresado una opcion incorrecta')
#         continue


# if opcion == 2:
#     print('Gracias por utilizar el programa')
# else:
#     print('Usted ha ingresado una opcion incorrecta')
    # elif opcion == 2:
    #     print('Gracias por utilizar el programa')
    #     break
    # else:
    #     print('Usted ha ingresado una opcion incorrecta')
    #     continue

# Ejercicio 4

# import tkinter as tk
# multi = 0
# def multiplicar():
#     resultado = int(caja1.get()) * int(caja2.get())
#     label3.config(text=resultado)
#     print(resultado)
#
# ventana = tk.Tk()
# ventana.config(width=300,height=200)
# ventana.title = 'Primer ventana'
#
# label1 = tk.Label(text = 'Valor nro 1')
# label1.place(x=10,y=20)
# caja1 = tk.Entry()
# caja1.place(x= 80,y=20,width=50)
#
# label2 = tk.Label(text='Valor nro 2')
# label2.place(x=10,y=40)
# caja2 = tk.Entry()
# caja2.place(x= 80,y=40,width=50)
#
# boton = tk.Button(text='Multiplicar', command=multiplicar)
# boton.place(x=10,y=70,width=120)
#
# label3 = tk.Label(text='Resultado')
# label3.place(x=10,y=100)
#
# ventana.mainloop()


# ETAPA 4
#
import tkinter as tk

alumnos = {}

def login():
    # print('entro')
    if cUsuario.get() == 'admin' and cClave.get() == 'uni123':
        # print('Acceso aprovado')
        btnAgregar.config(state=tkinter.NORMAL)
        btnListar.config(state=tkinter.NORMAL)

def agregar():
    # print('Ágregar')
    alumnos[cAlumno.get()] = cCursos.get()
    print(cAlumno.get(), '-',cCursos.get())

def listar():
    # print('Listar')
    for nombre,cursos in alumnos.items():
        print(nombre + " - " + str(cursos) + " cursos")

def salir():
    ventana.destroy()

ventana = tk.Tk()
ventana.geometry("400x300")
# ventana.config(width=700,height=700)
ventana.title = 'Primer ventana'

lblUsuario = tk.Label(text = 'Usuario')
lblUsuario.place(x=10,y=20)
cUsuario = tk.Entry()
cUsuario.place(x= 80,y=20,width=100)

lblClave = tk.Label(text='Clave')
lblClave.place(x=10,y=40)
cClave = tk.Entry()
cClave.place(x= 80,y=40,width=100)

btnLogin = tk.Button(text='Login', command=login)
btnLogin.place(x=10,y=70,width=170)

label3 = tk.Label(text='Ingreso de alumnos a lista')
label3.place(x=10,y=100)

lblAlumno = tk.Label(text = 'Alumno')
lblAlumno.place(x=10,y=120)
cAlumno = tk.Entry()
cAlumno.place(x= 80,y=120,width=100)

lblCursos = tk.Label(text='Cursos')
lblCursos.place(x=10,y=140)
cCursos = tk.Entry()
cCursos.place(x= 80,y=140,width=100)

btnAgregar = tk.Button(text='Agregar', command=agregar)
btnAgregar.place(x=10,y=170,width=70)
btnAgregar.config(state=tkinter.DISABLED)
btnListar = tk.Button(text='Listar', command=listar)
btnListar.place(x=100,y=170,width=70)
btnListar.config(state=tkinter.DISABLED)
btnSalir = tk.Button(text='Salir', command=salir)
btnSalir.place(x=10,y=210,width=170)

# listbox = tk.Listbox()
# listbox.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
# # listbox.pack()
# listbox.insert(0, "Opción 1")
# listbox.insert(1, "Opción 2")
# items = ("Python", "C", "C++", "Java")
# listbox.insert(tk.END, *items) # tk.END añade al final

# Añadir elementos a la lista usando insert()
# elementos_para_anadir = ["Elemento 1", "Elemento 2", "Elemento 3", "Elemento 4"]
# for i, elemento in enumerate(elementos_para_anadir):
#     lista_elementos.insert(tk.END, elemento) # Añade al final

ventana.mainloop()
""" import random

loteria = [] # 6 num aleatorios
carton = [] # 6 num a adivinar, con 5 ya hay premio
acertados = [] # aqui para ganar deberian haber 5 num

def comprar_numeros():
    contador = 0
    while len(contador) < 6:
        num = int(input('Ingrese un numero del 1 al 40: '))
        while num.isdecimal() == False:
            print('Ingrese solo numeros')
            num = input('Ingrese un numero del 1 al 40: ')
    int(num)
    if num < 1 or num > 40:
        print('Ingrese un numero del 1 al 40: ')
    elif num in carton:
        print('El numero ya fue ingresado, ingrese otro: ')
    else:
        carton.append(num)
        contador += 1
    carton.sort()
    print(f'Su carton es: {carton}')
    return carton


def sortear_numeros():
    while len(loteria) < 6:
        num = random.randint(1,40)
        if num not in loteria:
            loteria.append(num)
    print(f'Los numeros sorteados son: {loteria}')
    #return loteria


def verificar_resultado():
    for num in carton:
        if num in loteria:
            acertados.append(num)
    print(f'Los numeros acertados son: {acertados}')
    if len(acertados) >= 5:
        print('Felicidades, ha ganado!')
    else:
        print('Lo siento, no ha ganado.')
    return acertados
 """
""" comprar_numeros() 
sortear_numeros()
verificar_resultado() """

""" Calcular promedio de notas de alumno
El usuario debe indicar la cantidad de notas a evaluar
En base a las notas indicadas, calcular el promedio
las notas se reciben como argumento (lista) en una función
 """   

def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio

""" def calcular_promedio2(notas):
    total = 0
    for nota in notas:
        total += nota
    promedio = total / len(notas)
    return promedio

notas = []
cantidad = int(input('Ingrese la cantidad de notas a evaluar: '))

while cantidad > 0:
    nota = float(input(f'Ingrese la nota: {len(notas)+1}: '))
    notas.append(nota)
    cantidad -= 1


promedio = calcular_promedio2(notas)
print(f'El promedio de las notas es: {promedio}')  """

def main():
    notas = []
    cantidad = int(input('Ingrese la cantidad de notas a evaluar: '))

    while cantidad > 0:
        nota = float(input(f'Ingrese la nota: {len(notas)+1}: '))
        notas.append(nota)
        cantidad -= 1


    promedio = calcular_promedio(notas)
    print(f'El promedio de las notas es: {promedio}')
    return promedio

if __name__ == '__main__':
    main()




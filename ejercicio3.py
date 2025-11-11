''' 
Parte 3: Programacion Dinamica
Problema: Mochila

Un ladrón tiene una mochila con capacidad de peso W. Hay n objetos, cada uno con un 
peso wᵢ y un valor vᵢ. El objetivo es seleccionar un subconjunto de objetos que maximice 
el valor total sin superar la capacidad de la mochila. 

'''

#funciones

def inicializarMatriz(m, capacidad , f):
    for i in range (f):
        m.append([])

        for j in range(capacidad + 1):
             m[i].append(0)
    return m

def mostrarMatriz(m, capacidad, f):
    print ("\n\n")
    for i in range (f):
        print(m[i])

#main

capacidad = int(input("Ingrese la capacidad de la mochila: "))
#lista [peso: valor]
objetos = [[6, 30], [3, 14], [4, 16], [2, 10], [3, 3], [2,5]]
#matriz de objetos
#[6, 30]
#[3, 14]
#[4, 16]
#[2, 10]
#[3,  3]
#[2,  5]

valorTotal = 0
m = []

inicializarMatriz(m,capacidad, len(objetos))

def rellenarMatriz(m, capacidad, objetos):
    for i in range (len(objetos)):
        for j in range (capacidad + 1):
            peso = objetos[i][0]
            valor = objetos[i][1]
            
            if peso <= j:
                # si entra, elijo entre incluirlo o no incluirlo
                if i > 0:
                    m[i][j] = max(valor + m[i - 1][j - peso], m[i - 1][j])
                else:
                    m[i][j] = valor
            else:
                # si no entra, copio el valor de la fila anterior (si existe)
                if i > 0:
                    m[i][j] = m[i - 1][j]
                else:
                    m[i][j] = 0

    return m
             

matrizResultante = rellenarMatriz(m, capacidad, objetos)
if capacidad < 1:
    print("La capacidad de la mochila tiene que ser al menos mayor que cero")
else:
    mostrarMatriz(matrizResultante, capacidad, len(objetos))
    print("\nValor máximo que se puede llevar en la mochila:", matrizResultante[-1][-1])




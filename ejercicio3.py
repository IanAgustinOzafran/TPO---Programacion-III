#funciones

def inicializarMatriz(m, c, f):
    for i in range (f):
        m.append([])

        for j in range(c):
             m[i].append(0)
    return m

def mostrarMatriz(m, c, f):
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
        for j in range (capacidad):
            if (len(objetos) == 1 and i[0] > capacidad): # si es solo un objeto y no entra en la mochila, no gano nada
                m[i][j] = 0
            elif (len(objetos) == 1 and i[0] < capacidad):  # si es solo un objeto y entra en la mochila gano su valor
                m[i][j] = objetos[i][1]
            if objetos[i][0] <= j + 1:  # si es mas de un objeto y entra, elige el valor mas grande
                m[i][j] = max(objetos[i][1] + (m[i-1][j-objetos[i][0]] if j-objetos[i][0] >= 0 else 0), m[i-1][j])
            else:  # si es mas de un objeto y la suma de sus valores no entra en la mochila, agarra el de arriba
                m[i][j] = m[i-1][j] #no entra, copia el de arriba

    return m
             

matrizResultante = rellenarMatriz(m, capacidad, objetos)
if capacidad < 1:
    print("La capacidad de la mochila tiene que ser al menos mayor que cero")
else:
    mostrarMatriz(matrizResultante, capacidad, len(objetos))
    print("Valor máximo que se puede llevar:", matrizResultante[-1][-1])


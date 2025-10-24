'''
Parte 4: Grafos: Floyd - Warshall

Consigna: Cada grupo debera inventar un problema de la vida real que pueda modelarse
con un grafo ponderado y resolverlo utilizando el algorito de Floyd - Warshall para obtener las
distancias mas cortas entre todos los nodos pares.

Etapa 1: Creacion del problema

-La empresa Rappi quiere optimizar las rutas de sus repartidores dentro de una ciudad.
-La ciudad esta dividida en zonas conectadas por calles de distintas distancias.
-No todas las zonas estan conectadas directamente, y algunas rutas son mas rapidas debido al trafico.

La empresa necesita saber la distancia mas corta entre todas las zonas para:
    -Caluclar el tiempo estimado de entrega entre restaurantes, depositos y clientes.
    -Asignar rutas optimas a los repartidores segun la ubicacion del pedido.
    -Reducir costo de combustible y tiempos muertos.

Para ello, se modela la ciudad como un grafo ponderado dirigido, donde:
    -Cada nodo representa una zona (por ejemplo: Restaurante, Depósito, Cliente, etc.).
    -Cada arista representa una calle o conexión directa con su distancia en kilómetros o tiempo promedio de viaje.
    -Si no hay conexión directa, el valor es ∞ (infinito).

'''

import math

zonas = ["Restaurante", "Deposito", "Bodegon", "Tienda", "Cliente A", "Cliente B"]

inf = math.inf #importamos infinito

grafo = [
    [0,   4,   inf, 2,   inf, inf],  # Restaurante
    [inf, 0,   5,   inf, 10,  inf],  # Depósito
    [inf, inf, 0,   3,   inf,  7 ],  # Bodegón
    [inf, inf, inf, 0,   6,   inf],  # Tienda
    [inf, inf, inf, inf, 0,   2  ],  # Cliente A
    [inf, inf, inf, inf, inf, 0  ]   # Cliente B
]

def inicializarMatriz(m, c, f):
    for i in range (f):
        m.append([])

        for j in range (c):
            m[i].append(0)

    return m

def mostrarMatriz (m):
    print ("\n\n")
    for fila in m:
        print(fila)

def floyd (grafo):
    dist = [fila[:] for fila in grafo]
    n=len(dist)

    for k in range (n):
        for i in range (n):
            for j in range (n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist

# --- PROGRAMA PRINCIPAL ---

print("Matriz de distancias directas:")
mostrarMatriz(grafo)

resultado = floyd(grafo)

print("\nDistancias más cortas entre todas las zonas:")
mostrarMatriz(resultado)


print("\nDistancia mínima entre zonas:")
for i in range(len(zonas)):
    for j in range(len(zonas)):
        if i != j:
            print(f"De {zonas[i]} a {zonas[j]}: {resultado[i][j]}")




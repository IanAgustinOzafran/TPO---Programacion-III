''' 
Parte 1: Divide & Conquista
Problema: Par de puntos mas cercano

En un plano bidimensional se tienen n puntos con coordenadas (x, y). El objetivo es 
encontrar el par de puntos que estén a la menor distancia posible entre sí. 

'''
import math 

def distancia(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1]) #calcula la distancia entre los puntos x, y 

# Versión para pocos puntos
def fuerza_bruta(puntos,n):

    menor_dist = float('inf')#infinito 
    par = (None, None)
    for i in range(n):
        for j in range(i + 1, n):
            d = distancia(puntos[i], puntos[j])
            if d < menor_dist:
                menor_dist = d
                par = (puntos[i], puntos[j])
    return par[0], par[1], menor_dist

# Función principal recursiva
def divideConquista(puntos):
    n = len(puntos)
    if n <= 3:
        return fuerza_bruta(puntos,n)

    mid = n // 2
    mitad_izq = puntos[:mid]
    mitad_der = puntos[mid:]

    # Llamadas recursivas
    p1_izq, p2_izq, distancia_izq = divideConquista(mitad_izq)
    p1_der, p2_der, distancia_der = divideConquista(mitad_der)

    # Tomamos la menor distancia de ambas mitades
    if distancia_izq < distancia_der:
        d_min = distancia_izq
        par_min = (p1_izq, p2_izq)
    else:
        d_min = distancia_der
        par_min = (p1_der, p2_der)

   
   #Busco el par más cercano del medio
    x_medio = puntos[mid][0]
    tira = [p for p in puntos if abs(p[0] - x_medio) < d_min]
    tira.sort(key=lambda p: p[1]) #ordeno por Y

    for i in range(len(tira)):
        for j in range(i + 1, len(tira)):
            if (tira[j][1] - tira[i][1]) >= d_min:
                break
            d = distancia(tira[i], tira[j])
            if d < d_min:
                d_min = d
                par_min = (tira[i], tira[j])

    return par_min[0], par_min[1], d_min


def puntos_mas_cercanos_dc(puntos):
    puntos.sort(key=lambda p: p[0])#ordena por los puntos x 
    return divideConquista(puntos)

# Ejemplo de uso
puntos = [(223, 3), (1, 30), (40, 50), (5, 200), (12, 10), (343, 4)]
p1, p2, d = fuerza_bruta(puntos, len(puntos))
a1, a2, dis = divideConquista(puntos)

print("\n=== Método fuerza bruta ===")
print(f"Puntos más cercanos: {p1} y {p2}. Con distancia: {d:.2f}")

print("\n=== Método Divide y Conquista===")
print(f"Puntos más cercanos: {a1} y {a2}. Con distancia: {dis:.2f}")


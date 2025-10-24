''' 
Parte 2: Greedy
Problema: Seleccion de actividades

Un estudiante tiene n actividades, cada una con un horario de inicio y fin.
El objetivo es seleccionar la maxima cantidad de actividades que no se superpongan.

actividades: (inicio: fin)

ejemplo:
[[0,4], [2,8], [3,9], [5, 6] [7, 10], [10, 15]]

tareas ordenadas de menor a mayor por finalizacion
[[0, 4], [5, 6], [2, 8], [3, 9], [7, 10], [10, 15]]

resultado:
(0,4), (5,6), (7,10), (10,15)

'''

#funciones

def maximizarTareas(tareas):
    tareasOrdenadas = ordenarXFinalizacion(tareas)
    seleccionadas=[]
    nuevoFin = -1
    for inicio, fin in tareasOrdenadas:
        if inicio >= nuevoFin:
            seleccionadas.append((inicio, fin))
            nuevoFin = fin #se actualiza al nuevo fin de la ultima agregada
    return seleccionadas

def ordenarXFinalizacion(tareas):
    return sorted(tareas, key=lambda x: x[1]) #ordena las tareas por finalizacion
        

#main

tareas1 = [[0, 4], [5, 6], [2, 8], [3, 9], [7, 10], [10, 15]]
tareas2 = [[2, 5], [1, 3], [8, 10],[5, 9], [4, 7], [1, 8]]

resultado1 = maximizarTareas(tareas1)
resultado2 = maximizarTareas(tareas2)

print("Actividades seleccionadas: ",resultado1)
print("Actividades seleccionadas: ",resultado2)





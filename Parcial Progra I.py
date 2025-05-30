from Funciones import cargar_matriz_notas, porcentaje_aprobados, mejor_promedio, buscar_nota
"""PARTE 2 - EJERCICIO PRÁCTICO
Contexto: Una institución educativa necesita registrar las notas de sus
alumnos en distintos exámenes. Cada fila de una matriz representa un
alumno y cada columna un examen.
Requisitos Generales para Todos los Puntos:
- Se deben modularizar todas las operaciones. No se permite resolver
todo en el main.
- No está permitido el uso de funciones propias de Python como max,
min, sum, enumerate, etc.
- La validación debe hacerse en la función de carga, verificando que
cada nota sea un número entero entre 1 y 10.
- Se debe implementar un menú con opciones para ejecutar cada punto
de forma separada.
- Usar estructuras adecuadas, acumuladores, contadores y recorrido
doble.
- Nombrar las funciones tal como se indican a continuación.

1 - Función cargar_matriz_notas(): Recibe dos enteros n y m y permite
cargar n x m notas válidas entre 1 y 10 inclusive. La validación debe
hacerse dentro de esta función.

2 - Función porcentaje_aprobados(): Calcula el porcentaje de
exámenes aprobados (nota ≥ 6) por cada alumno y muestra un resumen
individual. Usar contadores y acumuladores.

3 - Función mejor_promedio(): Calcula el promedio de cada alumno y
determina cuál tiene el mejor promedio. Retorna el índice del alumno y
el valor del promedio.

4 - Función buscar_nota(): Recibe la matriz y una nota buscada, y
retorna una lista con todas las posiciones (fila, columna) donde aparece
esa nota exacta."""

matriz_notas = []

#Menu Principal
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1 - Cargar matriz de notas")
    print("2 - Mostrar porcentaje de exámenes aprobados por alumno")
    print("3 - Mostrar el alumno con mejor promedio")
    print("4 - Buscar una nota entre los alumnos")
    print("0 - Salir")

    opcion = input("Elija una opción (0-4): ")

    match opcion:
        case "1":
            matriz_notas = cargar_matriz_notas()
        case "2":
            if matriz_notas:
                porcentaje_aprobados(matriz_notas)
            else:
                print("Primero debe cargar las notas de los alumnos!")
        case "3":
            if matriz_notas:
                mejor_promedio(matriz_notas)
            else:
                print("Primero debe cargar las notas de los alumnos!")          
        case "4":
            if matriz_notas:
                buscar_nota(matriz_notas)
            else:
                print("Primero debe cargar las notas de los alumnos!")
            
        case "0":
            print("\nHasta luego! (Terminando Programa)")
            break
        case _:
            print("Opción inválida. Ingrese una opcion (0-4).")

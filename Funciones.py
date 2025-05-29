def cargar_matriz_notas():

    """Pregunta al usuario cuántos alumnos y exámenes hay validando que sean numeros enteros.
    Después, carga las notas en una matriz donde cantidad de alumnos son filas y cantidad de examenes
    las columnas, asegurándose de que cada nota sea un número entre 1 y 10.
    Devuelve la matriz con todas las notas cargadas."""

    #defino primero las variables, dentro de la funcion
    cant_Alumnos = 0 #harcodeo un 2 para probar, pero la variable iniciaria en 0
    cant_Examenes = 0 #harcodeo un 2 para probar, pero la variable iniciaria en 0

    while cant_Alumnos <= 0: #al no haber alumnos cargados, entro al bucle
        entrada = input("Ingrese la cantidad de alumnos: ")
        if entrada.isdigit():
            cant_Alumnos = int(entrada) #convierto el str en un int 
            if cant_Alumnos <= 0:
                print("Debe ser mayor que cero.") #si carga un negativo o 0, tira error
        else:
            print("Debe ingresar un número entero.") #si carga algo que no sea un numero, tira error

    while cant_Examenes <= 0: #al no haber alumnos cargados, entro al bucle
        entrada = input("Ingrese la cantidad de exámenes: ")
        if entrada.isdigit():
            cant_Examenes = int(entrada) #convierto el str en un int 
            if cant_Examenes <= 0:
                print("Debe ser mayor que cero.") #si carga un negativo o 0, tira error
        else:
            print("Debe ingresar un número entero.") #al no haber alumnos cargados, entro al bucle

    matriz_de_Alumnos = [] #matriz vacia
    for i in range(cant_Alumnos): #defino las filas con el numero de alumnos
        fila = []
        print(f"\nIngrese las notas del Alumno {i+1}:") #i+1 porque arrancaria en 0 sino
        for j in range(cant_Examenes):
            nota_valida = False #bandera para verificar si ingreso una nota valida
            while not nota_valida:
                nota = input(f"Ingrese la nota del examen {j+1} (1 a 10): ") #j+1 porque arrancaria en 0 sino
                if nota.isdigit(): #valido que sea un numero y despues lo paso a int
                    nota = int(nota)
                    if 1 <= nota <= 10: #si entra, valido que esté entre 1 inclusive y 10 inclusive 
                        fila.append(nota)
                        nota_valida = True #cambia la bandera para que corte y pase al siguiente examen a cargar
                    else:
                        print("La nota debe estar entre 1 y 10.")
                else:
                    print("Debe ingresar un número entero.")
        matriz_de_Alumnos.append(fila) #agrego la fila del alumno con sus correspondientes a la matriz

    return matriz_de_Alumnos #devuelvo la matriz armada


def porcentaje_aprobados(matriz_notas):
    """Recibe la matriz creada y la recorre para controlar que porcentaje de examenes aprobo cada alumno.
    Usando como referencia la cantidad de examenes que se tomaron a los alumnos y se toma en cuenta que la 
    nota para aprobar sea igual o mayor que 6.
    Se suman las notas de cada alumno y saca un promedio de aprobacion por cada uno, luego se muestra en pantalla
    """

    for i in range(len(matriz_notas)): #recorro cada fila (alumnos) 
        contador_examenes_aprobados = 0 #inicio un acumulador para el alumno
        total_examenes = len(matriz_notas[i]) #total de examanes indicados por la cant de columnas de la matriz 
        
        for j in range(total_examenes): #recorro cada nota del alumno
            if matriz_notas[i][j] >= 6:
                contador_examenes_aprobados += 1 #si la nota es mayor o igual a 6, se aumenta al contador para promediarlo
        
        # Calcula el porcentaje de exámenes aprobados
        porcentaje = (contador_examenes_aprobados * 100) / total_examenes

        # Muestra el resultado para este alumno
        print(f"El Alumno {i+1} Aprobó {contador_examenes_aprobados} de {total_examenes} exámenes. "
              f"Su porcentaje de aprobación es: {porcentaje:.2f}%")


porcentaje_aprobados(cargar_matriz_notas())
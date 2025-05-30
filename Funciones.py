def cargar_matriz_notas():

    """Pregunta al usuario cuántos alumnos y exámenes hay validando que sean numeros enteros.
    Después, carga las notas en una matriz donde cantidad de alumnos son filas y cantidad de examenes
    las columnas, asegurándose de que cada nota sea un número entre 1 y 10.
    Devuelve la matriz con todas las notas cargadas."""

    #defino primero las variables, dentro de la funcion
    cant_Alumnos = 0 #harcodeo un 2 para probar, pero la variable iniciaria en 0
    cant_Examenes = 0 #harcodeo un 2 para probar, pero la variable iniciaria en 0

    while cant_Alumnos <= 0: #al no haber alumnos cargados, entro al bucle
        entrada = input("Ingrese la cantidad de alumnos: ") #se pide al usuario los alumnos
        if entrada.isdigit(): #verifico si se ingresa un numero entero
            cant_Alumnos = int(entrada) #convierto el str en un int 
            if cant_Alumnos <= 0:
                print("Error. La cantidad debe ser mayor que cero.") #si carga un negativo o 0, tira error
        else:
            print("Error. Debe ingresar un número entero.") #si carga algo que no sea un numero, tira error

    while cant_Examenes <= 0: #al no haber alumnos cargados, entro al bucle
        entrada = input("Ingrese la cantidad de exámenes: ")#se pide al usuario los alumnos
        if entrada.isdigit(): #verifico si se ingresa un numero entero
            cant_Examenes = int(entrada) #convierto el str en un int 
            if cant_Examenes <= 0:
                print("Error. La cantidad debe ser mayor que cero.") #si carga un negativo o 0, tira error
        else:
            print("Error. Debe ingresar un número entero.") #al no haber alumnos cargados, entro al bucle

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
        
        for j in range(total_examenes): #recorro cada columna (examenes del alumno)
            if matriz_notas[i][j] >= 6: #verifico si el la nota de ese alumno, en ese examen es igual o mayor a 6
                contador_examenes_aprobados += 1 #si la nota es mayor o igual a 6, se aumenta al contador para promediarlo
        
        # Calcula el porcentaje de exámenes aprobados del alumno
        porcentaje = (contador_examenes_aprobados * 100) / total_examenes 

        
        # Muestra el resultado para este alumno
        print(f"El Alumno {i+1} Aprobó {contador_examenes_aprobados} de {total_examenes} exámenes. "
              f"Su porcentaje de aprobación es: {porcentaje:.2f}%") #agrego el .2f para mostrar unicamente 2 decimales


#llamo a la funcion para ver los aprobados y le cargo como parametro la matriz que devuelve la funcion de carga
#porcentaje_aprobados(cargar_matriz_notas()) 


def mejor_promedio(matriz_notas):
    """Recibe la matriz de alumnos, declara variables que va a usar para guardar al alumno y su correspondiente promedio
    Recorre los examenes que tuvo alumno por alumno y luego va acumulando esas notas, divide la suma por la cantidad de columnas (examenes)
    que recorrió, y luego compara ese resultado con el mejor promedio encontrado hasta el momento (primera vez vacio)
    Si es mayor, guarda el indice de alumno y el total de su promedio en las variables declaradas al principio.
    Al terminar muestra el ultimo mejor promedio encontrado y el indice del alumno al que pertenece"""
    mejor_promedio = 0
    alumno_mejor_promedio = 0

    for i in range(len(matriz_notas)):  # Recorremos fila por fila (alumnos)
        suma_de_notas = 0 #inicio el acumulador
        for j in range(len(matriz_notas[i])):  #sumamos todas las notas del alumno i
            suma_de_notas += matriz_notas[i][j] #sumo la nota correspondiente al alumno i en el examen j
        promedio_alumno = suma_de_notas / len(matriz_notas[i]) #divido entre el largo de columnas (examenes)

        if promedio_alumno > mejor_promedio: #comparo el mejor promedio, entra si en esta iteración el promedio del primer recorrido es mayor al guardado
            mejor_promedio = promedio_alumno #reemplazo el valor del nuevo mejor promedio con el encontrado
            alumno_mejor_promedio = i + 1 #guardo el indice del alumno que tenga el mejor promedio, sumo +1 ára que sea correcto al imprimir
    
    print(f"el alumno {alumno_mejor_promedio} tuvo el mejor promedio y fue: {mejor_promedio}")


def buscar_nota(matriz_notas):
    """Busca una nota específca en la matriz de los alumnos.
        Pide al usuario que nota quiere buscar, validando que sea numero y que este entre 1 y 10 inclusive.
        Recorre las notas y si encuentra una coincidencia guarda el alumno y en que examen saco la nota en una lista auxiliar.
        Recorre la lista auxiliar que se formó y muestra al/los alumnos y en que examen se sacaron la nota a buscar
        Si no hay coincidencias indica que no se encontró la nota a buscar"""
    posicion_nota_encontrada = []  # Lista para guardar la posicion del alumno
    
    while True: #creo un bucle para preguntar y encontrar una nota a buscar valida
        nota_buscada = input("Ingrese la nota que desea buscar (1-10): ")
        if nota_buscada.isdigit(): # verifico si se ingresa un numero entero
            nota_buscada = int(nota_buscada) #convierto el str en un int 
            if 1 <= nota_buscada <= 10: #si entra, valido que la nota a buscar este entre 1 inclusive y 10 inclusive 
                break
            else:
                print("La nota debe estar entre 1 y 10.") #si es menor que 1 o mayor que 10 indico el error
            
        else:
            print("Error. Debe ingresar un número entero.") # si carga algo que no sea un numero, tira error

    for i in range(len(matriz_notas)): #recorro los alumnos
        for j in range(len(matriz_notas[i])): #recorro los examenes
            if matriz_notas[i][j] == nota_buscada: #si en numero de examen del alumno se encuentra la nota a buscar, entro
                posicion_nota_encontrada.append([i, j])  # Guardamos en la lista la fila (alumno) y la columna (examen)

    if len(posicion_nota_encontrada) == 0: #si la lista creada no tiene indices (alumnos cargados), significa que no encontro coincidencias
        print(f"No se encontró la nota {nota_buscada} entre los examenes de los alumnos.")
    else:
        print(f"La nota {nota_buscada} se encontró en los siguientes examenes:") #muestro de nuevo la nota ingresada por el usuario
        for posicion_alumno in posicion_nota_encontrada: #recorro la lista de los alumnos y notas encontradas
            print(f"En el Examen {posicion_alumno[1]+1} del Alumno {posicion_alumno[0]+1}") #muestro los alumnos y sus notas encontradas
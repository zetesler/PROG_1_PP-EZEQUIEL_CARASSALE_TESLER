
# ******************* FUNCIONES DE VALIDACIÓN DE DATOS ****************************************************


def validar_numero_entero(texto: str)->bool:
    """
    Verifica si un texto ingresado por el usuario es un número entero positivo.
    :FUNCIÓN: Usa el código ASCII de cada carácter (48 a 57 son los dígitos 0 a 9).
    :PARAM texto: String ingresado por el usuario.
    :RETURN: True si todos los caracteres son dígitos. False en caso contrario.
    """
    if len(texto) == 0:
        return False
    else:
        for caracter in texto:
            codigo = ord(caracter)
            if codigo < 48 or codigo > 57: # los números del 48 a 57 en código ASCII representan caracteres numéricos.
                return False
        return True
    

def validar_legajo(legajo: str)->bool:
    """
    Valida que el legajo ingresado contenga solo números.
    :FUNCIÓN: Usa el código ASCII de cada carácter (48 a 57 son los dígitos 0 a 9).
    :PARAM legajo: String ingresado por el usuario, que representa el número de legajo del estudiante.
    :RETURN: True si el texto contiene solo números. False en caso contrario.
    """
    return validar_numero_entero(legajo)


def validar_nombre_y_apellido(nombre_y_apellido: str)->bool:
    """
    Valida que el texto contenga solo letras y espacios.
    :FUNCIÓN: Usa el código ASCII de cada carácter (65-90 mayúsculas, 97-122 minúsculas, 32 espacio).
    :PARAM texto: String ingresado por el usuario, que representa el nombre y apellido del estudiante.
    :RETURN: True si el texto contiene solo letras y espacios. False en caso contrario.
    """
    if len(nombre_y_apellido) == 0:
        return False

    for caracter in nombre_y_apellido:
        codigo = ord(caracter)

        es_mayuscula = codigo >= 65 and codigo <= 90
        es_minuscula = codigo >= 97 and codigo <= 122
        es_espacio = codigo == 32

        if not (es_mayuscula or es_minuscula or es_espacio):
            return False

    return True


def validar_genero(genero: str)->bool:
    """
    Valida que el texto contenga solo alguna de las letras M / F / X.
    :PARAM genero: String ingresado por el usuario, que representa el género del estudiante: M / F / X.
    :RETURN: True si el texto corresponde a alguna de las letras M / F / X. False en caso contrario.
    """

    if genero == "F" or genero == "M" or genero == "X":
        return True
    return False


def validar_nota_parcial_1(nota_parcial_1: str)->bool:
    """
    Valida que el texto contenga solo numeros enteros del 1 al 10.
    :PARAM nota_parcial_1: String ingresado por el usuario, que representa la nota del primer parcial, como número entero del 1 al 10.
    :RETURN: True si el texto corresponde a un número entero del 1 al 10. False en caso contrario.
    """

    if not validar_numero_entero(nota_parcial_1):
        return False
    
    nota_numerica_1 = int(nota_parcial_1)
    
    if nota_numerica_1 < 1 or nota_numerica_1 > 10:
        return False
    
    return True


def validar_nota_parcial_2(nota_parcial_2: str)->bool:
    """
    Valida que el texto contenga solo numeros enteros del 1 al 10.
    :PARAM nota_parcial_1: String ingresado por el usuario, que representa la nota del segundo parcial, como número entero del 1 al 10.
    :RETURN: True si el texto corresponde a un número entero del 1 al 10. False en caso contrario.
    """

    if not validar_numero_entero(nota_parcial_2):
        return False
    
    nota_numerica_2 = int(nota_parcial_2)
    
    if nota_numerica_2 < 1 or nota_numerica_2 > 10:
        return False
    
    return True


# ******************* FUNCIONES DE CARGA DE DATOS ****************************************************


CANTIDAD_ESTUDIANTES = 30

def cargar_legajo():
    """
    Pide un legajo. No recibe nada y devuelve el legajo ya validado.
    :PARAM:
    :RETURN: El número de legajo (si es válido) 
    """
    while True:
        legajo = input("🡺  INGRESE NÚMERO DE LEGAJO: ")
        if validar_legajo(legajo):
            return int(legajo)
        else:
            print("⚠ ERROR! - EL LEGAJO DEBE SER UN NÚMERO ENTERO.")

def cargar_nombre():
    """
    Pide el nombre y apellido del estudiante hasta que sea válido (solo letras y espacios).
    :RETURN: El texto ingresado (str) si es válido.
    """
    while True:
        nombre_y_apellido = input("🡺  INGRESE NOMBRE Y APELLIDO: ")
        if validar_nombre_y_apellido(nombre_y_apellido):
            return nombre_y_apellido
        print("⚠ ERROR! - SOLO SE PERMITEN LETRAS Y ESPACIOS.")


def cargar_genero():
    """
    Pide el género hasta que el usuario ingrese una de las letras identificatorias válidas: 'F', 'M' o 'X'.
    Devuelve: El género ingresado (str).
    """
    while True:
        genero = input("🡺  INGRESE GÉNERO [M/F/X]:  ")
        if validar_genero(genero):
            return genero
        print("⚠ ERROR! - SOLO SE PERMITEN LAS SIGUIENTES OPCIONES: M/F/X")


def cargar_nota_1():
    """
    Pide la nota del primer parcial hasta que sea un entero entre 1 y 10.
    :RETURN: La nota del primer parcial como número entero (int).
    """
    while True:
        nota_parcial_1 = input("🡺  INGRESE LA NOTAL DEL PRIMER PARCIAL:  ")
        if validar_nota_parcial_1(nota_parcial_1):
            return int(nota_parcial_1)
        print("⚠ ERROR! - LA NOTA DEBE SER UN NÚMERO ENTERO ENTRE 1 y 10")


def cargar_nota_2():
    """
    Pide la nota del segundo parcial hasta que sea un entero entre 1 y 10.
    :RETURN: La nota del segundo parcial como número entero (int).
    """
    while True:
        nota_parcial_2 = input("🡺  INGRESE LA NOTAL DEL SEGUNDO PARCIAL:  ")
        if validar_nota_parcial_2(nota_parcial_2):
            return int(nota_parcial_2)
        print("⚠ ERROR! - LA NOTA DEBE SER UN NÚMERO ENTERO ENTRE 1 y 10")


def cargar_todos_datos(legajos: list, nombres: list, generos: list, notas_parcial_1: list, notas_parcial_2: list)-> list:
    """
    Carga los datos de todos los estudiantes en las listas paralelas.
    :PARAM legajos, nombres, generos, nota_parcial_1, nota_parcial_2: Las cinco listas completas.
    :RETURN: True cuando terminó la carga.
    """

    for i in range(CANTIDAD_ESTUDIANTES):
        print()
        print("∷∷∷ CARGANDO DATOS DE ESTUDIANTE", i + 1, "DE", CANTIDAD_ESTUDIANTES, "∷∷∷")
        print()
        legajos[i] = cargar_legajo()
        nombres[i] = cargar_nombre()
        generos[i] = cargar_genero()
        notas_parcial_1[i] = cargar_nota_1()
        notas_parcial_2[i] = cargar_nota_2()
    return True


# ******************* FUNCIONES DE VISUALIZACIÓN DE DATOS *********************************************


def mostrar_estudiante(legajo: int, nombre: str, genero: str, nota_parcial_1: int, nota_parcial_2: int)->list:
    """
    Muestra los datos de todos los estudiantes en las listas paralelas.
    :PARAM legajo, nombre, genero, nota_parcial_1, nota_parcial_2: Todos los datos de cada estudiante.
    :RETURN: Un informe con los datos de cada estudiante.
    """
    promedio = calcular_promedio(nota_parcial_1, nota_parcial_2)
    print("│", legajo, "│", nombre, "│", genero, "│", nota_parcial_1, "│", nota_parcial_2, "│" f"{promedio:.2f}", "│")


def mostrar_todos_datos(legajos: list, nombres: list, generos: list, notas_parcial_1: list, notas_parcial_2: list)->list:
    """
    Muestra los datos de todos los estudiantes en las listas paralelas.
    :PARAM legajos, nombres, generos, notas_parcial_1, notas_parcial_2: Todas las listas de datos.
    :RETURN: Un informe con los datos de todos los estudiantes.
    """
    print("∷∷∷ INFORME DE ESTUDIANTES ∷∷∷")
    print("LEGAJO │ NOMBRE Y APELLIDO │ GÉNERO │ NOTA 1° PARCIAL │ NOTA 2° PARCIAL │ PROMEDIO")

    for i in range(CANTIDAD_ESTUDIANTES):
        mostrar_estudiante(legajos[i], nombres[i], generos[i], notas_parcial_1[i], notas_parcial_2[i])


def mostrar_ordenados(legajos: list, nombres: list, generos: list, notas_parcial_1: list, notas_parcial_2: list, promedios: list):
    """
    Ordena a los estudiantes por promedio de manera DESCENDENTE y muestra el informe.
    :PARAM legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios: Las seis listas paralelas.
    """
    ordenar(legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios, "DESC")
    print()
    print("ORDENADOS POR PROMEDIO (de mayor a menor)")
    mostrar_todos_datos(legajos, nombres, generos, notas_parcial_1, notas_parcial_2)


def mostrar_menu():
    """
    Muestra por consola las opciones del menú principal.
    """
    print()
    print("∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷ MENÚ PRINCIPAL ∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷∷")
    print("1 ⠒ Cargar datos")
    print("2 ⠒ Mostrar todos los estudiantes")
    print("3 ⠒ Calcular promedios")
    print("4 ⠒ Mostrar ordenados por promedio - Orden DESCENDENTE")
    print("5 ⠒ Mostrar estudiante/s con mayor promedio")
    print("6 ⠒ Buscar estudiante por legajo")
    print("7 ⠒ Salir del programa 🡺")
    print(("∷") * 56)


# ******************* FUNCIONES DE CÁLCULO DE PROMEDIOS *********************************************

def calcular_promedio(nota_parcial_1: int, nota_parcial_2: int)->float:
    """
    Calcula el promedio de dos notas.
    :PARAM nota_parcial_1, nota_parcial_2: Dos números enteros del 1 al 10 que representan las 2 notas del estudiante.
    :RETURN: El promedio del estudiante (float), entre 1.00 y 10.00.
    """
    return (nota_parcial_1 + nota_parcial_2) / 2


def calcular_promedios(notas_parcial_1: int, notas_parcial_2: int, promedios:float)->list:
    """
    Calcula el promedio de cada estudiante y lo guarda en la lista de promedios.
    :PARAM nota_parcial_1, nota_parcial_2, promedios: Recibe las tres listas.
    :RETURN: True cuando terminó el cálculo.
    """

    for i in range(CANTIDAD_ESTUDIANTES):
        promedios[i] = calcular_promedio(notas_parcial_1[i], notas_parcial_2[i])
    print("✔ PROMEDIOS CALCULADOS CORRECTAMENTE")
    return True

def mostrar_mayor_promedio(legajos: list, nombres: list, generos: list, notas_parcial_1: list, notas_parcial_2: list, promedios: list):
    """
    Muestra el/los estudiante/s con el mayor promedio.
    :PARAM legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios: Recibe las seis listas paralelas.
    """

    mayor_promedio = obtener_mayor_promedio(promedios)

    print("∷∷∷ ESTUDIANTES CON MAYOR PROMEDIO ∷∷∷")
    print("LEGAJO │ NOMBRE Y APELLIDO │ GÉNERO │ NOTA 1° PARCIAL │ NOTA 2° PARCIAL │ PROMEDIO")

    for i in range(CANTIDAD_ESTUDIANTES):
        if promedios[i] == mayor_promedio:
            mostrar_estudiante(legajos[i], nombres[i], generos[i], notas_parcial_1[i], notas_parcial_2[i])


# ******************* FUNCIONES DE ORDENAMIENTO ****************************************************

def intercambiar(lista: list, posicion_1: int, posicion_2: int):
    """
    Intercambia los elementos de dos posiciones de una lista.
    :PARAM lista, posicion_1, posicion_2: El nombre de la lista a ordenar, y las posiciones de los elementos.
    """

    auxiliar = lista[posicion_1]
    lista[posicion_1] = lista[posicion_2]
    lista[posicion_2] = auxiliar

def ordenar(legajos: list, nombres: list, generos: list, notas_parcial_1: list, notas_parcial_2: list, promedios: list, orden: str):
    """
    Ordena las listas paralelas por promedio (método burbuja).
    :PARAM legajos, nombres:, generos, notas_parcial_1, notas_parcial_2, promedios, orden: Recibe las seis listas paralelas y el tipo de orden (str): "ASC" o "DESC".
    """
    for i in range(CANTIDAD_ESTUDIANTES - 1):
        for j in range(CANTIDAD_ESTUDIANTES - 1 - i):
            if orden == "ASC":
                debe_intercambiar = promedios[j] > promedios[j + 1]
            else:
                debe_intercambiar = promedios[j] < promedios[j + 1]

            if debe_intercambiar:
                intercambiar(legajos, j, j + 1)
                intercambiar(nombres, j, j + 1)
                intercambiar(generos, j, j + 1)
                intercambiar(notas_parcial_1, j, j + 1)
                intercambiar(notas_parcial_2, j, j + 1)
                intercambiar(promedios, j, j + 1)

def obtener_mayor_promedio(promedios: list):
    """
    Busca el promedio más alto de la lista.
    :PARAM Promedios: Lista de todos los promedios de los estudiantes.
    :RETURN: Devuelve el mayor promedio (float).
    """
    mayor_promedio = promedios[0]

    for i in range(1, CANTIDAD_ESTUDIANTES):
        if promedios[i] > mayor_promedio:
            mayor_promedio = promedios[i]
    return mayor_promedio

def buscar_legajo(legajos: list, legajo_buscado: int):
    """
    Busca un legajo en la lista.
    :PARAM legajos, legajo_buscado: lista de todos los legajos, y el legajo buscado (int).
    :RETURN: Retorna la posición donde está el legajo, o retorna -1 si el legajo no existe.
    """ 
    for i in range(CANTIDAD_ESTUDIANTES):
        if legajos[i] == legajo_buscado:
            return i
    return -1

def mostrar_por_legajo(legajos: list, nombres: list, generos: list, notas_parcial_1: list, notas_parcial_2: list, promedios: list):
    """
    Pide un legajo, lo busca y muestra los datos del estudiante.
    :PARAM legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios: Recibe las cinco listas paralelas.
    """

    print("∷∷∷ BUSCAR ESTUDIANTE POR LEGAJO ∷∷∷")
    legajo_buscado = cargar_legajo()
    posicion = buscar_legajo(legajos, legajo_buscado)

    if posicion == -1:
        print("⚠ NO SE ENCONTRÓ NINGÚN ESTUDIANTE CON EL LEGAJO INGRESADO.")
    else:
        print("LEGAJO | NOMBRE Y APELLIDO | GÉNERO | NOTA 1° PARCIAL | NOTA 2° PARCIAL | PROMEDIO")
        mostrar_estudiante(legajos[posicion], nombres[posicion], generos[posicion], notas_parcial_1[posicion], notas_parcial_2[posicion])



def salir():
    """
    Muestra el mensaje de despedida al finalizar el programa.
    """
    print("∷∷∷ FIN DEL PROGRAMA ∷∷∷")
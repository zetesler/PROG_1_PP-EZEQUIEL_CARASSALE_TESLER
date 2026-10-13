import funciones

# TESTING DE LAS FUNCIONES 
"""
print(funciones.validar_legajo("1234"))
print(funciones.validar_nombre_y_apellido("Ana Perez"))
print(funciones.validar_nombre_y_apellido("Ana3"))
print(funciones.validar_genero("X"))
print(funciones.validar_genero("H"))
print(funciones.validar_nota_parcial_1("10"))
print(funciones.validar_nota_parcial_1("11"))
print(funciones.validar_nota_parcial_1("0"))

"""
# CREACIÓN DE LAS LISTAS VACÍAS, LUEGO COMPLETADAS POR LA CANTIDAD DE ESTUDIANTES 

"""
legajos = [0] * funciones.CANTIDAD_ESTUDIANTES
nombres = [""] * funciones.CANTIDAD_ESTUDIANTES
generos = [""] * funciones.CANTIDAD_ESTUDIANTES
notas_parcial_1 = [0] * funciones.CANTIDAD_ESTUDIANTES
notas_parcial_2 = [0] * funciones.CANTIDAD_ESTUDIANTES
promedios = [0.0] * funciones.CANTIDAD_ESTUDIANTES
"""

# DATOS HARDCODEADOS (solo para pruebas) 

legajos = [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010,
           1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020,
           1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030]

nombres = ["Sofia Avalos", "Luis Gomez", "Sol Diaz", "Marcos Lopez", "Lucia Fernandez",
           "Juan Martinez", "Camila Rodriguez", "Mateo Sanchez", "Valentina Romero", "Nicolas Torres",
           "Ana Perez", "Tomas Ruiz", "Julieta Acosta", "Lautaro Benitez", "Agustina Castro",
           "Franco Molina", "Micaela Herrera", "Bruno Silva", "Carla Medina", "Facundo Ortiz",
           "Daniela Flores", "Santiago Rios", "Paula Vega", "Ezequiel Suarez", "Brenda Navarro",
           "Joaquin Cabrera", "Milagros Ibarra", "Gonzalo Paz", "Rocio Luna", "Ignacio Moreno"]

generos = ["F", "M", "X", "M", "F", "M", "F", "M", "F", "M",
           "F", "M", "F", "M", "F", "M", "F", "M", "F", "M",
           "F", "M", "F", "M", "F", "M", "F", "M", "X", "M"]

notas_parcial_1 = [8, 5, 10, 7, 9, 4, 6, 8, 7, 3,
            9, 5, 8, 6, 10, 2, 7, 9, 4, 8,
            6, 10, 5, 7, 9, 3, 8, 6, 7, 5]

notas_parcial_2 = [9, 6, 10, 8, 9, 5, 7, 6, 8, 4,
            10, 6, 7, 5, 9, 3, 8, 9, 6, 7,
            5, 10, 6, 8, 9, 4, 7, 7, 8, 6]
datos_cargados = True

# BANDERAS INICIALIZADAS EN FALSE HASTA QUE SE EJECUTEN LAS FUNCIONES.

promedios = [0.0] * funciones.CANTIDAD_ESTUDIANTES
# datos_cargados = False
promedios_calculados = False

# MENÚ DE OPCIONES

opcion = ""
while opcion != "7":

    funciones.mostrar_menu()
    opcion = input("🡺  ELIJA UNA OPCIÓN: ")
    print()

    if not datos_cargados and opcion != "1" and opcion != "7":
        print("⚠ PRIMERO DEBE CARGAR LOS DATOS - SELECCIONE OPCIÓN 1")
    elif (opcion == "4" or opcion == "5") and not promedios_calculados:
        print("⚠ PRIMERO DEBE CALCULAR LOS PROMEDIOS - SELECCIONE OPCIÓN 3")
    else:
        match opcion:
            case "1":
                datos_cargados = funciones.cargar_todos_datos(legajos, nombres, generos, notas_parcial_1, notas_parcial_2)
                promedios_calculados = False
            case "2":
                funciones.mostrar_todos_datos(legajos, nombres, generos, notas_parcial_1, notas_parcial_2)
            case "3":
                promedios_calculados = funciones.calcular_promedios(notas_parcial_1, notas_parcial_2, promedios)
            case "4":
                funciones.mostrar_ordenados(legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios)
            case "5":
                funciones.mostrar_mayor_promedio(legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios)
            case "6":
                funciones.mostrar_por_legajo(legajos, nombres, generos, notas_parcial_1, notas_parcial_2, promedios)
            case "7":
                funciones.salir()
            case _:
                print("⚠ OPCIÓN INVÁLIDA - ELIJA UN NÚMERO DEL 1 AL 7")
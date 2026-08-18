# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”
# Contexto
# Hay 2 días de atención: Lunes y Martes. Cada día tiene cupos fijos:
# • Lunes: 4 turnos
# • Martes: 3 turnos
# Reglas
# 1. Pedir nombre del operador (solo letras).
# 2. Menú repetitivo hasta salir:
# 1) Reservar turno
# 2) Cancelar turno (por nombre)
# 3) Ver agenda del día
# 4) Ver resumen general
# 5) Cerrar sistema
# 3. Reservar:
# o Elegir día (1=Lunes, 2=Martes).
# o Pedir nombre del paciente (solo letras).
# o Verificar que no esté repetido en ese día (comparando con las variables ya cargadas).
# o Guardar en el primer espacio libre (ej. lunes1, lunes2…).
# 4. Cancelar:
# o Elegir día.
# o Pedir nombre del paciente (solo letras).
# o Si existe, cancelar y dejar el espacio vacío ("").
# 5. Ver agenda del día:
# o Mostrar los turnos del día en orden (Turno 1..N), indicando “(libre)” si está vacío.
# 6. Resumen general:
# o Turnos ocupados y disponibles por día.
# o Día con más turnos (o empate).

# Variables contadoras
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3= ""
# Validación del nombre operador
while True:
    nom = input("Ingrese nombre del operador: ")
    if nom.isalpha() and nom.strip() != "":
        break
    else:
        print("Error: Debe ingresar solo letras.")
# Elección de opciones
while True:
        print (f"\n1) Reservar turno\n2) Cancelar turno\n3) Ver agenda del dia\n4) Ver resumen general\n5) Salir del sistema")
        opcion = input(" ")
        if not opcion.isdigit():
            print("Error: Debe ingresar un número valido.")
            continue
        opcion_int = int(opcion)
# Opción 1
        if opcion_int == 1:
            while True:
                print("Seleccione el día para reservar:")
                print(f"\n1) Lunes\n2) Martes")
                opcion_dia = (input(" "))
                if opcion_dia.isdigit() and (opcion_dia == "1" or opcion_dia == "2"):
                    opcion_dia_int = int(opcion_dia)
                    break
                else:
                    print("Error: Debe seleccionar 1 o 2.")
            while True:
                nom_paciente = input("Ingrese el nombre del paciente: ")
                if nom_paciente.isalpha() and nom_paciente.strip() != "":
                    break
                else:
                    print("Error: Debe ingresar solo letras.")
            if opcion_dia_int == 1:
                if nom_paciente == lunes1 or nom_paciente == lunes2 or nom_paciente == lunes3 or nom_paciente == lunes4:
                    print(f"Error: El paciente {nom_paciente} ya tiene un turno reservado para el Lunes.")
                else:
                    if lunes1 == "":
                        lunes1 = nom_paciente
                        print("Turno 1 del Lunes reservado exitosamente.")
                    elif lunes2 == "":
                        lunes2 = nom_paciente
                        print("Turno 2 del Lunes reservado exitosamente.")
                    elif lunes3 == "":
                        lunes3 = nom_paciente
                        print("Turno 3 del Lunes reservado exitosamente.")
                    elif lunes4 == "":
                        lunes4 = nom_paciente
                        print("Turno 4 del Lunes reservado exitosamente.")
                    else:
                        print("Error: No quedan turnos disponibles para el día Lunes.")
# Opción 2 
            elif opcion_dia_int == 2:
                if nom_paciente == martes1 or nom_paciente == martes2 or nom_paciente == martes3:
                    print(f"Error: El paciente {nom_paciente} ya tiene un turno reservado para el Martes.")
            else:
                if martes1 == "":
                    martes1 = nom_paciente
                    print("Turno 1 del Martes reservado exitosamente.")
                elif martes2 == "":
                    martes2 = nom_paciente
                    print("Turno 2 del Martes reservado exitosamente.")
                elif martes3 == "":
                    martes3 = nom_paciente
                    print("Turno 3 del Martes reservado exitosamente.")
                else:
                    print("Error: No quedan turnos disponibles para el día Martes.")
        elif opcion_int == 2:
            while True:
                print("\nSeleccione el día para cancelar:")
                print(f"\n1) Lunes\n2) Martes")
                opcion_dia = (input(" "))
                if opcion_dia.isdigit() and (opcion_dia == "1" or opcion_dia == "2"):
                    opcion_dia_int = int(opcion_dia)
                    break
                else:
                    print("Error: Debe seleccionar 1 para Lunes o 2 para Martes.")
            while True:
                nom_paciente = input("Ingrese el nombre del paciente a cancelar: ")
                if nom_paciente.isalpha() and nom_paciente.strip() != "":
                    break
                else:
                    print("Error: El nombre debe contener solo letras.")
            if opcion_dia_int == 1:
                if nom_paciente == lunes1:
                    lunes1 = ""
                    print(f"Turno 1 de '{nom_paciente}' cancelado con éxito.")
                elif nom_paciente == lunes2:
                    lunes2 = ""
                    print(f"Turno 2 de '{nom_paciente}' cancelado con éxito.")
                elif nom_paciente == lunes3:
                    lunes3 = ""
                    print(f"Turno 3 de '{nom_paciente}' cancelado con éxito.")
                elif nom_paciente == lunes4:
                    lunes4 = ""
                    print(f"Turno 4 de '{nom_paciente}' cancelado con éxito.")
                else:
                    print(f"Error: No se encontró al paciente '{nom_paciente}' el día Lunes.")
            elif opcion_dia_int == 2:
                if nom_paciente == martes1:
                    martes1 = ""
                    print(f"Turno 1 de '{nom_paciente}' cancelado con éxito.")
                elif nom_paciente == martes2:
                    martes2 = ""
                    print(f"Turno 2 de '{nom_paciente}' cancelado con éxito.")
                elif nom_paciente == martes3:
                    martes3 = ""
                    print(f"Turno 3 de '{nom_paciente}' cancelado con éxito.")
                else:
                    print(f"Error: No se encontró al paciente '{nom_paciente}' el día Martes.")
# Opción 3
        elif opcion_int == 3:
            while True:
                print("Seleccione el día para ver la agenda:")
                print(f"\n1) Lunes\n2) Martes")
                opcion_dia = input(" ")
                if opcion_dia.isdigit() and (opcion_dia == "1" or opcion_dia == "2"):
                    opcion_dia_int = int(opcion_dia)
                    break
                else:
                    print("Error: Debe seleccionar 1 o 2.")
            if opcion_dia_int == 1:
                print("\n--- AGENDA LUNES ---")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            elif opcion_dia_int == 2:
                print("\n--- AGENDA MARTES ---")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
            else:
                print ("Error: Debe ingresar un número valido.")
                continue
# Opción 4
        elif opcion_int == 4:
            t_ocupados_lunes = 0
            if lunes1 != "": t_ocupados_lunes += 1
            if lunes2 != "": t_ocupados_lunes += 1
            if lunes3 != "": t_ocupados_lunes += 1
            if lunes4 != "": t_ocupados_lunes += 1
            t_libres_lunes = 4 - t_ocupados_lunes
            t_ocupados_martes = 0
            if martes1 != "": t_ocupados_martes += 1
            if martes2 != "": t_ocupados_martes += 1
            if martes3 != "": t_ocupados_martes += 1
            t_libres_martes = 3 - t_ocupados_martes
            if t_ocupados_lunes > t_ocupados_martes:
                dia_mas_ocupado = "Lunes"
            elif t_ocupados_martes > t_ocupados_lunes:
                dia_mas_ocupado = "Martes"
            else:
                dia_mas_ocupado = "Empate entre ambos días"
            print("--------------RESUMEN GENERAL-----------------")
            print(f"Lunes - Turnos Ocupados: {t_ocupados_lunes} | Disponibles: {t_libres_lunes}")
            print(f"Martes - Turnos Ocupados: {t_ocupados_martes} | Disponibles: {t_libres_martes}")
            print(f"Día con más turnos ocupados: {dia_mas_ocupado}")
            print("----------------------------------------------")
# Opción 5 (Salir)
        elif opcion_int == 5:
            print(f"\n¡Muchas gracias por utilizar el sistema, {nom}!")
            break
        else:
            print("Error: Opción fuera de rango (debe ser de 1 a 5).")

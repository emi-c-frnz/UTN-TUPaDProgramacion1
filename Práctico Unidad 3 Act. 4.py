# Ejercicio 4 "Escape Room - La Bóveda"
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
forzar_seguidas = 0 # Regla anti-spam

# Definir nombre del agente
while True:
    nom_agente = input("Bienvenido. Ingrese el nombre del agente: ")
    if nom_agente.isalpha() and nom_agente.strip() != "":
        break
    else:
        print("Error: Debe ingresar únicamente letras.")

# Bucle principal de acciones
# energia > 0 - tiempo > 0 - cerraduras_abiertas < 3 - no estar bloqueado por alarma
print(f"\n=================== ESTADISTICAS ===================")
print(f"Agente: {nom_agente}")
print(f"Energía: {energia}% | Tiempo restante: {tiempo}h")
print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
print(f"Alarma activa: {'SÍ' if alarma else 'NO'}")
print(f"Código parcial de hackeo: '{codigo_parcial}'")
print(f"===================================================")

print(f"\n1) Forzar cerradura (Costo: -20 energía, -2 tiempo)\n2) Hackear panel (Costo: -10 energía, -3 tiempo\n3) Descansar (Costo: +15 energía, 1 tiempo)")
print(f"\n===================================================")

# Forzar cerradura
while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    while True:
        opcion = input(f"\nSeleccione su acción (1/2/3): ")
        if opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3"):
            opcion_int = int(opcion)
            break
        else:
            print("Error: Debe ingresar una opción valida.")
            continue
    if opcion_int == 1:
        forzar_seguidas += 1
        if forzar_seguidas < 3:
            energia -= 20
            tiempo -= 2
            if energia < 40:
                print ("\nADVERTENCIA! Energía baja. Hay riesgo de activar la alarma.")
                while True:
                    num_riesgo = input("Elija un número de seguridad (1, 2 o 3): ")
                    if num_riesgo.isdigit() and (num_riesgo == "1" or num_riesgo == "2" or num_riesgo == "3"):
                        num_riesgo_int = int(num_riesgo)
                        break
                    else:
                        print("Error: Debe ingresar un número entero valido.")
                if num_riesgo_int == 3:
                    alarma = True
                    print("Activaste la alarma! 🚨")
            if not alarma:
                    cerraduras_abiertas += 1
                    print(f"Has abierto la cerradura número {cerraduras_abiertas}!")
            else:
                    print("Cerradura bloqueada debido a que activaste la alarma.")
        else:
            energia -= 20
            tiempo -= 2
            alarma = True
            print("La cerradura se trabó. Se ha activado la alarma!")
# Hackear
    elif opcion_int == 2:
        forzar_seguidas = 0
        energia -= 10
        tiempo -= 3
        print("\nIniciando hackeo... (Costo: -10 energía, -3 tiempo)")
        for i in range (4):
            codigo_parcial += "H"
            print (f"Hackeando... paso {i+1}/4 | Código parcial: '{codigo_parcial}'")
        if len(codigo_parcial) >= 8:
                cerraduras_abiertas += 1
                codigo_parcial = ""
                print(f"Has abierto la cerradura número {cerraduras_abiertas}!")
        else:
            print(f"El código parcial está incompleto ({len(codigo_parcial)}/8 caracteres). Necesitas hackear otra vez.")
# Descansar
    elif opcion_int == 3:
        forzar_seguidas = 0
        tiempo -= 1
        print ("\nDecides tomarte un descanso... (Costo: -1 tiempo)")
        energia += 15
        if energia > 100:
            energia = 100
    if alarma:
        energia -= 10
        print("La alarma no te deja descansar bien.")
        print("Sufres estrés y pierdes 10 de energia adicional.")
    print(f"Tu energia actual quedó en: {energia}%")
# Terminar juego
print("\n================ JUEGO TERMINADO ================")
if cerraduras_abiertas == 3:
    print(f"VICTORIA! El agente ha logrado abrir las 3 cerraduras y asegurar el botín.")
elif alarma and tiempo <= 3:
    print("DERROTA. La alarma estuvo activa demasiado tiempo con poco margen. La bóveda se bloqueó.") 
else:
    print("DERROTA. Te has quedado sin tiempo o energía antes de abrir la bóveda.") 
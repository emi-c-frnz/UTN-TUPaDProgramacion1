# Ejercicio 5: La Arena del Gladiador
# Validación del nombre
while True:
    nombre = input("Nombre del Gladiador: ")
    if nombre.isalpha() and nombre.strip() != "":
        break
    else:
        print("Error: Solo se permiten letras.")
# Estadísticas
vida_jugador = 100
vida_enemigo = 100
pociones = 3
ataque_pesado_base = 15
ataque_enemigo = 12
turno_gladiador = True
print("\n=== INICIO DEL COMBATE ===")
# Combate
while vida_jugador > 0 and vida_enemigo > 0:
    print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
    if turno_gladiador:
        print("Elige acción:")
        print("1. Ataque Pesado")
        print("2. Ráfaga Veloz")
        print("3. Curar")
        while True:
            opcion = input("Opción: ")
            if opcion.isdigit() and (opcion == "1" or opcion == "2" or opcion == "3"):
                opcion_int = int(opcion)
                break
            else:
                print("Error: Ingrese un número válido (1, 2 o 3).")
        if opcion_int == 1:
# Si golpe crítico
            if vida_enemigo < 20:
                dano_final = ataque_pesado_base * 1.5  # float (22.5)
                print("¡GOLPE CRÍTICO!")
            else:
                dano_final = float(ataque_pesado_base)
            vida_enemigo -= int(dano_final) 
            print(f"¡Atacaste al enemigo por {dano_final} puntos de daño!")
            turno_gladiador = False
        elif opcion_int == 2:
            print(">> ¡Inicias una ráfaga de golpes!")
            for i in range(3):
                vida_enemigo -= 5
                print(" > Golpe conectado por 5 de daño")
            turno_gladiador = False  
        elif opcion_int == 3:
            if pociones > 0:
                vida_jugador += 30
                if vida_jugador > 100:
                    vida_jugador = 100
                pociones -= 1
                print(f"Te has curado. Tu vida actual es {vida_jugador} HP.")
                turno_gladiador = False
            else:
                print("¡No quedan pociones! Has perdido tu turno.")
                turno_gladiador = False 
# Turno del enemigo
    else:
        if vida_enemigo > 0:
            print("\n ¡El enemigo contraataca!")
            vida_jugador -= ataque_enemigo
            print(f"¡El enemigo te atacó por {ataque_enemigo} puntos de daño!")
        
        turno_gladiador = True
# Final del combate
print("\n=== FIN DE LA BATALLA ===")
if vida_jugador > 0:
    print(f" ¡VICTORIA! {nombre} ha ganado la batalla.")
else:
    print(" DERROTA. Has caído en combate.")
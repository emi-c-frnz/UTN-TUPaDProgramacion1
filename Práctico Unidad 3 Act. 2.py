# Ejercicio 2: Login con intentos + menú de acciones con validación estricta.
# Requisitos
# 1. Definir credenciales fijas en el código: • usuario correcto: "alumno" • clave correcta: "python123"
# 2. Permitir máximo 3 intentos para ingresar usuario y clave.
# 3. Si falla 3 veces: mostrar “Cuenta bloqueada” y terminar.
# 4. Si ingresa bien: mostrar un menú repetitivo (usar while) hasta elegir salir:
# 1) Ver estado de inscripción (mostrar “Inscripto”)
# 2) Cambiar clave (pedir nueva clave y confirmación; deben coincidir)
# 3) Mostrar mensaje motivacional (1 frase)
# 4) Salir
# 5) Validación del menú: • Debe ser número (.isdigit()). • Debe estar entre 1 y 4.
# Cambio de clave: • La nueva clave debe tener mínimo 6 caracteres (validar con len()), si no, rechazar.)
usuario_correcto = "alumno"
clave_correcta = "python123"
intentos = 0
max_intentos = 3
login = False 

while intentos < max_intentos:
    usuario = input("Ingrese el nombre de usuario: ")
    clave = input("Ingrese la clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso permitido.")
        login = True
        break
    else:
        print ("Error: Has ingresado incorrectamente el usuario o la contraseña.")
        intentos += 1
        print (f"Intentos restantes: {intentos}/{max_intentos}")
        continue
if not login:
    print("Cuenta bloqueada.")
else:
    print("Bienvenido al menú del sistema! Ingrese un número.")
    menu = True
    while menu:
        print (f"\n1) Ver estado de inscripción\n2) Cambiar clave\n3) Mostrar mensaje motivacional\n4) Salir")
        opcion = input("")
        if opcion.isdigit():
            opcion_int = int(opcion)
            if 1 <= opcion_int <= 4:
                if opcion_int == 1:
                    print ("Estado: Inscripto")
                elif opcion_int == 2:
                    nueva_clave = input("Ingrese su nueva clave: ")
                    if len(nueva_clave) >= 6:
                        confirmacion = input("Confirme su nueva clave: ")
                        if nueva_clave == confirmacion:
                            clave_correcta = nueva_clave
                            print("Clave cambiada con éxito.")
                        else:
                            print("Error: Las claves no coinciden.")
                    else:
                        print("Error: La clave debe tener un mínimo de 6 caracteres.")
                elif opcion_int == 3:
                    print("Tener éxito no es aleatorio. Es una variable dependiente del esfuerzo. -Sofocles")
                elif opcion_int == 4:
                    print("Adiós!")
                    menu = False
            else:
                print ("Error: Debe ingresar las opciones en pantalla.")
        else:
            print ("Error: Ingrese un número válido.")
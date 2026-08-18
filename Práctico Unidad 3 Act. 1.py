# Ejercicio 1— “Caja del Kiosco”
# Objetivo: Simular una compra con validaciones y cálculo de total.
# 1. Pedir nombre del cliente (solo letras, validar con .isalpha() en while).
# 2. Pedir cantidad de productos a comprar (número entero positivo, validar con .isdigit() en while).
# 3. Por cada producto (usar for): 
# Pedir precio (entero, validar .isdigit()). Pedir si tiene descuento S/N (validar con while, aceptar "s" o "n" en cualquier mayuscula/minuscula). Si tiene descuento: aplicar 10% al precio de ese producto.
# 4. Al final mostrar: Total sin descuentos. Total con descuentos. Ahorro total o Promedio por producto (usar float y formatear con :.2f, ejem:
# x = 3.14159
# print(f"{x:.2f}"))

# Pedir nombre del cliente.

while True:
        nom = input("Ingrese su nombre: ")
        if nom.isalpha():
            break
        else:
            print ("Error: Debe ingresar solo letras.")
            continue

# Pedir cantidad de productos comprados.
cont = 0
while True:
        cant_prod = input("Ingrese la cantidad de productos comprados: ")
        if cant_prod.isdigit():
            cant_prod_int = int(cant_prod)
            if cant_prod_int > 0:
                break
            else:
                print ("Error: La cantidad debe ser mayor a 0.")
            continue
        else:
            print ("Error: Debe ingresar un número mayor a 0.")
total_sin_desc = 0
total_con_desc = 0
for i in range (cant_prod_int):
    while True:
        precio_str = input(f"Ingrese el precio del producto {i + 1}: ")
        if precio_str.isdigit():
            precio = int(precio_str)
            break
        else:
            print("Error: El precio debe ser un número entero positivo.")

# Pedir si tiene descuentos
    while True:
        desc = input("Tiene un código de descuento (S/N): ").upper() 
        if desc == "S" or desc == "N":
            break
        else:
            print("Error: Debe ingresar S o N.")
    total_sin_desc += precio
    if desc == "S":
        precio_con_descuento = precio * 0.90 # Restar 10% equivale a pagar el 90% del valor original.
    else:
        precio_con_descuento = precio
total_con_desc += precio_con_descuento
ahorro = total_sin_desc - total_con_desc
promedio = total_con_desc / cant_prod_int

print("\n-----RESUMEN DE COMPRA-----")
print(f"Cliente: {nom}")
print(f"Cantidad de productos: {cant_prod_int}")
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc:.2f}") # Formateado con dos decimales
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")
print("-------------------------")
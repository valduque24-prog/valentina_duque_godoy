# Programa de facturación para la tienda de llantas "Rueda Fácil"

print("======================================")
print("      FACTURACIÓN RUEDA FÁCIL")
print("======================================")

# Solicitar la cantidad de clientes
cantidad_clientes = int(input("Ingrese la cantidad de clientes a facturar: "))

# Bucle para procesar a cada cliente
for cliente in range(1, cantidad_clientes + 1):
    print(f"\nCliente N° {cliente}")

    # Solicitar la cantidad de llantas compradas
    cantidad_llantas = int(input("Ingrese la cantidad de llantas compradas: "))

    # Determinar el precio unitario según la cantidad de llantas
    if cantidad_llantas < 5:
        precio_unitario = 35000
    elif cantidad_llantas >= 5 and cantidad_llantas <= 10:
        precio_unitario = 40000
    else:
        precio_unitario = 45000

    # Calcular el total a pagar
    total_pagar = cantidad_llantas * precio_unitario

    # Mostrar la factura del cliente
    print("---------- DETALLE DE COMPRA ----------")
    print(f"Cantidad de llantas compradas: {cantidad_llantas}")
    print(f"Precio unitario aplicado: ${precio_unitario}")
    print(f"Total a pagar: ${total_pagar}")
    print("---------------------------------------")

print("\nProceso de facturación finalizado.")
# Programa para reservar un asiento en una sala de cine

# Crear una matriz de 3 filas y 4 columnas.
# 0 significa que el asiento está libre.
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Solicitar la fila al usuario
fila = int(input("Ingrese la fila (0 a 2): "))

# Solicitar la columna al usuario
columna = int(input("Ingrese la columna (0 a 3): "))

# Verificar que la fila y la columna sean válidas
if fila >= 0 and fila < 3 and columna >= 0 and columna < 4:

    # Verificar si el asiento está libre
    if asientos[fila][columna] == 0:

        # Reservar el asiento
        asientos[fila][columna] = 1
        print("\n¡Asiento reservado correctamente!")

    else:
        print("\nEl asiento ya está reservado.")

else:
    print("\nError: la fila debe estar entre 0 y 2 y la columna entre 0 y 3.")

# Mostrar el estado completo de la sala
print("\nEstado de la sala:")
print("+---+---+---+---+")

# Recorrer la matriz utilizando bucles anidados
for i in range(3):
    print("|", end="")
    for j in range(4):
        print(f" {asientos[i][j]} |", end="")
    print()
    print("+---+---+---+---+")
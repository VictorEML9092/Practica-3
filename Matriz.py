"""
Created on Monday 09/09/24

@author: Victor Mendoza
"""

# Vector que contendra las ventas
Ventas = [[0 for _ in range(13)] for _ in range(3)]
# Función para pedir las ventas por mes y departamento
def Ingresar_ventas():
    for f in range(3):
        for c in range(1, 13):
            Ventas[f][c] = int(input(f"Ingrese las ventas del mes [{c}] en el departamento[{f}]: "))
# Función para buscar un dato con la fila y columna
def Encontrar_dato():
    F = int(input("Ingrese la fila del valor que desea buscar: "))
    C = int(input("Ingrese la columna del valor que desea buscar: "))
    encontrado = False
    
    for f in range(3):
        for c in range(1, 13):
            if f == F and c == C:
                print(f"Valor encontrado fue:",Ventas[f][c])
                encontrado = True
    
    if not encontrado:
        print("Valor no encontrado en la matriz.")
# Función para eliminar un dato con la fila y columna
def Eliminar_dato():
    F = int(input("Ingrese la fila del valor que desea eliminar: "))
    C = int(input("Ingrese la columna del valor que desea eliminar: "))
    encontrado = False

    for f in range(3):
        for c in range(1, 13):
            if f == F and c == C:
                print(f"Valor eliminado fue:",Ventas[f][c])
                Ventas[f][c] = 0  # Se reemplaza con 0
                encontrado = True
    
    if not encontrado:
        print("El valor no existe en la matriz.")

# Inicio del programa
print("La siguiente matriz almacena las ventas por mes de cada departamento")
print("""
    Las siguientes posiciones significan:
    - Ropa = [0][?]
    - Deportes = [1][?]
    - Juguetería = [2][?]""")

Resp1 = input("\n¿Desea ingresar datos a la matriz? (Si/No): ")

if Resp1.lower() == "si":
    Ingresar_ventas()
else:
    exit()

print("\nLa matriz es:\n ")
for fila in Ventas:
    print(" ".join(str(num) for num in fila))

Resp2 = input("\n¿Desea buscar un dato en la matriz? (Si/No): ")

if Resp2.lower() == "si":
    Encontrar_dato()

Resp3 = input("\n¿Desea eliminar un dato de la matriz? (Si/No): ")

if Resp3.lower() == "si":
    Eliminar_dato()
    print("\nLa matriz ahora es:\n ")
    for fila in Ventas:
        print(" ".join(str(num) for num in fila))
else:
    print("Entonces, adiós")

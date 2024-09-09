Ventas = [[0 for _ in range(13)] for _ in range(3)]
    
print("La siguiente matriz almacena las ventas por mes de cada departamento")
print("""
    Las siguientes posiciones significan:
    - Ropa = [0][?]
    - Deportes = [1][?]
    - Juguetería = [2][?]""")
    
for f in range(3):
    for c in range(1, 13):
        Ventas[f][c] = int(input(f"Ingrese las ventas del mes [{c}] en el departamento[{f}]: "))

Elem1 = int(input("Ingrese el valor que desea buscar en la matriz: "))
encontrado = False
    
for f in range(3):
    for c in range(1, 13):
        if Ventas[f][c] == Elem1:
            print(f"Valor encontrado en el departamento [{f}] y mes [{c}]")
            encontrado = True
    
if not encontrado:
    print("Valor no encontrado en la matriz.")
    
Elem2 = int(input("Ingrese el valor que desea eliminar de la matriz: "))
encontrado = False

for f in range(3):
    for c in range(1, 13):
        if Ventas[f][c] == Elem2:
            print(f"Valor eliminado en el departamento [{f}] y mes [{c}]")
            Ventas[f][c] = 0  # Se reemplaza con 0
            encontrado = True
    
if not encontrado:
    print("Valor no encontrado en la matriz para eliminar.")
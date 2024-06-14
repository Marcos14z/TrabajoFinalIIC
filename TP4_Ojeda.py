piezas_procesadas = 0
x = True
while x:
    CP = int(input("Ingrese el código de la pieza o 0 para terminar: "))
    if CP == 0:
        print(f"Cantidad de piezas procesadas: {piezas_procesadas}")
        break
    elif CP < 1 or CP > 99:
        print("Código de pieza inválido")
        continue
    
    print(f"Código de pieza válido: {CP}")
    piezas_procesadas += 1
    PrT = 0
    
    while x:
        CC = int(input(f"Ingrese el código de componente {CP} o 0 para terminar: "))
        if CC == 0:
            print(f"Precio total de la pieza {CP}: ${PrT}")
            break
        elif CC % 100 != CP:
            print("código de componente inválido")
            continue
        
        print(f"Código de componente válido: {CC}")

        
        PrC = float(input(f"Ingrese el precio del componente {CC}: "))
        if PrC < 10.00 or PrC > 999.99:
            print("Precio del componente inválido.")
            continue

        PrT += PrC
        print(f"precio del componente: ${PrC}")


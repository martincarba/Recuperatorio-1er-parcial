from paquete.validaciones import *
from paquete.calculos import *

def cargar_matriz_secuencial(matriz:list,
                             depositos:list,
                             insumos:list,
                             mensaje:str) -> list: 
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            dato = input(f"{mensaje} {depositos[i]}, insumo {insumos[j]} :")
            while not validar_numero(dato):
                dato = input(f"ERROR. {mensaje} {depositos[i]}, insumo {insumos[j]} :")
            matriz[i][j] = int(dato)
    
    return matriz

def estimar_stock(matriz:list,
                  depositos_o_insumos:list,
                  mensaje:str,
                  limite:int,
                  por_fila: bool = True) -> None:
    
    totales = calcular_totales(matriz, por_fila)

    print(mensaje)

    for i in range(len(totales)):
        if totales[i] > limite:
            print(f"-{depositos_o_insumos[i]} -{totales[i]}")

def stock_insumos(matriz:list,
                  depositos:list,
                  insumos:list) -> None:
    
    for i in range(len(matriz)):
        mayor_stock = [matriz[i][0]]
        mayor_insumos = insumos[i]
        for j in range(len(matriz[i])):

            if matriz[i][j] > mayor_stock:
                mayor_stock = matriz[i][j]
                mayor_insumos = insumos[j]
        
        print(f"en el deposito {depositos[i]} el insumo con mayor stock es {mayor_insumos}")
        print(f"con {mayor_stock} unidades")


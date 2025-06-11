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

def stock_insumos(matriz: list,
                  depositos: list,
                  insumos: list) -> None:

    totales_por_insumo = calcular_totales(matriz, por_fila=False)
    
    for j in range(len(insumos)):
        mayor_stock = matriz[0][j]
        deposito_mayor = depositos[0]
        
        for i in range(1, len(depositos)):
            if matriz[i][j] > mayor_stock:
                mayor_stock = matriz[i][j]
                deposito_mayor = depositos[i]
        
        print(f"insumo '{insumos[j]}' tiene un total de {totales_por_insumo[j]} unidades.")
        print(f"mayor cantidad almacenada en depósito '{deposito_mayor}': {mayor_stock} unidades.\n")



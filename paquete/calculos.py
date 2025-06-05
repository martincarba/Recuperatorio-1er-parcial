def calcular_totales(matriz: list,
                     por_fila: bool = True) -> list:
    
    if por_fila:
        totales = [0] * len(matriz)
        for i in range(len(matriz)):
            for j in range(len(matriz[i])):
                totales[i] += matriz[i][j]
    else:
        columnas = len(matriz[0])
        totales = [0] * columnas
        for j in range(columnas):
            for i in range(len(matriz)):
                totales[j] += matriz[i][j]

    return totales




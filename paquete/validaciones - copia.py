def validar_numero(dato: str) -> bool:

    bandera = True
    indice = 0

    while bandera and indice < len(dato):
        if ord(dato[indice]) > 47 and ord(dato[indice]) < 58:
            indice += 1
        else:
            bandera = False

    return bandera

def validar_letras(dato: str) -> bool:
    bandera = True
    indice = 0

    while bandera and indice < len(dato):
        if (ord(dato[indice]) >= 65 and ord(dato[indice]) <= 90) or \
           (ord(dato[indice]) >= 97 and ord(dato[indice]) <= 122):
            indice += 1
        else:
            bandera = False

    return bandera

def validar_rango(numero: int, minimo: int, maximo: int) -> bool:
    return minimo <= numero <= maximo


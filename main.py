from paquete.matices import *
from paquete.validaciones import *

matriz = [[0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0],
          [0,0,0,0,0]]
 
depositos = ["Rosario", "Córdoba", "Salta", "Bahía Blanca"]

insumos = ["Arduino UNO", "Sensor de temperatura", "Cable USB", "Display LCD", "Protoboard"]

seguir = "s"

while seguir == "s":

    print("opciones: ")
    print("1. cargar stock")
    print("2. Mostrar depósitos con stock total superior a 5000 unidades")
    print("3. Mostrar insumos con stock total superior a 3000 unidades")
    print("4. Mostrar el depósito con mayor cantidad de unidades por insumo")

    opcion = input("ingrese: ")
    while not validar_numero(opcion):
        opcion = input("error. ingrese: ")
    opcion = int(opcion)


    match opcion:
        case 1:
            cargar_matriz_secuencial(matriz,
                                     depositos,
                                     insumos,
                                     "ingrese la cantidad en stock para")

        case 2:
            estimar_stock(matriz,
                          depositos,
                          "Los depositos que superan el limite de stock son: ",
                          5000)
        case 3:
            estimar_stock(matriz,
                          insumos,
                          "Los insumos que superan el limite de stock son: ",
                          3000,
                          False)
        case 4:
            stock_insumos(matriz,
                          depositos,
                          insumos)
            

    seguir = input("continuas? s/n: ")
    while not validar_letras(seguir):
        seguir = input("ERROR. continuas? s/n: ")

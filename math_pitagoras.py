import math

def calc_pitagoras(LadoA, LadoB, LadoC):
    LadoA = int(input('Insira o valor:'))
    LadoB = int(input('Insira o valor:'))
    adoC = math.sqrt(LadoA*LadoA + LadoB*LadoB)

    print(LadoA, LadoB, LadoC)
import math

def calc_pitagoras(LadoA, LadoB, LadoC):
    LadoA = int(input('Insira o valor:'))
    LadoB = int(input('Insira o valor:'))
    LadoC = math.sqrt(LadoA*LadoA + LadoB*LadoB)

    print(LadoA, LadoB, LadoC)
    #aplicação de função, chamada simples.
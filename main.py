import numpy as np
import math

def lerEntrada():
    n, m = input().split()
    n = int(n)
    m = int(m)

    custos = input().split()
    custos = list(map(int, custos))

    matrizSubConjuntos = []
    for i in range(n):
        linhaMatriz = input().split()
        linhaMatriz = list(map(int, linhaMatriz))
        matrizSubConjuntos.append(linhaMatriz)

    matrizSubConjuntos = np.array(matrizSubConjuntos)
    custos = np.array(custos)
    return n, m, custos, matrizSubConjuntos

def executarAlgoritmo(n, m, custos, matrizSubConjuntos):
    x = np.zeros((1, n))
    c = set()
    verticesCobertos = set()
    matrizSubConjuntosTransposta = matrizSubConjuntos.T

    while len(verticesCobertos) < n:
        faltante = -1
        for i in range(n):
            if not i in verticesCobertos:
                faltante = i
                break
        maiorAumentoPossivel = math.inf
        linhaMaiorAumento = -1
        for i in range(m):
            if matrizSubConjuntosTransposta[i, faltante] == 1:
                falta = custos[i] - matrizSubConjuntosTransposta[i]@x.T
                if falta < maiorAumentoPossivel:
                    maiorAumentoPossivel = falta
                    linhaMaiorAumento = i
        x[0, faltante] += maiorAumentoPossivel
        produto = matrizSubConjuntosTransposta@x.T
        conjuntoAdicionado = linhaMaiorAumento
        for i in range(n):
            if matrizSubConjuntosTransposta[conjuntoAdicionado, i] == 1:
                verticesCobertos.add(i)
        c.add(conjuntoAdicionado)
    return x, c

def printarSaida(m, x, c):
    for i in range(m):
        if i in c:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()

    for el in x[0]:
        print(int(el), end = ' ')
    print()

if __name__ == '__main__':
    n, m, custos, matrizSubConjuntos = lerEntrada()
    x, c = executarAlgoritmo(n, m, custos, matrizSubConjuntos)
    printarSaida(m, x, c)
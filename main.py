import numpy as np
import math

def lerEntrada():
    # Lê os valores n e m
    n, m = input().split()
    n = int(n)
    m = int(m)

    # Lê o vetor de custos
    custos = input().split()
    custos = list(map(int, custos))

    # Lê a matriz A
    matrizSubconjuntos = []
    for i in range(n):
        linhaMatriz = input().split()
        linhaMatriz = list(map(int, linhaMatriz))
        matrizSubconjuntos.append(linhaMatriz)

    # Converte a matriz e o vetor para arrays numpy
    matrizSubconjuntos = np.array(matrizSubconjuntos)
    custos = np.array(custos)

    # Retorna os valores lidos
    return n, m, custos, matrizSubconjuntos

def executarAlgoritmo(n, m, custos, matrizSubconjuntos):
    # Declara o vetor x, inicialmente composto apenas de zeros
    vetorX = np.zeros((1, n))
    
    # Declara os conjuntos de elementos cobertos e subconjuntos escolhidos
    subconjuntosEscolhidos = set()
    elementosCobertos = set()

    # Salva o resultado c-A.T@x para evitar realizar a multiplicação de matrizes
    # a cada iteração
    linhasCustosMenosMatrizT = custos

    # Enquanto existir elementos que não foram cobertos ainda
    while len(elementosCobertos) < n:
        # Encontra o elemento de menor índice não coberto
        faltante = -1
        for i in range(n):
            if not i in elementosCobertos:
                faltante = i
                break

        # Encontra o maior aumento possível da entrada do elemento não coberto em x
        # de forma que A.T@x <= c continue viável
        maiorAumentoPossivel = math.inf
        linhaMaiorAumento = -1
        for i in range(m):
            if matrizSubconjuntos[faltante, i] == 1:
                falta = linhasCustosMenosMatrizT[i]
                if falta < maiorAumentoPossivel:
                    maiorAumentoPossivel = falta
                    linhaMaiorAumento = i
        
        # Atualiza o vetor linhasCustosMenosMatrizT com os novos valores do vetor x
        # Ou seja, atualiza o resultado de c-A.T@x
        for i in range(m):
            if matrizSubconjuntos[faltante, i] == 1:
                linhasCustosMenosMatrizT -= maiorAumentoPossivel

        # Altera o vetor x para que esse maior aumento possível seja feito
        vetorX[0, faltante] += maiorAumentoPossivel

        # Salva no conjunto de elementos cobertos os elementos que o subconjunto
        # escolhido cobre
        conjuntoAdicionado = linhaMaiorAumento
        for i in range(n):
            if matrizSubconjuntosTransposta[conjuntoAdicionado, i] == 1:
                elementosCobertos.add(i)

        # Adiciona o subconjunto escolhido no conjunto de subconjuntos
        subconjuntosEscolhidos.add(conjuntoAdicionado)
    # Retorna o vetor x e os subconjuntos escolhidos
    return vetorX, subconjuntosEscolhidos

def printarSaida(m, vetorX, subconjuntosEscolhidos):
    # Imprime os subconjuntos escolhidos
    for i in range(m):
        if i in subconjuntosEscolhidos:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()

    # Imprime o vetor x
    for el in vetorX[0]:
        print(int(el), end = ' ')
    print()

if __name__ == '__main__':
    n, m, custos, matrizSubconjuntos = lerEntrada()
    vetorX, subconjuntosEscolhidos = executarAlgoritmo(n, m, custos, matrizSubconjuntos)
    printarSaida(m, vetorX, subconjuntosEscolhidos)
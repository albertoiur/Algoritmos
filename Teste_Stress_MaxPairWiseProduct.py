#Use python3
import random

def MaxPairWiseProductNaive(A):
    '''
    Função: Algoritmo lento
    '''
    producto = 0
    n = len(A)

    if len(A)<2:
        return A[0]

    for i in range(0,n):
        for j in range(i+1,n):
            producto = max(producto, A[i] * A[j])
    return producto

def MaxPairWiseProductFast(A):
    '''
    Função: Algoritmo rápido
    '''
    A.sort()
    if len(A)<2:
        return A[0]
    return (A[-1] * A[-2])


def Teste_Stress(N,M):
    '''
    Função Teste: Cria, num ciclo infinito, testes automáticos
    '''

    while True:
        A = []
        n = random.randint(2,N)

        for i in range(1,n):
            A.append(random.randint(0,M))

        print('Lista: ',A)
        resultado1 = MaxPairWiseProductNaive(A)
        resultado2 = MaxPairWiseProductFast(A)

        if resultado1 == resultado2:
            print("OK", resultado1,resultado2)
        else:
            print('Errado!',resultado1,resultado2)
            return

Teste_Stress(10,100000)

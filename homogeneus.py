#recebe a matriz A -> calcular autovalores
#Para cada autovalor, encontrar autovetor
import numpy as np
from gauss_jordan import calculaInversa
from gauss_jordan import calculaVetor
from matrix_operations import matrix_product
from matrix_operations import matrix_copy

def calcular_determinante(matriz):
    # Converter a lista de listas em uma matriz NumPy
    matriz_np = np.array(matriz)

    # Calcular o determinante usando a função det() do NumPy
    determinante = np.linalg.det(matriz_np)
    return determinante

def matrix_diagonalization(n, a):
    #reset bellow the diagonal
    for i in range(n-1):
        pivo = a[i][i]
        if pivo != 0:
            c = 1/pivo
            aux = a[i+1][i]
            c = aux*c
            for j in range(n):
                a[i+1][j] = a[i+1][j] - a[i][j]*c

    for i in range(n-1,0, -1):
        pivo = a[i][i]
        if pivo != 0:
            c = 1/pivo
            aux = a[i-1][i]
            c = aux*c
            for j in range(n):
                a[i-1][j] = a[i-1][j] - a[i][j]*c

def eigenvalue_finder(n, matriz_A, eigenvalue_list):
    eigenvalue_candidates = []
    num_lbda = 0
    lbda = 1
    while (num_lbda < n):
        for k in range(2):
            matrix_A2 = []
            matrix_product(matriz_A, matriz_A, matrix_A2, n)
            lbda = -1*lbda
            for i in range (n):
                matrix_A2[i][i] -= lbda

            det = calcular_determinante(matrix_A2)
            
            if det == 0:
                if lbda > 0:
                    num_lbda += 1
                else:
                    num_lbda += 2
                eigenvalue_candidates.append(lbda)
        lbda += 1
        
    for i in range(len(eigenvalue_candidates)):
        if eigenvalue_validation(eigenvalue_candidates[i], matriz_A, n) == 1:
            eigenvalue_list.append(eigenvalue_candidates[i])
    
def eigenvalue_validation(eigenvalue, matrix_A, n):
    #validates in the case that lbda > 0 
    if eigenvalue > 0:
        eigenvalue = eigenvalue**(1/2)
        for i in range(2):
            mtrx_copy = []
            matrix_copy(matrix_A, mtrx_copy, n)
            eigenvalue = -1*eigenvalue
            for j in range (n):
                mtrx_copy[j][j] -= eigenvalue
            det = calcular_determinante(mtrx_copy)
            if det == 0:
                return 1
    return 0

def eigenvector_finder(eigenvalue, matrix_A, n):
    matrix_copy = []
    vetor = [0,0]
    #salvar a matriz_A em algum lugar
    for i in range(n):
        matrix_copy.append([])
        for j in range(n):
            matrix_copy[i].append(matrix_A[i][j])
        matrix_copy[i][i] -= eigenvalue
        
    calculaInversa(n, matrizCaracteristica, matrizIdentidade)
    print(matrizIdentidade)
    calculaVetor(n, matrizIdentidade, vetor)

n = int(input("Ordem da matriz: "))
matrizCaracteristica = []
matrizIdentidade = []
vetorCaracteristico = []
eigenvalue_list = []

print("Matriz caracteristica")
for i in range(n):
    linha = input().split(" ")
    matrizCaracteristica.append([])
    matrizIdentidade.append([])
    for j in range(n):
        matrizCaracteristica[i].append(int(linha[j]))
        matrizIdentidade[i].append(0)
    matrizIdentidade[i][i] = 1

eigenvalue_finder(n, matrizCaracteristica, eigenvalue_list)
print(eigenvalue_list)
# eigenvector_finder(eigenvalue_list[0], matrizCaracteristica, n)
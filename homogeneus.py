#recebe a matriz A -> calcular autovalores
#Para cada autovalor, encontrar autovetor
from gauss_jordan import calculaInversa
from gauss_jordan import calculaVetor
from matrix_operations import matrix_product

def matrix_diagonalization(n, a):
    #reset bellow the diagonal
    for i in range(n-1):
        pivo = a[i][i]
        c = 1/pivo
        aux = a[i+1][i]
        c = aux*c
        for j in range(n):
            a[i+1][j] = a[i+1][j] - a[i][j]*c


    for i in range(n-1,0, -1):
        pivo = a[i][i]
        c = 1/pivo
        aux = a[i-1][i]
        c = aux*c
        
        for j in range(n):
            a[i-1][j] = a[i-1][j] - a[i][j]*c

def eigenvalue_finder(n, matriz_A, eigenvalue_candidates):
    
    num_lbda = 0
    lbda = 0
    while (num_lbda < n):
        
        matrix_A2 = []
        matrix_product(matriz_A, matriz_A, matrix_A2, n)
        
        for i in range (n):
            matrix_A2[i][i] -= lbda

        matrix_diagonalization(n, matrix_A2)
        
        det = 0
        for i in range(n):
            det += matrix_A2[i][i]
            
        
        if det == 0:
            print(lbda)
            if lbda >= 0:
                num_lbda += 1
            else:
                num_lbda += 2
            eigenvalue_candidates.append()
        elif det > 0:
            lbda -= 1
        elif det < 0:
            lbda += 1
        
    print(eigenvalue_candidates)
        
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
# print(eigenvalue_list)
# eigenvector_finder(eigenvalue_list[0], matrizCaracteristica, n)
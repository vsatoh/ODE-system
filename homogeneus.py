#recebe a matriz A -> calcular autovalores
#Para cada autovalor, encontrar autovetor
from gauss_jordan import gauss_jordan_method
from matrix_operations import matrix_product
from matrix_operations import matrix_copy

def submatrix(matrix, row, col):
    """Retorna a submatriz excluindo a linha 'row' e a coluna 'col'."""
    return [[matrix[i][j] for j in range(len(matrix[i])) if j != col] for i in range(len(matrix)) if i != row]

def determinant(matrix):
    """Calcula o determinante de uma matriz usando expansão por cofatores."""
    # Caso base: matriz 1x1
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix[0][0]

    det = 0
    for col in range(len(matrix[0])):
        cofactor = (-1) ** col * matrix[0][col] * determinant(submatrix(matrix, 0, col))
        det += cofactor

    return det

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

            det = determinant(matrix_A2)
            if det == 0:
                if lbda > 0:
                    eigenvalue = lbda**(1/2)
                    for i in range(2):
                        eigenvalue = eigenvalue*-1
                        if eigenvalue_validation(eigenvalue, matriz_A, n) == 1:
                            eigenvalue_list.append(eigenvalue)
                            matriz_A_copy = []
                            matrix_copy(matriz_A, matriz_A_copy, n)
                            for j in range (n):
                                matriz_A_copy[j][j] -= eigenvalue
                            num_lbda += eigenvalue_multiplicity(matriz_A_copy, n)
                else:
                    num_lbda += 2
                    eigenvalue_candidates.append(lbda)
        lbda += 1
        
    
def eigenvalue_validation(eigenvalue, matrix_A, n):
    #validates in the case that lbda > 0 
    mtrx_copy = []
    matrix_copy(matrix_A, mtrx_copy, n)
    for j in range (n):
        mtrx_copy[j][j] -= eigenvalue
    det = determinant(mtrx_copy)
    if det == 0:
        return 1
    return 0

def eigenvalue_multiplicity(matrix, n):
    if n == 1:
        return 0
    det = determinant(matrix)
    if det != 0:
        return 0
    aux1 = True
    for i in range(n-1):
        for j in range(i+1, n):
            if aux1 == True:
                pivo = matrix[i][0]/matrix[j][0]
                aux2 = True
                k = 1
                while aux2:
                    a = matrix[i][k]
                    b = matrix[j][k]
                    if a != 0 and b != 0:
                        lbda = a/b
                        if lbda != pivo:
                            aux2 = False
                    if k == n-1:
                        ind1 = i
                        aux2 = False
                        aux1 = False
                    k += 1
    n_matrix = []
    k = 0
    for i in range(n):
        if i != ind1:
            n_matrix.append([])
            for j in range(1,n):
                n_matrix[k].append(matrix[i][j])
            k+=1
    return 1 + eigenvalue_multiplicity(n_matrix, n-1)

def eigenvector_finder_case1(matrix, n, result_vector):
    aux1 = True
    for i in range(n-1):
        for j in range(i+1, n):
            if aux1 == True:
                pivo = matrix[i][0]/matrix[j][0]
                aux2 = True
                k = 1
                while aux2:
                    a = matrix[i][k]
                    b = matrix[j][k]
                    if a != 0 and b != 0:
                        lbda = a/b
                        if lbda != pivo:
                            aux2 = False
                    if k == n-1:
                        ind1 = i
                        aux2 = False
                        aux1 = False
                    k += 1
    n_matrix = []
    result_vector.append(1)
    value_vector = []
    k = 0
    for i in range(n):
        if i != ind1:
            n_matrix.append([])
            value_vector.append(-1*matrix[i][0])
            for j  in range(1,n):
                n_matrix[k].append(matrix[i][j])
            k+=1
        
    gauss_jordan_method(n_matrix, value_vector, result_vector, n-1)


n = int(input("Ordem da matriz: "))
matrizCaracteristica = []
vetorCaracteristico = []
eigenvalue_list = []

print("Matriz caracteristica")
for i in range(n):
    linha = input().split(" ")
    matrizCaracteristica.append([])
    for j in range(n):
        matrizCaracteristica[i].append(int(linha[j]))
    
eigenvalue_finder(n, matrizCaracteristica, eigenvalue_list)
print(eigenvalue_list)

for eign in eigenvalue_list:
    matrix_copy_A = []
    result_vector = []
    matrix_copy(matrizCaracteristica, matrix_copy_A, n)
    
    for i in range(n):
        matrix_copy_A[i][i] -= eign
        
    eigenvector_finder_case1(matrix_copy_A, n, result_vector)
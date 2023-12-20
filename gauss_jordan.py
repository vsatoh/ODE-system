from matrix_operations import matrix_copy

def calculaInversa(n, a, b):
    for i in range(n):
        pivo = a[i][i]
        c = 1/pivo
        for j in range(n):
            a[i][j] = c*a[i][j]
            b[i][j] = c*b[i][j]
        if(i != n-1):
            for j in range(i+1, n):
                lbd = a[j][i]
                for k in range(n):
                    a[j][k] -= lbd*a[i][k]
                    b[j][k] -= lbd*b[i][k]

    for i in range(n-1,-1, -1):
        pivo = a[i][i]
        c = 1/pivo
        for j in range(n):
            a[i][j] = c*a[i][j]
            b[i][j] = c*b[i][j]
        if(i != 0):
            for j in range(i-1, -1, -1):
                lbd = a[j][i]
                for k in range(n):
                    a[j][k] -= lbd*a[i][k]
                    b[j][k] -= lbd*b[i][k]
                    
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
                    
def calculaVetor(n, matrizInversa, vetor, result_vector):
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += matrizInversa[i][j]*vetor[j]
        result_vector.append(soma)
        soma = 0
    print(result_vector)
    
def gauss_jordan_method(matrix_A, value_vector, result_vector, n):
    identity_matrix = []
    
    for i in range(n):
        identity_matrix.append([])
        for j in range(n):
            if i == j:
                identity_matrix[i].append(1)
            else:
                identity_matrix[i].append(0)
                
    matrix_A_copy = []
    matrix_copy(matrix_A, matrix_A_copy, n)
    
    calculaInversa(n, matrix_A_copy, identity_matrix)
    calculaVetor(n, identity_matrix, value_vector, result_vector)
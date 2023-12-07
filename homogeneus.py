#recebe a matriz A -> calcular autovalores
#Para cada autovalor, encontrar autovetor
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

def eigenvalue_finder(n, matriz_A, eigenvalue_list):
    matrix_copy = []
    #salvar a matriz_A em algum lugar
    for i in range(n):
        matrix_copy.append([])
        for j in range(n):
            matrix_copy[i].append(matriz_A[i][j])
            
    #matrix_copy will be a diagonal matrix after the follow method
    matrix_diagonalization(n, matrix_copy)
    for i in range(n):
        eigenvalue_list.append(matrix_copy[i][i])
    
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
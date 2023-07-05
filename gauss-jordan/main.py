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
                    
def calculaVetor(n, matrizInversa, vetor):
    resultado = [] 
    soma = 0
    for i in range(n):
        for j in range(n):
            soma += matrizInversa[i][j]*vetor[j]
        resultado.append(soma)
        soma = 0
    print(resultado)
    return resultado
                    

                    
n = int(input("Ordem da matriz: "))
matrizCaracteristica = []
matrizIdentidade = []
vetorCaracteristico = []

print("Matriz caracteristica")
for i in range(n):
    linha = input().split(" ")
    matrizCaracteristica.append([])
    matrizIdentidade.append([])
    for j in range(n):
        matrizCaracteristica[i].append(int(linha[j]))
        matrizIdentidade[i].append(0)
    matrizIdentidade[i][i] = 1

print("Vetor correspondente")
linha = input().split()
for i in range(n):
    vetorCaracteristico.append(int(linha[i]))
print(matrizCaracteristica)
calculaInversa(n, matrizCaracteristica, matrizIdentidade)
print(matrizCaracteristica)
calculaVetor(n, matrizIdentidade, vetorCaracteristico)


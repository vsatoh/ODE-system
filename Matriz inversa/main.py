n = int(input("Ordem da matriz: "))
a = []
b = []

for i in range(n):
    linha = input().split(" ")
    a.append([])
    b.append([])
    for j in range(n):
        a[i].append(int(linha[j]))
        b[i].append(0)
    b[i][i] = 1
print(b)


for i in range(n):
    pivo = a[i][i]
    c = 1/pivo
    for j in range(n):
        a[i][j] = c*a[i][j]
        b[i][j] = c*b[i][j]
    if(i != n-1):
        for j in range(i+1, n):
            lbd = a[j][i]
            print(lbd)
            for k in range(n):
                a[j][k] -= lbd*a[i][k]
                b[j][k] -= lbd*b[i][k]

print(a)


for i in range(n-1,-1, -1):
    pivo = a[i][i]
    c = 1/pivo
    for j in range(n):
        a[i][j] = c*a[i][j]
        b[i][j] = c*b[i][j]
    if(i != 0):
        for j in range(i-1, -1, -1):
            lbd = a[j][i]
            print(lbd)
            for k in range(n):
                a[j][k] -= lbd*a[i][k]
                b[j][k] -= lbd*b[i][k]
                print(a)
                print(b)
                print("\n")
                



        

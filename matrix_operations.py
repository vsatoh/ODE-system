def matrix_product(MA, MB, MC, n):
    #MA: Matrix A
    #MB: Matrix B
    #MC: Result Matrix
    
    for k in range(n):
        MC.append([])
        for i in range(n):
            min_product_sum = 0
            for j in range(n):
                min_product_sum += MA[k][j]*MB[j][i]
            MC[k].append(min_product_sum)
            
            
def matrix_copy(matrix_A, matrix_copy, n):
    for i in range(n):
        matrix_copy.append([])
        for j in range(n):
            matrix_copy[i].append(matrix_A[i][j])
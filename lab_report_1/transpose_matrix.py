matrix1=[[1,2,3],[4,5,6],[7,8,9]]

matrix2=[[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]

for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        matrix2[i][j]=matrix1[j][i]
        
print(matrix2)
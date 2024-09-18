matrix1=[[1,2,3],[4,5,6]]
matrix2=[[1,2,3],[4,5,6]]
matrix3=[[0 for i in range(len(matrix1[0]))] for j in range(len(matrix1))]

if(len(matrix1[0])!=len(matrix2[0]) or len(matrix1)!=len(matrix2)):
    print("adding not possible")
else:
    for i in range(len(matrix1)):
        for j in range(len(matrix1[0])):
            matrix3[i][j]=matrix1[i][j]+matrix2[i][j]
            
print(matrix3)

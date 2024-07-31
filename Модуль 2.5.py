def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        row = [value]*m
        matrix.append(row)
        return matrix
result1 = get_matrix(3,4,10)
result2 = get_matrix(5,5,62)
result3 = get_matrix(3,6,85)
print(result1)
print(result2)
print(result3)





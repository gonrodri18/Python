A = [[1,3,5], [2,-4,6], [3,8,9]]
n = len(A)
traza = 0
for i in range(n):
    traza += A[i][i] 
print (traza)
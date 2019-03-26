a = ((1, 2, 3),
     (4, 5, 6))
b = ((-1, 0),
     (0, 1),
     (1,1))
resultado = [[0,0],
          [0,0]]
for i in range(len(a)):
    for j in range(len(b[0])):
        for m in range(len(b)):
            resultado[i][j] += a[i][m] * b[m][j]
for i in range(len(resultado)):
    resultado[i] = tuple(resultado[i])
resultado = tuple(resultado)
for i in range(len(resultado)):
    print(resultado[i])

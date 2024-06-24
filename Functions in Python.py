def get_matrix(n, m, value):
    matrix = []
    a = []
    for i in range(n):
        matrix.append(a)
    for j in range(m):
        a.append(value)
    return matrix

print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))

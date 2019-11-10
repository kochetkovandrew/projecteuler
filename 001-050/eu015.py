lattice = [[1]]
size = 20

for i in range(1, 2*size + 1):
    diag = []
    if i <= size:
        for j in range(0, i+1):
            summ = 0
            if j > 0:
                summ += lattice[i-1][j-1]
            if j < i:
                summ += lattice[i-1][j]
            diag.append(summ)
    else:
        for j in range(0, 2*size - i + 1):
            summ = lattice[i-1][j] + lattice[i-1][j+1]
            diag.append(summ)
    lattice.append(diag)

print(lattice[-1][0])

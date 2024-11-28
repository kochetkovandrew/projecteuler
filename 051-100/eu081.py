f = open('0081_matrix.txt', 'r')
lines = f.readlines()
weights = list(map(lambda line: list(map(lambda num: int(num), line.split(','))), lines))
rows, cols = (len(weights), len(weights[0]))
sums = [[0 for i in range(cols)] for j in range(rows)]
sums[0][0] = weights[0][0]

oldsum = 0
newsum = sum(map(lambda row: sum(row), sums))

while oldsum != newsum:
    for i in range(0, rows):
        for j in range(0, cols):
            if sums[i][j] > 0:
                if j < cols-1:
                    right = sums[i][j] + weights[i][j+1]
                    if sums[i][j+1] == 0 or sums[i][j+1] > right:
                        sums[i][j+1] = right
                if i < rows-1:
                    down = sums[i][j] + weights[i+1][j]
                    if sums[i+1][j] == 0 or sums[i+1][j] > down:
                        sums[i+1][j] = down
    oldsum = newsum
    newsum = sum(map(lambda row: sum(row), sums))

print(sums[rows-1][cols-1])

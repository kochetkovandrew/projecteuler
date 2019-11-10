f = open('eu018.txt', 'r')
sum = 0
lines = f.readlines()

triangle = []
triangle_sums = []

for line in lines:
    nums = list(map(lambda elem: int(elem), line.split()))
    triangle.append(nums)

triangle_sums.append(triangle[0])

for i in range(1, len(triangle)):
    row = [ triangle_sums[i-1][0] + triangle[i][0] ]
    for j in range(1, len(triangle[i]) - 1):
        row.append(max([triangle_sums[i-1][j-1] + triangle[i][j], triangle_sums[i-1][j] + triangle[i][j]]))
    row.append(triangle_sums[i-1][len(triangle[i]) - 2] + triangle[i][len(triangle[i]) - 1])
    triangle_sums.append(row)

print(max(triangle_sums[-1]))

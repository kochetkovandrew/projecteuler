lim = 1000
triangles = {}
m = 2

while m**2 < lim:
    for n in range(1, m):
        k = 1
        perimeter = 2 * k * (m ** 2) + 2 * k * m * n
        while perimeter <= lim:
            if perimeter not in triangles:
                triangles[perimeter] = []
            triangle = sorted([k*(m**2 - n**2), k*(m**2 + n**2), 2*k*m*n])
            if triangle not in triangles[perimeter]:
                triangles[perimeter].append(triangle)
            k += 1
            perimeter = 2 * k * (m ** 2) + 2 * k * m * n
    m += 1

triangle_count = {perimeter: len(triangle_list) for perimeter, triangle_list in triangles.items()}
max_value_key = max(triangle_count, key=triangle_count.get)
print(max_value_key)


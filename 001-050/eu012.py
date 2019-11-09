from lib import Prime

prime = Prime()

divider_count = 500
triangle_number = 1
step = 2
while prime.sigma_zero(triangle_number) <= divider_count:
    triangle_number += step
    step += 1

print(triangle_number)

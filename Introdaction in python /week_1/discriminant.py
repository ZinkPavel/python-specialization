import sys
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

d = math.sqrt(b ** 2 - 4 * a * c)

x1 = (-b + d) / (2 * a)
x2 = (-b - d) / (2 * a)

print(f"{math.trunc(x1)}\n{math.trunc(x2)}")

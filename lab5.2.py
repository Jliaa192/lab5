import math
a = float(input())
b = float(input())
if a < b:
    lst=[round(x * 0.1, 1) for x in range(int(a * 10), int(b *10) + 1)]
    s = [round(math.sin(x), 2) for x in lst]
print(s)


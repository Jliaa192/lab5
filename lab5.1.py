n = int(input())
lst = [[i for k in range(n)]for i in range(n)]
for x in lst:
    print(*x)
n = int(input())
l1, l2 = [list(map(int, input().split())) for _ in range(2)]
result = []
for i, j in zip(l1, l2):
    result.append(i)
    result.append(j)

print(*result)

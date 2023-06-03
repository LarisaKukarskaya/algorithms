n = int(input())
m = int(input())
a = []
for i in range(n):
    row = input().split()
    for i in range(m):
        row[i] = int(row[i])
    a.append(row)
n0 = int(input())
m0 = int(input())

spisok = []
if n0 > 0:
    n1 = n0 - 1
    m1 = m0
    spisok.append(a[n1][m1])

if m0 < m - 1:
    n1 = n0
    m1 = m0 + 1
    spisok.append(a[n1][m1])

if n0 < n - 1:
    n1 = n0 + 1
    m1 = m0
    spisok.append(a[n1][m1])

if m0 > 0:
    n1 = n0
    m1 = m0 - 1
    spisok.append(a[n1][m1])

spisok.sort()
for k in spisok:
    print(k, end=' ')

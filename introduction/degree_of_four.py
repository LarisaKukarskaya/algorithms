n = int(input())
while True:
    if n == 1:
        flag = True
        break
    n = n / 4
    if (n % 4 > 0 and n != 1):
        flag = False
        break
print(flag)

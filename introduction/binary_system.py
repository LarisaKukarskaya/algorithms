a = input()
b = input()
if (len(a) >= len(b)):
    n = len(a)
    b = b.zfill(n)
else:
    n = len(b)
    a = a.zfill(n)
a = list(a)
b = list(b)
for i in range(len(a)):
    a[i] = int(a[i])
for i in range(len(b)):
    b[i] = int(b[i])
a.reverse()
b.reverse()
all_list = []
if (len(a) >= len(b)):
    n = len(a)
else:
    n = len(a)
flag = 0
for i in range(n):
    temp = a[i] + b[i] + flag
    if temp == 0:
        all_list.append(0)
    elif temp == 1:
        all_list.append(1)
        flag = 0
    elif temp == 2:
        all_list.append(0)
        flag = 1
    else:
        all_list.append(1)
        flag = 1
if flag == 1:
    all_list.append(1)
all_list.reverse()
for i in range(len(all_list)):
    print(all_list[i], end='')

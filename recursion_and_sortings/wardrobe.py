n = int(input())
str = (input().split())
left = 0
right = len(str)
less = []
equal = []
greater = []
for x in str:
    if x == '0':
        less.append(x)
    elif x == '1':
        equal.append(x)
    else:
        greater.append(x)
print(*(less + equal + greater))

import string

sp = input().lower()
sp = sp.replace(' ', '')

for p in string.punctuation:
    if p in sp:
        sp = sp.replace(p, '')
i = 0
flag = 1
while i < len(sp) // 2:
    if (sp[i] != sp[len(sp) - i - 1]):
        flag = 0
        break
    i += 1
if flag == 0:
    print('False')
else:
    print('True')

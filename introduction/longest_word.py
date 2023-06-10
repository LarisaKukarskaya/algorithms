n = int(input())
sp = input().split()
long_word = sp[0]
i = 0
while i < len(sp):
    if len(sp[i]) > len(long_word):
        long_word = sp[i]
    i += 1
print(long_word)
print(len(long_word))

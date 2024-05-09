def hashes_arr(k):
    h_len = len(k) + 1
    hashes = [0] * h_len
    hashes[1] = k[0]
    for i in range(2, h_len):
        hashes[i] = (hashes[i-1] * a + k[i-1]) % m
    return hashes

def quick_hash(o, p, r):
    m = o % r
    t = 1
    while p:
        if p % 2:
            t *= m
            t %= r
        m *= m
        m %= r
        p //= 2
    return t % r
a = int(input().strip())
m = int(input().strip())
hashes = hashes_arr(bytes(input().strip(), encoding='ascii'))
n = int(input().strip())

res = [0] * n
for i in range(n):
    b, e = input().strip().split()
    beginning, end = int(b), int(e)
    res[i] = (hashes[end] % m - hashes[beginning-1] * quick_hash(a, end-beginning+1, m)) % m
print(*res, sep='\n')

import random
import string

base = 1000
size_table= 123_987_123

def polynomial_hash(str, p, m):
    power_of_p = 1
    hash_val = 0

    for char in str:
        hash_val = ((hash_val + ord(char) * power_of_p) % m)
        power_of_p = (power_of_p * p) % m

    return int(hash_val)

letters = string.ascii_lowercase
str = ''.join(random.choice(letters) for i in range(10))
hash = polynomial_hash(str[::-1], base, size_table)
map = {}

while True:
    str = ''.join(random.choice(letters) for i in range(20))
    hash = polynomial_hash(str[::-1], base, size_table)
    if not map.get(hash):
        map[hash] = str
    else:
        print(f"{str} - {hash}")
        break

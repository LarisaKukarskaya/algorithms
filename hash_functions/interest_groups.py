n = int(input())
groups = [input() for i in range(n)]
new_groups = sorted (set(groups), key = lambda a:groups.index(a))
for group in new_groups:
    print(group)

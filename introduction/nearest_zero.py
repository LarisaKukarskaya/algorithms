def distance_to_zero(first, seq):
	a = first
	for n in seq:
		if n == '0':
			a = 0
		else:
			a += 1
		yield a

input()
numbers = input().split()

left = distance_to_zero(len(numbers), numbers)
right = reversed(tuple(distance_to_zero(len(numbers), reversed(numbers))))

print(*map(min, zip(left, right)))

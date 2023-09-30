def brackets_generator(pair, n1, n2, prefix):
	if n1 == 0 and n2 == 0:
		print(prefix)
	else:
		if n1 > 0:
			brackets_generator(pair + 1, n1 - 1, n2, prefix + '(')
		if (pair > 0 and n2 > 0):
			brackets_generator(pair - 1, n1, n2 - 1, prefix + ')')


if __name__ == '__main__':
	n = int(input())
	pair = 0
	n1 = n
	n2 = n
	brackets_generator(pair, n1, n2, '')	

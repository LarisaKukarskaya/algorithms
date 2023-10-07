def subsequence(s, t):
	position = -1
	for i in s:
		position = t.find(i, position + 1)
		if position == -1:
			return False
	return True

if __name__ == '__main__':
	s = input()
	t = input()
	print(subsequence(s, t))

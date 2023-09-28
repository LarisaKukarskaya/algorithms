def big_number(n, array):
	for i in range(n-1):
		for j in range(0, n-1-i):
			var1 = array[j] + array[j+1]
			var2 = array[j+1] + array[j]
			if var1 < var2:
				array[j], array[j+1] = array[j+1], array[j]
	print(''.join(array))


if __name__ == '__main__':
	n = int(input())
	array = input().split(' ')
	big_number(n, array)	

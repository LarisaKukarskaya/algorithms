def bubble_sort(n, array):
	flag = 1
	for i in range(n-1):
		for j in range(0, n-i-1): 
			if array[j] > array[j+1]:
				array[j], array[j+1] = array[j+1], array[j]
				flag = 1
		if flag == 1:
			for x in array:
				print(x, end=' ')
			print()
			flag = 0

if __name__ == '__main__':
	n = int(input())
	array = [int(num) for num in input().split(' ')]
	bubble_sort(n, array)	

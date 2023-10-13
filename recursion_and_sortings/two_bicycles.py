def daysBicycles(arr, x, left, right):
	if (right <= left and left != 0):
		return -1
	mid = (left + right) // 2
	if (arr[mid] >= x and (arr[mid - 1] < x or mid == 0)):
		return mid + 1
	elif x <= arr[mid]:
		return daysBicycles(arr, x, left, mid)
	else:
		return daysBicycles(arr, x, mid + 1, right)
        
days = int(input())
arr = [int(num) for num in input().split(' ')]
x = int(input())
print(daysBicycles(arr, x, left = 0, right = len(arr)), end=' ')
print(daysBicycles(arr, x * 2, left = 0, right = len(arr)), end=' ')

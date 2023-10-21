def merge_flower_beds(data):
	data.sort()
	
	new_data = []
	start = data[0][0]
	end = data[0][1]
	for i in range(n-1):
		if end<data[i+1][0]:
			new_data.append('{} {}'.format(start, end))
			start = data[i+1][0]
			end = data[i+1][1]
		elif data[i+1][1]>end:
			end = data[i+1][1]
	new_data.append('{} {}'.format(start, end))
	return new_data


if __name__ == '__main__':
	n = int(input())
	if n>=1:
		data=[]
		for i in range(n):
			data.append(tuple([int(x) for x in input().split(' ')]))
	print('\n'.join(merge_flower_beds(data)), end='')

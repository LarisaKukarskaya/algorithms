def letter_combinations(digits):
	
	letter_dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv',
'9':'wxyz'}

	def letters(digits, path, result):
		if digits == '':
			result.append(path)
			return
		for letter in letter_dic[digits[0]]:
			
			path += letter
			letters(digits[1:], path, result)
			path = path[:-1]
	result = []
	letters(digits, '', result)
	for x in result:
		print(x, end=' ')

			
	
if __name__ == '__main__':
	data_vvod = input()
	letter_combinations(data_vvod)

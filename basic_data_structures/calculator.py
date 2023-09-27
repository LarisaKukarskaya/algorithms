import operator

MATH_ACTIONS = {
	        '+': operator.add,
            '-': lambda x, y: x.__rsub__(y),
            '*': operator.mul,
            '/': lambda x, y: y.__floordiv__(x)
}

class NoItems(Exception):
	pass

class Stack():
	def __init__(self):
		self.items = []
		self.size = 0

	@property
	def is_empty(self):
		return self.size == 0

	def push(self, item):
		self.size += 1
		self.items.append(item)
		

	def pop(self):
		if self.is_empty:
			raise NoItems
		self.size -= 1
		return self.items.pop()
		
stack = Stack()
for value in input().split(' '):
			action = MATH_ACTIONS.get(value)
			stack.push(action(stack.pop(), stack.pop()) if action else int(value))
			
if __name__ == '__main__':
	print(stack.pop())

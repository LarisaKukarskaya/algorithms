class SizeError(Exception):
	pass

class Deque():
	def __init__(self, max_size):
		self.queue = [None] * max_size
		self.max_n = max_size
		self.head = 0
		self.tail = -1
		self.size = 0

	@property
	def is_full(self):
		return self.size == self.max_n

	@property
	def is_empty(self):
		return self.size == 0

	def push_back(self, value):
		if self.is_full:
			raise SizeError
		self.tail = (self.tail  + 1) % self.max_n
		self.queue[self.tail] = value 
		self.size += 1
			
	def push_front(self, value):
		if self.is_full:
			raise SizeError
		self.head = (self.head - 1) % self.max_n
		self.queue[self.head] = value
		self.size += 1
		
	def pop_front(self):
		if self.is_empty:
			raise SizeError
		value = self.queue[self.head]
		self.head = (self.head + 1) % self.max_n
		self.size -= 1
		return value

	def pop_back(self):
		if self.is_empty:
			raise SizeError
		value = self.queue[self.tail]
		self.tail = (self.tail - 1) % self.max_n
		self.size -= 1
		return value

def main():
	n = int(input())
	queue_length = int(input())
	s = Deque(queue_length)
	for i in range(n):
		command, *values = input().split()
		op = getattr(s, command)
		values = tuple(map(int, values))
		try:
			result = op(*values)
		except SizeError:
			result = 'error'
		if result is not None:
			print(result)

if __name__ == '__main__':
    main()

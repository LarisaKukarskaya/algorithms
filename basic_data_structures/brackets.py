def is_correct_bracket_seq(self):
	while '()' in self or '[]' in self or '{}' in self:
		self = self.replace('()', '')
		self = self.replace('[]', '')
		self = self.replace('{}', '')
	return not self		

print(is_correct_bracket_seq(input()))

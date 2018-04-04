def is_valid_parentheses(string):
	prevStr = ''
	while prevStr != string:
		prevStr = string
		string = string.replace(r'{}', '')
		string = string.replace('[]', '')
		string = string.replace('()', '')
	print(len(string)==0)

if __name__ == '__main__':
	is_valid_parentheses("()")  # True
	is_valid_parentheses("())")  # False
	is_valid_parentheses("({})")  # True
	is_valid_parentheses("({)}")  # False
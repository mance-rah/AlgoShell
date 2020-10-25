def bracket_match(string):
	stack = []
	count = 0

	for c in string:
		if c == "(":
			stack.append(c)
		elif c == ")" and stack:
			stack.pop()
		else:
			count += 1

	return len(stack) + count
# Write a function that takes a string of braces, and determines if the order of the braces is valid. It should return 
# true if the string is valid, and false if it's invalid. This Kata is similar to the Valid Parentheses Kata, but 
# introduces new characters: brackets [], and curly braces {}. Thanks to @arnedag for the idea! All input strings will 
# be nonempty, and will only consist of parentheses, brackets and curly braces: ()[]{}. 

def match(a, b):
	if a == '(' and b == ')':
		return True
	else:
		return False
	if a == '[' and b == ']':
		return True
	else:
		return False
	if a == '{' and b == '}':
		return True
	else:
		return False
	return False

def balanced(strng):
	stack=[]
	str=list(strng)
	bal=False
	for c in str:
		if c =='(' or c=='{' or c=='[':
			stack.append(str[0])
			str=str[1:]
		if (c == ')' or c=='}' or c==']') and len(stack)>0:
			a = stack.pop()
			b = str[0]
			str=str[1:]
			if not match(a, b):
				return False
			else:
				bal = True
	return bal

def main():
	print(balanced('([}{])'))

if __name__ == "__main__":
	main()
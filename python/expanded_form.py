# You will be given a number and you will need to return it as a string in Expanded Form. For example:
# expanded_form(12) => Should return '10 + 2'
# expanded_form(42) => Should return '40 + 2'
# expanded_form(70304) => Should return '70000 + 300 + 4'

def expanded_form(num):
	num = num[::-1]
	allnums = []
	pos=0
	retstr = ''
	for digit in num:
		if int(digit) > 0:
			num_app = num[pos]
			allnums.append(num_app + '0' * pos)
			pos+=1
		else:
			pos+=1
	allnums = allnums[::-1]
	for n in allnums:
		retstr = retstr + n + ' + '
	return retstr[:-3]

def main():
	num = "70304"
	print(expanded_form(num))

if __name__ == "__main__":
	main()
multiples = {3:'fizz', 5:'buzz'}

def fizzBuzz(multiples, *args):
	for i in range(*args):
		output = ''
		for key in multiples:
			if i % key == 0:
				output += multiples[key]
		if output == '':
			output = i 
		print (output)


def main():
	fizzBuzz(multiples, 1, 50)

if __name__ == "__main__":
	main()
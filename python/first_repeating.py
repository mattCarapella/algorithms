def find_first_repeating(str):
	letters = {}
	for ch in str:
		if ch in letters:
			return ch 
		else:
			letters[ch]=1
	return None


def main():
	str = "abbcacba"
	print(find_first_repeating(str))


if __name__ == "__main__":
	main()
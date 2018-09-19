'''Problem Statement: Given two integers a and b, compute ab (a raised to the power of b) in 
O(log b) time. You can assume that b > 0. Note that log b is linear in the number of bits used 
to represent b so the algorithm will be linear in the size of b. For example, if b=1024 then 
the size of b in bits is 10. '''

import sys

def exp(a, b):
	if b == 1:
		return a
	elif b%2 == 0:
		return exp(a * a, b/2)
	else:
		return a * exp(a * a, (b-1)/2)

def main():
	input_filename = sys.argv[1]
	output_filename = sys.argv[2]
	f = open(input_filename)
	a = int(f.readline())
	b = int(f.readline())
	file_out = open(output_filename, 'w')
	file_out.write(str(exp(a,b)))

if __name__ == "__main__":
    main()
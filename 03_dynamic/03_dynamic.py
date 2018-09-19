# You are working as an assistant for a billionaire who is an avid collector of Marvel action figures. There is a large auction for rare 
# figures coming up that the billionaire would like to attend, but she will be busy in meetings to discuss an upcoming merger so she decides 
# send you to the auction to make purchases on her behalf. She gives you a list of all n items that will appear in the auction along with 
# values quantifying how much each one is worth to her along with enough money to outbid anyone else in attendance (i.e. you don’t have to 
# worry about how much the items will cost, only their values).

# When you get to the auction, you learn a few things about the format. First, you learn the order in which the action figures will be 
# presented. You also realize that each time you buy an item, you will have to fill out some paperwork to finalize your purchase. You will 
# be so busy with this paperwork, that you will not be able to purchase either of the next two items in the auction. Since you have plenty 
# of money, your job is to determine how to maximize the total value of the figures you purchase under this format.

# More formally, you are given a sequence of n items such that each item i has value vi and if you buy item j you can not buy items 
# j + 1 or j + 2. Your goal is to maximize the sum of the values of all the items purchased.

# Give an O(n) runtime algorithm to find a set of items fitting these criteria, prove the correctness of your algorithm, and analyze 
# its runtime.

import sys
import csv

def main():
	
	input_filename = sys.argv[1]
	output_filename = sys.argv[2]
	entries  = []
	max_cost = []	
	max_path = []

	with open(input_filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			entries.append(float(row[1]))

	max_cost.append(0)
	max_cost.append(0)
	max_cost.append(0)
	max_cost.append(entries[0])
	entries.insert(0,0)
	entries.insert(0,0)
	entries.insert(0,0)
	
	for i in range(4, len(entries)):
		a = max_cost[i-1]
		b = max_cost[i-3] + entries[i]
		max_cost.append(max(a, b))
		
	path = []
	i = len(max_cost)-1

	while i >= 3:
		if max_cost[i-1] >= max_cost[i-3] + entries[i]:
			i-=1
		else:
			path.append(i-3)
			i-=3

	path.reverse()	
	file_out = open(output_filename, 'w')
	for i in path:
		file_out.write(str(i)+"\n")

if __name__ == "__main__":
    main()


	  #   		a = max_cost[i-2]
			# b = max_cost[i-3]
			# c = max_cost[i-4]+entries[i]
			# max_cost.append(max(a, b ,c))

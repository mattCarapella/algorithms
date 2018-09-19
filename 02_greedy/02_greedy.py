# You been given the role of a manager for a team of video game speed runners and must prepare for upcoming competition. In this 
# competition your team will compete in Super Mario Bros. on NES and Doom 2 on PC. By the nature of the competition, each team 
# will be given as many PC’s as they need to run Doom 2, but only one NES to run Mario. Furthermore, each contestant must play 
# through Mario in its entirety before they can start playing Doom 2. This means that each team member must play Mario one at a 
# time before they can start playing Doom 2, however  they can all play Doom 2 at the same time. For example, while the first player 
# is playing Mario the rest of the team is standing by without playing anything. Once the first player finishes Mario and moves 
# on to Doom 2, the next player can start Mario. The next player can finish Mario and start playing Doom 2 even if the first player 
# is still playing Doom 2 since there as many PC’s as needed for the entire team to play Doom 2 in parallel.

# Your goal is implement an algorithm that produces a schedule for your team that minimizes the completion time of the team. The 
# completion time for the team is the time taken for all team member to finish both portions of the competition. Specifically, the 
# completion time is the time from when your first player starts Mario until your last player finishes Doom 2. Keep in mind that the 
# last player to finish Doom 2 might not be the last player in your schedule. Each speed runner has a known time for the Mario portion 
# and the Doom 2 portions of the competition and you can assume that each player will exactly match this given time. You must design 
# and implement an algorithm that computes an optimal schedule and runs in O(nlog(n)) time. The players will start playing Mario in the 
# order given in this schedule. 

import sys
import csv

def main():
	
	input_filename  = sys.argv[1]
	output_filename = sys.argv[2]
	entries = []
	
	with open(input_filename) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			 entries.append([int(row[0]), float(row[1]), float(row[2])])

	entries.sort(key=lambda x: x[2])

	file_out = open(output_filename, 'w')
	for entry in entries[::-1]:
		file_out.write(str(entry[0])+'\n')

if __name__ == "__main__":
    main()
# The football.csv file contains the results from the English Premier League. 
# The columns labeled ‘Goals’ and ‘Goals Allowed’ contain the total number of 
# goals scored for and against each team in that season (so Arsenal scored 79 goals 
# against opponents, and had 36 goals scored against them). Write a program to read the file, 
# then print the name of the team with the smallest difference in ‘for’ and ‘against’ goals.

import csv

# open football.csv
with open('football.csv', "rb") as football:
	new_diff = 100
	new_team = ""

	football.readline()
	for row in csv.reader(football):
	
		diff = abs(int(row[5]) - int(row[6]))
		team = row[0]

		if diff < new_diff:
			new_diff = diff
			new_team = team

	print new_team

def main():
	totalBugs = 0
		
	for x in range(7):
		
		if x == 0:
			day = "Sunday"
		elif x == 1:
			day = "Monday"
		elif x == 2:
			day = "Tuesday"
		elif x == 3:
			day = "Wednesday"
		elif x == 4:
			day = "Thursday"
		elif x == 5:
			day = "Friday"
		elif x == 6:
			day = "Saturday"
		
		
		bugs = input("How many bugs did u catch " + day + " :")
		
		totalBugs = totalBugs + bugs
		
	print(totalBugs)
	
	
main()

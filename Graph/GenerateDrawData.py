import csv

csvFile = open("cleaned.csv", "r")
outputfile = open("GPS.csv", "a")
reader = csv.reader(csvFile)
counter = 0
for line in reader:
	if len(line[len(line) - 4]) == 0:
		continue
	writestr = line[len(line) - 4] + ',' + line[len(line) - 3]+'\n'
	outputfile.write(writestr)

csvFile = open("GPS.csv", "r")
outputfile = open("grid.csv", "a")


reader = csv.reader(csvFile)
latilist = []
longlist = []
for line in reader:
	latilist.append(float(line[0]) * 1000000000)
	longlist.append(float(line[1]) * 1000000000)

minlati = min(latilist)
maxlati = max(latilist)
minlong = min(longlist)
maxlong = max(longlist)

levelnum = 500
latilevel = (maxlati - minlati)/levelnum

longlevel = (maxlong - minlong)/levelnum
print(minlati, minlong, latilevel, longlevel)

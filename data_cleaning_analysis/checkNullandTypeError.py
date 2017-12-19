import numpy as np
import csv
from pyspark import SparkContext
sc = SparkContext()

COLNUM = 24

csvfile = sc.textFile('crimedata.csv')
dataOriginal = csvfile.mapPartitions(lambda line: csv.reader(line))

def checkNull(line, index):
	return len(line[index]) == 0

for i in range(0, COLNUM):
	firstfilter = dataOriginal.filter(lambda line: checkNull(line, i))
	print("Empty record in column "+str(i)+": "+str(firstfilter.count()))

def checkNotNumber(line, index):
	result = False
	if len(line[index]) == 0:
		result = False
	else:
		s = line[index]
		for character in s:
			if (not character.isdigit()) and character != '.':
				result = True
	return result

indexlist = [6, 8, 14, 19, 20]
for i in indexlist:
	secondfilter = dataOriginal.filter(lambda line: checkNotNumber(line, i))
	print("Wrong Type in column "+str(i)+": "+str(secondfilter.count()))

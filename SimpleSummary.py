import numpy as np
import csv
from pyspark import SparkContext
sc = SparkContext()

csvfile = sc.textFile('cleaned.csv')
dataOriginal = csvfile.mapPartitions(lambda line:csv.reader(line))

yearAccumulators = []
for i in range(0, 11):
	yearAccumulators.append(sc.accumulator(0))
monthAccumulators = []
for i in range(0, 12):
	monthAccumulators.append(sc.accumulator(0))
hourAccumulators = []
for i in range(0, 24):
	hourAccumulators.append(sc.accumulator(0))

def iterateRecord(record):
	date = record[5]
	year = int(date[-4:]) - 2006
	yearAccumulators[year].add(1)

	month = int(date[0:2]) - 1
	monthAccumulators[month].add(1)
	
	#ignore unknown time	
	if len(record[2]) != 0:
		hour = int(record[2][0:2])
		if hour == 24:
			hour = 0
		hourAccumulators[hour].add(1)

dataOriginal.foreach(iterateRecord)
for i in range(0, 11):
	year = str(2006+i)
	print("Total Incidents Number in year "+year+": "+ str(yearAccumulators[i]))
for i in range(0, 12):
	month = str(1+i)
	print("Total Incidents Number in month "+month+": "+ str(monthAccumulators[i]))
for i in range(0, 24):
        hour = str(i)
        print("Total Incidents Number in hour "+hour+": "+ str(hourAccumulators[i]))

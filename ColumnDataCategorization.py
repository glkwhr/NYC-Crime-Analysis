#! /bin/python
import csv
from pyspark import SparkContext

# extract csv data
sc =SparkContext()
csvFile = sc.textFile('./rows.csv')
crimeData = csvFile.mapPartitions(lambda x: csv.reader(x))

for i in range(6, 19):
	counts = crimeData.map(lambda line: (line[i].encode('utf-8'),1)).reduceByKey(lambda x,y: x+y).sortBy(lambda x: x[1], False)
	counts.saveAsTextFile("./count/count-" + str(i) + ".out")

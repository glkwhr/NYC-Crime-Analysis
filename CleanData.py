import numpy as np
import csv
from pyspark import SparkContext
sc = SparkContext()

COLNUM = 24

csvfile = sc.textFile('crimedata.csv')
dataOriginal = csvfile.mapPartitions(lambda line: csv.reader(line))

def cleanBadData(line):
        flag = True
	
	if line[0] == "CMPLNT_NUM":
                return True

        #Complaint Number should not be NULL
        if len(line[0]) == 0:
                return False

        #Date should not be NULL
        if len(line[1]) == 0:
                return False
	
	#Incident before 2006, ignore
        if int(line[1][-4:]) < 2006:
                return False

        #Report Date should not be NULL
        if len(line[5]) == 0:
                return False

        #KY_CD should not be NULL
        if len(line[6]) == 0:
                return False

        #CRM_ATPT_CPTD_CD should not be NULL
	if len(line[10]) == 0:
                return False

        #BORO_NUM and ADDR_CD should not be NULL simultaneously
        if len(line[13]) == 0 and len(line[14]) == 0:
                return False

        #Check lat/long
        if len(line[21]) > 1 and len(line[22]) > 1:
                if not (40.4<= float(line[21]) <= 40.93 and -74.35 <= float(line[22]) <= -73.69):
                        return False
        return flag

def toCSVLine(line):
        return '*'.join(str(d) for d in line)

filtered = dataOriginal.filter(cleanBadData)
lines = filtered.map(toCSVLine)
lines.saveAsTextFile('cleanedData.csv')

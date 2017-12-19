import csv
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext()
sqlContext = SQLContext(sc)

csvfile = sc.textFile('cleanedData.csv')
data = csvfile.mapPartitions(lambda line: csv.reader(line, delimiter='*'))
header = data.first()
datatail = data.filter(lambda x: x!=header)

schema = sqlContext.createDataFrame(datatail, schema=header)
schema.registerTempTable("ta")

def toCSVLine(line):
        return '*'.join(str(d) for d in line)

# count each type of crime
# DUPLICATED with kycdCount.py
odata = sqlContext.sql("SELECT KY_CD, COUNT(*) FROM ta GROUP BY KY_CD ORDER BY KY_CD")
lines = odata.map(toCSVLine)
lines.saveAsTextFile('kycdProportion.csv')

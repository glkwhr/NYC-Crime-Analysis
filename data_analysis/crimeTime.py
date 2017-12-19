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
        return ','.join(str(d) for d in line)

# Find out how many each type of crimes started at each hour of a day
odata = sqlContext.sql("SELECT KY_CD, HOUR(CMPLNT_FR_TM) AS HR, COUNT(*) FROM ta GROUP BY KY_CD, HOUR(CMPLNT_FR_TM) ORDER BY KY_CD, HR")
lines = odata.map(toCSVLine)
lines.saveAsTextFile('keyCode2Time.csv')

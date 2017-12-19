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

# For each borough, count each type of premises where crimes happened.
odata = sqlContext.sql("SELECT BORO_NM, PREM_TYP_DESC, COUNT(*) AS CNT FROM ta GROUP BY BORO_NM, PREM_TYP_DESC ORDER BY BORO_NM, CNT")
lines = odata.map(toCSVLine)
lines.saveAsTextFile('boroPrem.csv')

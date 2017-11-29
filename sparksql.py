import csv
from pyspark import SparkContext
from pyspark.sql import SQLContext

sc = SparkContext()
sqlContext = SQLContext(sc)

csvfile = sc.textFile('crimedata.csv')
data = csvfile.mapPartitions(lambda line: csv.reader(line))
header = data.first()
datatail = data.filter(lambda x: x!=header)

schema = sqlContext.createDataFrame(datatail, schema=header)
schema.registerTempTable("ta")

#odata = sqlContext.sql("SELECT CMPLNT_NUM FROM ta WHERE CMPLNT_TO_DT=''")
#print(odata.count())

odata = sqlContext.sql("Select PREM_TYP_DESC from ta where LOC_OF_OCCUR_DESC=' ' group by PREM_TYP_DESC")
print(odata.show(100))

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

# (column 6 & 7) check the mapping from KY_CD to OFNS_DESC
# odata = sqlContext.sql("SELECT KY_CD, OFNS_DESC FROM ta GROUP BY KY_CD, OFNS_DESC ORDER BY KY_CD")
# print(odata.show(200, False))

# (column 8 & 9) check the mapping from PD_CD to PD_DESC
# odata = sqlContext.sql("SELECT PD_CD, COUNT(PD_DESC) FROM ta WHERE PD_CD='' OR PD_DESC='' GROUP BY PD_CD, PD_DESC ORDER BY PD_CD")
# odata = sqlContext.sql("SELECT KY_CD, OFNS_DESC FROM ta WHERE PD_CD='' OR PD_DESC='' GROUP BY KY_CD, OFNS_DESC ORDER BY KY_CD")
# print(odata.show(200, False))

# (column 10) check CRM_ATPT_CPTD_CD
# odata = sqlContext.sql("SELECT CMPLNT_NUM,CMPLNT_FR_DT,CMPLNT_FR_TM,CMPLNT_TO_DT,CMPLNT_TO_TM,RPT_DT,KY_CD,OFNS_DESC,PD_CD,PD_DESC,LAW_CAT_CD,JURIS_DESC,BORO_NM,ADDR_PCT_CD FROM ta WHERE CRM_ATPT_CPTD_CD=''")
# print(odata.show(200))

# (column 13) BORO_NM
# odata = sqlContext.sql("SELECT ADDR_PCT_CD, COUNT(ADDR_PCT_CD) FROM ta WHERE BORO_NM='' GROUP BY ADDR_PCT_CD ORDER BY ADDR_PCT_CD")
# print(odata.show(200, False))
# odata = sqlContext.sql("SELECT BORO_NM, ADDR_PCT_CD, COUNT(ADDR_PCT_CD) FROM ta GROUP BY BORO_NM, ADDR_PCT_CD ORDER BY BORO_NM")
# odata = sqlContext.sql("SELECT BORO_NM, ADDR_PCT_CD, COUNT(ADDR_PCT_CD) FROM ta WHERE ADDR_PCT_CD='34' OR ADDR_PCT_CD='100' OR ADDR_PCT_CD='121' OR ADDR_PCT_CD='' OR BORO_NM=''  GROUP BY BORO_NM, ADDR_PCT_CD ORDER BY BORO_NM")
# print(odata.show(200, False))

# (column 15) check the types of PREM_TYP_DESC in rows where LOC_OF_OCCUR_DESC is empty or white space
# odata = sqlContext.sql("SELECT PREM_TYP_DESC FROM ta WHERE LOC_OF_OCCUR_DESC=' ' GROUP BY PREM_TYP_DESC")
# print(odata.show(100))
# odata = sqlContext.sql("SELECT PREM_TYP_DESC FROM ta WHERE LOC_OF_OCCUR_DESC='' GROUP BY PREM_TYP_DESC")
# print(odata.show(100))

# (column 16) check PREM_TYP_DESC
odata = sqlContext.sql("SELECT LOC_OF_OCCUR_DESC, COUNT(*) FROM ta WHERE PREM_TYP_DESC='' GROUP BY LOC_OF_OCCUR_DESC")
print(odata.show(200, False))


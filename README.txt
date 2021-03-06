DATA CLEANING SCRIPTS

1. "checkNullandTypeError.py"
	To run this script, you need to upload the crimedata.csv to HDFS.
	Then use command "spark-submit checkNullandTypeError.py". Information
	we need will be printed on the screen.

2. "CleanData.py"
	Input of this script is the original crimedata.csv.
	Output file is called "cleanedData.csv". Delimiter in this file is "*".
	Data we don't need are no longer in this file.


DATA ANALYSIS SCRIPTS

The following scripts assume that "cleanedData.csv" has been put in HDFS.
To run those scripts, use command "spark-submit FILENAME.py".

1. "boroCrime.py"
	For each borough, count each kind of law category (e.g. felony).
	This script produces output file "boroCrimeLevel.csv".
	Output data columns: (BORO_NM, LAW_CAT_CD, COUNT)

2. "boroKycd.py"
	For each borough, count each type of crime (incident code).
	This script produces output file "boroKycd.csv".
	Output data columns: (BORO_NM, KY_CD, COUNT)

3. "boroPrem.py"
	For each borough, count each type of premises where crimes happened.
	This script produces output file "boroPrem.csv".
	Output data columns: (BORO_NM, PREM_TYPE_DESC, COUNT)

4. "crimeRet.py"
	For each type of crime, count each type of CRM_ATPT_CPTD_CD (e.g. Completed, Attempted).
	This script produces output file "crimeRet.csv".
	Output data columns: (KY_CD, CRM_ATPT_CPTD_CD, COUNT).

5. "crimeTime.py"
	Find out how many each type of crimes started at each hour of a day.
	This script produces output file "keyCode2Time.csv".
	Output data columns: (KY_CD, HOUR(CMPLNT_FR_TM), COUNT)

6. "keycode2desc.py"
	Associate incident code with its description.
	This script produces output file "keyCode2desc.csv".
	Output data columns: (KY_CD, OFNS_DESC, COUNT)

7. "kycdCount.py"
	Count each type of crime (incident code).
	This script produces output file "kycdCount.csv"
	Output data columns: (KY_CD, COUNT)

8. "lawProportion.py"
	For each type of crime level (e.g. felony), count each type of CRM_ATPT_CPTD_CD (e.g. Attempted).
	This script produces output file "lawProportion.csv"
	Output data columns: (LAW_CAT_CD, CRM_ATPT_CPTD_CD, COUNT)


DATA VISUALIZATION
1. /GraphSave/index.html and /GraphSave/draw.js draw2.js ... draw5.js
	These are used to draw the summary charts for report.
	You need to start a Python server to run these code.
	Notice that you have to manually modify the code in index.html to call
	different JS files.

2. "GenerateDrawData.py"
	This script is not for HPC. The input is cleaned data. Output is the two
	columns in the orginal data: latitude and longitude. Information about 
	these data will also be printed on the screen.

3. "drawmap.py"
	This script is not for HPC. It just calls Pillow to draw a
	distribution graph based on the latitude and longitude data. 
	Output is a PNG picture. 

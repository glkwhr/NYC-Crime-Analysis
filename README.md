# NYC-Crime-Analysis
Big Data Analysis (CS-GY-9223) Course Project Report (Partial)

## Content
- [Members](#members)
- [Data Collection](#data-collection)
- [Part I: Data Cleaning](#part-i-data-cleaning)
- [Part II: Data Analysis](#part-ii-data-analysis)
- [How to Run Scripts](#how-to-run-scripts)

## Members
|hw1550         |jz2657         | xz1600|
|:-------------:|:-------------:|:-----:|
|Haoran Wu      |Jiazhen Zhang  |Xu Zhu |

## Data Collection
[NYPD Complaint Data Historic (public safety)](https://data.cityofnewyork.us/Public-Safety/NYPD-Complaint-Data-Historic/qgea-i56i)

## Part I: Data Cleaning
Index | Column Name | Column Description
:----:|:-----------:|:------------:
0 | `CMPLNT_NUM` | Unique ID
1, 2 | `CMPLNT_FR_DT`, `CMPLNT_FR_TM` | Complaint From Date
3, 4 | `CMPLNT_TO_DT`, `CMPLNT_TO_TM` | Complaint To Date
5  | `RPT_DT` | Report Date
6, 7 | `KY_CD`, `OFNS_DESC`	| Criminal ID and Description
8, 9 | `PD_CD`, `PD_DESC` | Police Department Code and Description
10   | `CRM_ATPT_CPTD_CD` | Completed, Attempted but Fail, etc.
11   | `LAW_CAT_CD` | Level: Felony, Misdemeanor, Violation
12 | `JURIS_DESC` | Jurisdiction
13 | `BORO_NM` | Name of BORO where crime happen
14 | `ADDR_PCT_CD` | Address of incident
15 | `LOC_OF_OCCUR_DESC` | Specific location of occurrence
16 | `PREM_TYP_DESC` | Discription of premises
17 | `PARKS_NM` | Name of Park of incident
18 | `HADEVELOPT` | NYCHA Housing Development
19, 20 | `X_COORD_CD`, `Y_COORD_CD` | New York State Plane Coordinate System Coordinates
21, 22 | `Latitude`, `Longitude` | Global Coordinate System
23 | `Lat_Lon` | GPS Coordinates

### CMPLNT_NUM
A unique number used to distinguish individual records.
### CMPLNT_FR_DT, CMPLNT_FR_TM
Date and time, where time can be empty but date cannot, otherwise it doesn’t make sense. Some complaints’ dates are obviously wrong, we should eliminate them also.
### CMPLNT_TO_DT, CMPLNT_TO_TM
Date and time, both can be empty.
### RPT_DT
Date, cannot be empty.
### KY_CD, OFNS_DESC
`KY_CD` is a number (code), and `OFNS_DESC` is a string. `OFNS_DESC` is the description of `KY_CD` (code). According to our analysis of the values, it is possible that for a `KY_CD`, multiple `OFNS_DESC` values exist. Those values slightly different from each other though, they all describe the same type associated with the `KY_CD`. Therefore, as long as `KY_CD` is not empty, `OFNS_DESC` can be empty.

<br>**Example: KY_CD 124 and KY_CD 364 have multiple OFNS_DESC values**

KY_CD | OFNS_DESC
:----:|:--------:
124 | KIDNAPPING & RELATED OFFENSES
124 | KIDNAPPING
124 | KIDNAPPING AND RELATED OFFENSES
124 | \<empty\>
364 | OTHER STATE LAWS (NON PENAL LAW)
364 | AGRICULTURE & MRKTS LAW-UNCLASSIFIED
364 | OTHER STATE LAWS (NON PENAL LA
364 | \<empty\>

### PD_CD, PD_DESC
`PD_CD` is a number (code), and `PD_DESC` is a string. `PD_DESC` is the description of `PD_CD`. Similar to `KY_CD` & `OFNS_DESC`, `PD_DESC` is associated to `PD_CD`. But according to our analysis. In original data, those two columns are either both empty or both non-empty. There are 4909 records where those two are both empty. And when they are both empty, corresponding values of `KY_CD` & `OFNS_DESC` are `101` & `MURDER & NON-NEGL. MANSLAUGHTER`.

### CRM_ATPT_CPTD_CD
`CRM_ATPT_CPTD_CD` is a string and should not be empty. In our analysis, we found 7 records with empty value in this column, which are categorized to dirty data.

### LAW_CAT_CD
`LAW_CAT_CD` is a string and should not be empty. There is no record with this value empty in the original data.

### JURIS_DESC
`JURIS_DESC` is a string and should not be empty. There is no record with this value empty in the original data.

### BORO_NM & ADDR_PCT_CD
`BORO_NM` is a string. `ADDR_PCT_CD` is a number (code). They are related to the each other. When either `BORO_NM` or `ADDR_PCT_CD` is empty, some possible value pairs and count for each pair are as the following:

BORO_NM | ADDR_PCT_CD | Count
:--:|:--:|:--:
\<empty\> | \<empty\> | 387
\<empty\> | 100 | 1
\<empty\> | 121 | 74
\<empty\> | 34 | 1
BRONX | \<empty\> | 1
MANHATTAN | \<empty\> | 2

It doesn’t make sense when they are both empty. So, we categorize records that both BORO_NM and ADDR_PCT_CD are empty to dirty data.

### LOC_OF_OCCUR_DESC & PREM_TYPE_DESC
Both `LOC_OF_OCCUR_DESC` and `PREM_TYPE_DESC` are strings. Together they describe the place where the incidence happens. As long as `PREM_TYPE_DESC` is not empty, `LOC_OF_OCCUR_DESC` is OK to be empty, since it describes direction only.

### PARKS_NM & HADEVELOPT
`PAKS_NM` and `HADEVELOPOPT` are strings. The `PARKS_NM` describe the parks_name where the incidence happens. And `HADEVELOPT` is `NYCHA Housing Development`. Since not all the criminals happen around a park, it can be empty. And so does `HADEVELOPT` .

### X_COORD_CD & Y_COORD_CD
The `X_Coord_CD` & `Y_Coord_CD` are coordinates in New York State Plane Coordinate System. Since we focus more on GPS coordinates, these column values are OK to be empty.

### Latitude, Longitude & Lat_Lon
Those are the coordinates in GPS. `Lat_Lon` is the concatenation of Latitude and Longitude. So Latitude and Longitude should not be empty. And we need to check if the coordinates is inside New York area.


## Part II: Data Analysis
### Incident Number in Each Year
According to the analysis result of the last section. We could find that column 1 represents the complaint date, which is an important feature of offense incidents. So we decide to count incidents number of each year, from 2006 to 2016. Trying to find the trending in last 11 years. Here is the graph of these data: 

![](https://github.com/glkwhr/NYC-Crime-Analysis/blob/master/Graph/GraphSave/YearIncidents.png?raw=true)

From this graph, we could clearly see the number of incidents in last 11 years. Except year 2011 and 2012, generally the number of incidents per year decreases every year. The highest value appears in 2007, which is 530976. The lowest value is the number of 2016: 466455. The number of events has decreased 12.2% since 2006. The security of NYC is getting better and better.

### Incident Number at Each Hour of a Day
![](https://github.com/glkwhr/NYC-Crime-Analysis/blob/master/Graph/GraphSave/HourIncidents.png?raw=true)

### Incident Number in Boroughs
The 14th column in original dataset represents in which borough the incident occurred. As we all know, NYC has five boroughs: Brooklyn, Manhattan, Queens, Bronx and Staten Island. We want to figure out how many incidents happened in each borough in last 11 years. And the percentage of levels in each area. So we plot this graph:

![](https://github.com/glkwhr/NYC-Crime-Analysis/blob/master/Graph/GraphSave/FMVinboros.png?raw=true)

In the graph, we draw groups of bars. Each group represents a borough. The deep red bar in each group is the number of felony incidents in that borough. While the bar with a lighter red represents the number of misdemeanor incidents in the area. And the yellow bar is the number of violation incidents in that borough. 
From the chart we could see that in all five boroughs, misdemeanor always composes the majority of offense incidents. And we can also figure out that felony number is always greater than the violation. In all five boroughs, Brooklyn has the maximum value of all three kinds of crimes and Staten Island has the smallest value among all the boroughs.

### Incidents on the Map
The last three column in the dataset is the accurate latitude and longitude information of where the incident occured. By using these coordinates, we could mark all the incidents in the last 11 years on the map of NYC accurately. 

To draw the points more conveniently, we first find the lower left point and upper right point of the rectangle that can cover the entire NYC. Then divide the width and height into 500 parts and get a `500*500` grid. For each small square in the grid, it has an accumulator. If there is an incident occurs in it, accumulator will add 1. We then render these small squares into pixels and draw a PNG image. Small square that has more incidents will be brighter than square that has less incidents. We then put this PNG image over the map of NYC, here is the result:

![](https://github.com/glkwhr/NYC-Crime-Analysis/blob/master/Graph/GraphSave/incidents_map.png?raw=true)

From the picture above we could see that Manhattan has a high density of offense incidents, also Bronx. For Brooklyn and Queens, the incidents are dense at the border of these two boroughs. In Brooklyn, the south part is better than the north part. In Queens, east part is better than the west part. Another phenomenon is that there are only very few incidents in parks. As for Staten Island, because it has much less people than other boroughs, incidents are fewer and only gathers around the northeast part of the island.

## How to Run Scripts
### Data Cleaning Scripts
- `checkNullandTypeError.py`  
To run this script, you need to upload the `crimedata.csv` to HDFS.
Then use command ` spark-submit checkNullandTypeError.py`. Information we need will be printed on the screen.

- `CleanData.py`  
Input of this script is the original `crimedata.csv`.
Output file is called `cleanedData.csv`. Delimiter in this file is `*`. Data we don't need are no longer in this file.


### Data Analysis Scripts
The following scripts assume that `cleanedData.csv` has been put in HDFS. To run those scripts, use command `spark-submit FILENAME.py`.

- `boroCrime.py`  
  For each borough, count each kind of law category (e.g. felony).  
  This script produces output file `boroCrimeLevel.csv`.  
  Output data columns: (BORO_NM, LAW_CAT_CD, COUNT)  

- `boroKycd.py`  
	For each borough, count each type of crime (incident code).  
	This script produces output file `boroKycd.csv`.  
	Output data columns: (BORO_NM, KY_CD, COUNT)  

- `boroPrem.py`  
	For each borough, count each type of premises where crimes happened.  
	This script produces output file `boroPrem.csv`.  
	Output data columns: (BORO_NM, PREM_TYPE_DESC, COUNT)  

- `crimeRet.py`  
	For each type of crime, count each type of CRM_ATPT_CPTD_CD (e.g. Completed, Attempted).  
	This script produces output file `crimeRet.csv`.  
	Output data columns: (KY_CD, CRM_ATPT_CPTD_CD, COUNT).  

- `crimeTime.py`  
	Find out how many each type of crimes started at each hour of a day.  
	This script produces output file `keyCode2Time.csv`.  
	Output data columns: (KY_CD, HOUR(CMPLNT_FR_TM), COUNT)  

- `keycode2desc.py`  
	Associate incident code with its description.  
	This script produces output file `keyCode2desc.csv`.  
	Output data columns: (KY_CD, OFNS_DESC, COUNT)  

- `kycdCount.py`  
	Count each type of crime (incident code).  
	This script produces output file `kycdCount.csv`  
	Output data columns: (KY_CD, COUNT)  

- `lawProportion.py`  
	For each type of crime level (e.g. felony), count each type of CRM_ATPT_CPTD_CD (e.g. Attempted).  
	This script produces output file `lawProportion.csv`  
	Output data columns: (LAW_CAT_CD, CRM_ATPT_CPTD_CD, COUNT)  


### Data Visualization Scripts
- `/GraphSave/index.html` and `/GraphSave/draw.js` `draw2.js` ... `draw5.js`  
	These are used to draw the summary charts for report.  
	You need to start a Python server to run these code.  
	Notice that you have to manually modify the code in index.html to call different JS files.  

- `GenerateDrawData.py`  
	This script is not for HPC. The input is cleaned data. Output is the two columns in the orginal data: `latitude` and `longitude`. Information about	these data will also be printed on the screen.

- `drawmap.py`  
	This script is not for HPC. It just calls Pillow to draw a distribution graph based on the latitude and longitude data. Output is a PNG picture. 

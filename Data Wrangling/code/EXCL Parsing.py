#####Excel data processing #######
import xlrd
import os

###########################
DIRPATH='C:/Users/vijay/Desktop/ML/Data Wrangling/'
FILENAME="native_Load_2017.xlsx"

datafile=os.path.join(DIRPATH,FILENAME)
workbook=xlrd.open_workbook(datafile)
sheet=workbook.sheet_by_index(0)

data=[[sheet.cell_value(row,col) for col in range(sheet.ncols)] for row in range(sheet.nrows)]
#####
##for col in (sheet.ncols):
##   for row in (sheet.nrows):
##      sheet.cell_value(row,cols)

### Get the 50 row data

for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        if row == 50:
          print sheet.cell_value(row,col)

#####
coast_data=[]
coast_time={}
for i in range(1,sheet.nrows):
    coast_data.append(data[i][1])
    coast_time[data[i][0]]=data[i][1]
minval= min(coast_data)
maxval=max(coast_data)
avgval=sum(coast_data)/len(coast_data)
mindate=[name for name in coast_time if coast_time[name]==minval]
maxdate=[name for name in coast_time if coast_time[name]==maxval]

print minval, mindate, maxval,maxdate,avgval


####### CSV file Parsing##############


##Step 1 -Import module##
import os
import csv

## Define Global Variables##

DIRPATH='C:/Users/vijay/Desktop/ML/Data Wrangling/'
FILENAME='beatles-diskography.csv'

##Step 2 - Parse File ##



def parse_file_method1(datafile):
    data={}
    data1=[]
    counter=0
    with open(datafile,'r') as f:
        for line in islice(f,1,16):
            if counter == 10:
                break
            data={}
            data['Title']=line.split(',')[0]
            data['Released']=line.split(',')[1]
            data['Label']=line.split(',')[2]
            data['UK Chart Position']=line.split(',')[3]
            data['US Chart Position']=line.split(',')[4]
            data['BPI Certification']=line.split(',')[5]
            data['RIAA Certification']=line.split(',')[6]
            print data
            counter =counter +1 
            data1.append(data)

    return data1


def parse_file_method2(datafile):
    data={}
    data1=[]
    counter=0
    with open(datafile,'r') as f:
        header=f.readline().split(",")
        for line in f:
            if counter == 10:
                break
            fields=line.split(",")
            print fields
            data={}
            for i,value in enumerate(fields):
                data[header[i].strip()]=value.strip()
            data1.append(data)

            counter +=1

### using CSV module###

            
def parse_file_method3(datafile):
    data=[] ### List
    with open (datafile, 'r') as f:
        read=csv.DictReader(f)
        for i in read:
                data.append(i)
        return data

             					
def test():
    datafile=os.path.join(DIRPATH,FILENAME)
    d=parse_file_method3(datafile)
    print d

test()
    
        

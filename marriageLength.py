#!/usr/bin/env python3

#using datetime module in this code and re module
from datetime import datetime
import re
import os

#specify file name and path
inputCommand = "zcat AllDivorces.gz"

#write info to a file
outputFile = open("yearLengthTags.txt","w")

#open file to read from
f = os.popen(inputCommand)

#read in each line
lines = f.readlines()

#initialize dictotionary to use later
d = {}

#loop through each line of file and output the dates of marriage and divorce
for line in lines:
    #split each line into fields - it's pipe delimited
    fields = line.split("|")
    
    #only get records with the right amount of fields
    if len(fields)<7:
        continue #goes to the next line in lines

    #only get out the lines with both marriage and divorce dates
    if fields[7] == "" or fields[6] == "" or fields[6]==" / /" or fields[6]=="//" or fields[7]==" / /" or fields[6]=="//":
        continue #goes to next case

    #extract marriage and divorce dates
    try: t1 = fields[7].split("/") #divorce
    except: continue
    try: t2 = fields[6].split("/") #marriage
    except: continue

    #only calculate length for entries with correct format
    if len(t1) == 3 and len(t2) == 3 and int(t1[0]) < 13 and int(t2[0]) < 13:
        #get the year of divorce and marriage
        dyear = t1[2]
        myear = t2[2]
        
        #use datetime module to calculate length of marriages
        divorce_datetime_object = datetime.strptime(fields[7], "%m/%d/%Y")

        marriage_datetime_object = datetime.strptime(fields[6], "%m/%d/%Y")

        length = divorce_datetime_object - marriage_datetime_object
        #convert length to a string
        lengthDays = str(length.days)
        #calculating the amount of years from the days
        year = int(lengthDays)/365.2425

    if int(dyear) > 1979 and int(dyear) < 2011:
        print(str(dyear) +  "|" +  str(year), file = outputFile)

    

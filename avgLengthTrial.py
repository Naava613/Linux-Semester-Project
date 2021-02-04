#!/usr/bin/env python3

#open file to read from
f = open("yearLengthTags.txt")
#file to send output to
outputFile = open("average.txt", "w")

#initialize variables and dicts:
count = {}
d = {}

#loop through file
for line in f:

    fields = line.split('|')
    year = fields[0]
    number = float(fields[1].strip('\n'))
    
    if year in d:
        d[year] += number #total amount per year
        count[year]+=1 #number of entries seen per year
    else:
        d[year]=number
        count[year]=1
        
for year in d:
    average = d[year]/count[year] #divide to get average
    print(str(year) + "|" + str(average), file = outputFile)

    

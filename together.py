#!/usr/bin/env python3
import pyspark

sc = pyspark.SparkContext()
sc.setLogLevel("ERROR")

outputFile = open("readyToPlot.txt", "w")

def getInfo(line):
    fields = line.split('|')
    year = fields[0]
    number = fields[1]
    return (year, number)

#read in from files and put info into RDDs
employ = sc.textFile('unemploymentRates.txt')
marriage = sc.textFile('average.txt')
mappedEmploy = employ.map(getInfo)
mappedMarriage = marriage.map(getInfo)

#put the two RDD's together:
together = mappedEmploy.union(mappedMarriage)

#get all info of same year to be on same line
pipeIt = together.reduceByKey(lambda x,y: (x + "|" + y))

#sort it by year
sort = pipeIt.sortBy(lambda x: x[0], ascending = True)

#get ready to print it out and be fed into plotting file later
rearrange = sort.map(lambda x: (x[0] + "|" + x[1]))

ans = rearrange.take(31)
for a in ans:
    print(a, file = outputFile)


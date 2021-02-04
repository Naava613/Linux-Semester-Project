#!/usr/bin/env python3

import matplotlib.pyplot as plt

#create a figure instance that will later be written to a PDF
f = plt.figure()

#open file for reading
inputFile = open("readyToPlot.txt", "r") #(year|unemployment|divorce)

#initialize lists
x = [] #unemployment
y = [] #divorce

#get list of points to be plotted
for line in inputFile:
    fields = line.split('|')
    value = fields[1]
    x.append(float(value))
    valueY = fields[2]
    y.append(float(valueY))

# do the scatter plot, with specified colors and sizes
plt.scatter(x, y, c = "black") #, s = areas, alpha = 0.5)

# specify the x and y axis labels and title of plot
plt.xlabel("Unemployment Rate")
plt.ylabel("Avg Years Married Before Divorce")
plt.title("Comparing Divorce and Unemployment Rates")

# Save the plot into a PDF file
f.savefig("finalPlot.pdf")

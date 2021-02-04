#!/usr/bin/gawk -f

BEGIN{
    #set output to be pipe delimited
    FS = "\t"
    OFS = "|"

    #loop through Data.txt file to get unemployment rate per year
    while ((getline < "Data.txt") > 0){
	#only want the lines of the years and rates, not the other extra info.
	
       	if ($1 ~ /^[0-9]/){
	    year = $1
	    for (i=2; i<=13; i++){
		#add up each month's rate for that year
		rate[year] += $i
	    }
    }
    }

    #do for loop to print it all out
    for (year in rate){
	yearAvg = rate[year]/12
	#only print out until 2010
	if (year<2011)
	    print year, yearAvg > "unemploymentRates.txt"
    }
}

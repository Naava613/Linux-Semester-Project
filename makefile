#Graph file is the main goal
all: finalPlot.pdf

#temp files made during the process to be cleaned up
clean:
	rm yearLengthTags.txt unemploymentRates.txt average.txt readyToPlot.txt

finalPlot.pdf: readyToPlot.txt plotProject.py
	python3 ./plotProject.py

#putting all the information together - ouput: year|unemployment|divorce
readyToPlot.txt: average.txt unemploymentRates.txt together.py
	./together.py

#calculate avg years of marriages in same year - outputs 30 lines of year|avg
average.txt: yearLengthTags.txt avgLengthTrial.py
	./avgLengthTrial.py

#calculate length of marriages of those who divorced - outputs year|length of each entry
yearLengthTags.txt: AllDivorces.gz marriageLength.py
	./marriageLength.py

#calculating the avg rate of unemployment per year - ouputs year|rate
unemploymentRates.txt: Data.txt unemployment.awk
	./unemployment.awk


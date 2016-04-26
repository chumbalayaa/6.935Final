import os
import csv
import datetime
import time

filesToAnalyze = os.listdir('./datesFixed')

def average(lst):
	total = 0
	for x in lst:
		total += float(x)
	return total/len(lst)

for fta in filesToAnalyze:
	with open('./datesFixed/'+fta, 'r') as input:
		with open('./dataByDate/'+fta.replace('_sentiment', ''), 'w') as output:
			writer = csv.writer(output)
			reader = csv.reader(input)

			dateData = {}
			headers = next(reader)

			for row in reader:
				date = row[7]
				if row[4] == 'pos':
					sentiment = 1
				else:
					sentiment = 0
				pos = row[5]
				neg = row[6]

				if date not in dateData.keys():
					dateData[date] = {
					'sentiment': [sentiment],
					'pos': [pos],
					'neg': [neg]
					}
				else:
					dateData[date]['sentiment'].append(sentiment)
					dateData[date]['pos'].append(float(pos))
					dateData[date]['neg'].append(float(neg))
			for key in dateData.keys():
				dateData[key]['sentAverage'] = average(dateData[key]['sentiment'])
				dateData[key]['posAverage'] = average(dateData[key]['pos'])
				dateData[key]['negAverage'] = average(dateData[key]['neg'])

			all = []
			all.append(['date', 'sentiment', 'pos', 'neg'])
			for key in dateData.keys():
				all.append([key, dateData[key]['sentAverage'], dateData[key]['posAverage'], dateData[key]['negAverage']])

			writer.writerows(all)


 


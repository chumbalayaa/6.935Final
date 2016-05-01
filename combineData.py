import os
import csv
import datetime
import time

def average(lst):
	total = 0
	for x in lst:
		total += float(x)
	return total/len(lst)

filesToAnalyze = os.listdir('./dataByDate')

combinedData = {}

for fta in filesToAnalyze:
	with open('./dataByDate/'+fta, 'r') as input:
		reader = csv.reader(input)
		headers = next(reader)

		for row in reader:
			date = row[0]
			sentiment = row[1]
			pos = row[2]
			neg = row[3]

			if date not in combinedData.keys():
				combinedData[date] = {
					'sentiment': [float(sentiment)],
					'pos': [float(pos)],
					'neg': [float(neg)]
				}
			else:
				combinedData[date]['sentiment'].append(float(sentiment))
				combinedData[date]['pos'].append(float(pos))
				combinedData[date]['neg'].append(float(neg))

			for key in combinedData.keys():
				combinedData[key]['sentAverage'] = average(combinedData[key]['sentiment'])
				combinedData[key]['posAverage'] = average(combinedData[key]['pos'])
				combinedData[key]['negAverage'] = average(combinedData[key]['neg'])

with open('./combinedTwitterData/combinedData.csv', 'w') as output:
	writer = csv.writer(output)

	all = []
	all.append(['date', 'sentiment', 'pos', 'neg'])
	for key in combinedData.keys():
		all.append([key, combinedData[key]['sentAverage'], combinedData[key]['posAverage'], combinedData[key]['negAverage']])

	writer.writerows(all)



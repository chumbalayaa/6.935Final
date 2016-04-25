import os
import csv
import datetime
import time

filesToAnalyze = os.listdir('./twitterData')

for fta in filesToAnalyze:
        with open('./sentimentData/'+fta, 'r') as input:
                with open('./datesFixed/'+fta, 'w') as output:
                        writer = csv.writer(output)
                        reader = csv.reader(input)
                        all = []
                        row = next(reader)
                        row.append('StockDate')
                        all.append(row)

                        for row in reader:
                                aTime = time.strptime(row[1], '%Y-%m-%d %H:%M:%S')
                                theTime = datetime.datetime(*aTime[:6])
                                if theTime.hour <= 4:
                                        finalTime = time.strftime("%Y-%m-%d", theTime.timetuple())
                                        row.append(finalTime)
                                else:
                                        theTime = theTime + datetime.timedelta(days = 1)
                                        finalTime = time.strftime("%Y-%m-%d", theTime.timetuple())
                                        row.append(finalTime)
                                all.append(row)

                        writer.writerows(all)

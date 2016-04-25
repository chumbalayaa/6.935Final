from training import trainData
from training import trainFake

cl = trainData()
#cl = trainFake()

import os
import csv

filesToAnalyze = os.listdir('../twitterData')

for fta in filesToAnalyze:
	print('Analyzing', fta)
	with open('../twitterData/'+fta, 'r') as input:
		with open('../sentimentData/'+fta.replace('tweets', 'sentiment'), 'w') as output:
                        writer = csv.writer(output)
                        reader = csv.reader(input)
                        all = []
                        row = next(reader)
                        row.append('Sentiment')
                        row.append('ProbPos')
                        row.append('ProbNeg')
                        all.append(row)

                        i = 0
                        for row in reader:
                                if i%100 == 0:
                                        print(i)
                                row.append(cl.classify(row[3]))
                                prob_dist = cl.prob_classify(row[3])
                                row.append(round(prob_dist.prob("pos"), 4))
                                row.append(round(prob_dist.prob("neg"), 4))
                                all.append(row)
                                i+=1

                        writer.writerows(all)

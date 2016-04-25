from textblob.classifiers import NaiveBayesClassifier
from pos_tweets import pos_tweets
from neg_tweets import neg_tweets

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def trainData():

	totalData = []
	#1000 of each
	amazon_data = []
	with open('datasets/amazon_cells_labelled.txt') as f:
		for line in f.readlines():
			values = line.split('\t')
			if RepresentsInt(values[1]):
				if int(values[1]) == 1:
					amazon_data.append((values[0], 'pos'))
				elif int(values[1]) == 0:
					amazon_data.append((values[0], 'neg'))
				else:
					print("ERROR", values[1])
	print('Updating with amazon')

	imdb_data = []
	with open('datasets/imdb_labelled.txt') as f:
		for line in f.readlines():
			values = line.split('\t')
			if RepresentsInt(values[1]):
				if int(values[1]) == 1:
					imdb_data.append((values[0], 'pos'))
				elif int(values[1]) == 0:
					imdb_data.append((values[0], 'neg'))
				else:
					print("ERROR", values[1])
	print('Updateing with IMDB')

	yelp_data = []
	with open('datasets/yelp_labelled.txt') as f:
		for line in f.readlines():
			values = line.split('\t')
			if RepresentsInt(values[1]):
				if int(values[1]) == 1:
					yelp_data.append((values[0], 'pos'))
				elif int(values[1]) == 0:
					yelp_data.append((values[0], 'neg'))
				else:
					print("ERROR", values[1])
	print('Updating with Yelp')
	totalData = pos_tweets + neg_tweets + amazon_data + imdb_data + yelp_data
	cl = NaiveBayesClassifier(totalData)
	return cl

def trainFake():
	cl = NaiveBayesClassifier(pos_tweets+neg_tweets)
	return cl


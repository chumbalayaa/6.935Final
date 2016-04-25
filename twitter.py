
import tweepy
import csv

consumer_key = 'fI4o0YBQXZ9tmIzXl0UBCyTsP'
consumer_secret = 'bvu2lHvTsdbAFot995M5EKjcT89gxOLbum50Vf4N4malNFvDN7'
access_token = '1571130690-5IA6Twm576E1PH52AGRguXiCIZllV0vbUMmHAao'
access_secret = 'jDz0TVMTVwX9ANOPSGWKBimSzxy8DUl3HVcNPhjkeQ3zJ'
  
def get_all_tweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print("getting tweets before %s" % (oldest))

		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)

		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print("...%s tweets downloaded so far" % (len(alltweets)))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.retweet_count, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow([bytes("id", "UTF-8"), bytes("created_at", "UTF-8"), bytes("retweet_count", "UTF-8"), bytes("text", "UTF-8")])
		writer.writerows(outtweets)
	
	pass


if __name__ == '__main__':
	#pass in the username of the account you want to download
        advisors = ["ReformedBroker", "hjudeboudreaux", "jjeffrose", "ClarkHoward", "behaviorgap"]
        another = ["cnbc", "stocktwits", "WSJMarkets", "FARNOOSH", "sophiabera", "IBDinvestors"]
        second = ["stephanie_link", "bespokeinvest", "benzinga", "breakoutstocks",
  		"DaveRamsey", "moorehn", "CateyHill", "TimMaurer", "mandiwoodruff",
  		"nytimesbusiness", "JeanChatzky"]
        last = ['KimberlyPalmer']
        for ad in last:
            print(ad)
            get_all_tweets(ad)

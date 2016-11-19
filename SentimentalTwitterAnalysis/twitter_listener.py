import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
import predict
import matplotlib.pyplot as plt
import numpy as np
 
consumer_key = 'N3SXBClTt9tFAk98dkN0Ig6WW'
consumer_secret = 'SInQ4RpBMiVjhoK3CJP3YgUmMLn90GoMtEAdwl1RuEcLbJ7ELK'
access_token = '478290418-4gMvS4oxOU2aYpt1YCxlcIpxZsa3VONWy77GUYFc'
access_secret = 'Kz2bvZsmJGC9tfsWzs1nAY9G7DdATX4NP5uW8xOcF3oj6'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)
 
class MyListener(StreamListener):
	def on_data(self, data):
		d = json.loads(data)
		tweet_text = d["text"]
		print(tweet_text)
		prediction = predict.classifier.classify(predict.extract_features(tweet_text.split()))
		global positive_tweets
		global negative_tweets
		if prediction == "positive":
			positive_tweets += 1
		elif prediction == "negative":
			negative_tweets += 1
		print(prediction)
		labels = 'Positive', 'Negative'
		data = [positive_tweets, negative_tweets]
		colors = ['yellowgreen', 'gold']
		explode = (0, 0)
		plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
		plt.draw()
		return True

	def on_error(self, status):
		print(status)
		return True

positive_tweets = 0
negative_tweets = 0

labels = 'Positive', 'Negative'
data = [positive_tweets, negative_tweets]
colors = ['yellowgreen', 'gold']
explode = (0, 0)
plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.ion()
plt.show()

data = [1, negative_tweets]
plt.pie(data, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
plt.show()

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#AIRuben2016'])
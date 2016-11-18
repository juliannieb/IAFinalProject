import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json
 
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
		print(d["text"])
		return True

	def on_error(self, status):
		print(status)
		return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#AIRuben2016'])
import sys
import re
import nltk
import pickle
import pickle

def extract_features(tweet):
	tweet_words = set(tweet)
	features = {}
	for word in word_features:
		features["%s" % word] = (word in tweet_words)
	return features

f = open('word_features.pickle', 'rb')
word_features = pickle.load(f)
f.close()

f = open('naive_bayes_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

#print classifier.show_most_informative_features(32)

tweet = "I hate this shit"
tweet = tweet.lower()
print classifier.classify(extract_features(tweet.split()))
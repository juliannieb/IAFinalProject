import sys
import re
import nltk
import pickle
import pickle

def get_words_in_tweets(tweets):
	all_words = []
	for (words, sentiment) in tweets:
		all_words.extend(words)
	return all_words

def get_word_features(word_list):
	word_list = nltk.FreqDist(word_list)
	word_features = word_list.keys()
	return word_features

def extract_features(tweet):
	tweet_words = set(tweet)
	features = {}
	for word in word_features:
		features["%s" % word] = (word in tweet_words)
	return features

def clean_word(word):
	word = word.lower()
	word = word.strip(".,#")
	return word

data = []

for line in sys.stdin:
	line = re.split('","', line)
	line[0] = line[0][1:]
	line[1] = line[1][:-2]
	if line[0] == '0':
		line[0] = "negative"
	else:
		line[0] = "positive"
	data.append((line[0], line[1]))

tweets = []

for (sentiment, tweet) in data:
	tweet_filtered = [clean_word(word) for word in tweet.split() if ((len(word) >= 3) and (not '@' in word))]
	tweets.append((tweet_filtered, sentiment))

word_features = get_word_features(get_words_in_tweets(tweets))

f = open('naive_bayes_classifier.pickle', 'rb')
classifier = pickle.load(f)
f.close()

print classifier.show_most_informative_features(32)

tweet = "I hate this shit"
tweet = tweet.lower()
print classifier.classify(extract_features(tweet.split()))
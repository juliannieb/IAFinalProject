import predict
import re
import nltk

def clean_word(word):
	word = word.lower()
	word = word.strip(".,#")
	return word

data = []

with open('test_data.csv', 'r') as cleaned_data_file:
	for line in cleaned_data_file:
		line = re.split('","', line)
		line[0] = line[0][1:]
		line[1] = line[1][:-2]
		if line[0] == '0':
			line[0] = "negative"
		else:
			line[0] = "positive"
		data.append((line[0], line[1]))
	cleaned_data_file.close()

tweets = []

for (sentiment, tweet) in data:
	tweet_filtered = [clean_word(word) for word in tweet.split() if ((len(word) >= 3) and (not '@' in word))]
	tweets.append((tweet_filtered, sentiment))

correct = 0
count = 0

for tweet in tweets:
	tweet_text = tweet[0]
	prediction = predict.classifier.classify(predict.extract_features(tweet_text))
	answer = tweet[1]
	if prediction == answer:
		correct += 1
	count += 1

accuracy = 0
if count > 0:
	accuracy = float(correct) / float(count)
print(accuracy)
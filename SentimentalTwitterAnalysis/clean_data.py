import sys
import re

max_positive = 5000
max_negative = 5000

count_positive = 0
count_negative = 0

with open('training_1600000_data.csv', 'r') as training_data_file:
	with open('cleaned_training_data.csv', 'w') as cleaned_data_file:
		for line in training_data_file:
			line = re.split('","', line)
			line[0] = line[0][1:]
			line[5] = line[5][:-2]
			if line[0] == '0':
				if count_positive < max_positive:
					cleaned_data_file.write('"%s","%s"\n' % (line[0], line[5]))
					count_positive += 1
			else:
				if count_negative < max_negative:
					cleaned_data_file.write('"%s","%s"\n' % (line[0], line[5]))
					count_negative += 1
		cleaned_data_file.close()
	training_data_file.close()
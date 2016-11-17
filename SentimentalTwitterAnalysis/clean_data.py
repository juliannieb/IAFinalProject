import sys
import re

max_positive = 5000
max_negative = 5000

count_positive = 0
count_negative = 0

for line in sys.stdin:
	line = re.split('","', line)
	line[0] = line[0][1:]
	line[5] = line[5][:-2]
	if line[0] == '0':
		if count_positive < max_positive:
			print('"%s","%s"' % (line[0], line[5]))
			count_positive += 1
	else:
		if count_negative < max_negative:
			print('"%s","%s"' % (line[0], line[5]))
			count_negative += 1
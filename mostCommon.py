import json
import itertools
from collections import Counter


def most_common():
	file = open('nnn.json', 'r', encoding="utf8")
	data_file = json.load(file)

	words_in_one_list = []

	for line in data_file:
		#words = line['content'].split()
		#print(words)
		#words_in_one_list.extend(line)
	#print(words_in_one_list)
		c = Counter(data_file)
	# print(c)
	# top10 = c.most_common(10)

	# with open('ccc.json', 'w', encoding='utf-8') as outfile:
		# json.dump(top10,outfile,indent=2, ensure_ascii=False)
			

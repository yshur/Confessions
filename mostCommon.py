import json
import itertools
from collections import Counter


def most_common():
	file = open('data1College.json', 'r', encoding="utf8")
	python_obj = json.load(file)

	words_in_one_list = []

	for line in python_obj:
		words = line['content'].split()
		#print(words)
		words_in_one_list.extend(words)
	#print(words_in_one_list)
	c = Counter(words_in_one_list)
	print(c)
	top10 = c.most_common(10)

	with open('top10Colleges.json', 'w', encoding='utf-8') as outfile:
		json.dump(top10,outfile,indent=2, ensure_ascii=False)
			

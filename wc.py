import urllib.request
import re
import json
import operator
import string

file = open('data100.json', 'r', encoding="utf8")
data_file = json.load(file)
di = dict()
all_occurrences = []

for line in data_file:

	words = line['content'].split()
	for word in words:
		word = re.sub(r'\W+',"", word)
		if word != "":
			if word in di:
				di[word] = di[word]+1
			else:
				di[word]=1

for word in list(di):
	if di[word] < 50:
		del di[word]
for word in list(di):
	if word.isdigit():
		del di[word]

try: 
	for key,value in di.items():
		occurrence = {}
		occurrence['word'] = key
		occurrence['total'] = value
		all_occurrences.append(occurrence)

except AttributeError:
		pass
		
print(di, '\n')
print('-------------------------------------------------------------------------------------------------------------------------')
	
with open('allWordsMoreThan50.json', 'w', encoding='utf-8') as outfile:
	json.dump(all_occurrences,outfile, indent=2, ensure_ascii=False)
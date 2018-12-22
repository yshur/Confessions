import urllib.request
import re
import json
import operator
def getWordsCounter(confessionsSource):

	file = open('data1.json', 'r', encoding="utf8")
	python_obj = json.load(file)
	#print(python_obj)
	di = dict()
	for line in python_obj:
		words = line['content'].split()
		#words.remove(words[0])
		if line['source'] == confessionsSource:
			#print(line['source'])
			for word in words:
				if word in di:
					di[word] = di[word]+1
				else:
					di[word]=1
	
	try: 
		occurrence = {}
		occurrence['source'] = confessionsSource
		occurrence['word_occurrence'] = di
		all_occurrences.append(occurrence)

	except AttributeError:
			pass
			
	print('#',confessionsSource,'# -> Before sorting')
	print(di, '\n')
	print('-------------------------------------------------------------------------------------------------------------------------')
	print('#',confessionsSource,'# -> After sorting')
	
	sorted_d = sorted(di.items(), key=lambda x: x[1])
	print(sorted_d, '\n')

all_occurrences = []				
confessionsList = ["ShenkarConfessions","bezalelconf","TechnionConfessions"]

for confPage in confessionsList:
	getWordsCounter(confPage)
	
with open('wordsCounter.json', 'w', encoding='utf-8') as outfile:
	json.dump(all_occurrences, outfile, ensure_ascii=False)
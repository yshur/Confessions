import urllib.request
import re
import json
import operator
import csv

def getWordsCounter(confessionsSource):

	file = open('data100.json', 'r', encoding="utf8")
	python_obj = json.load(file)
	#print(python_obj)
	di = dict()
	for line in python_obj:
		words = line['content'].split()
		#words.remove(words[0])
		if line['source'] == confessionsSource:
			#print(line['source'])
			for word in words:
				word = word.replace('.','')
				word = word.replace(',','')
				word = word.replace('-','')
				word = word.replace(':','')
				word = word.replace(')','')
				word = word.replace('(','')
				word = word.replace(';','')
				word = word.replace('!','')
				word = word.replace('?','')
				if word in di:
					di[word] = di[word]+1
				else:
					di[word]=1
	
	
	for word in list(di):
		if di[word] < 10:
			del di[word]

	try: 
		occurrence = {}
		occurrence['source'] = confessionsSource
		occurrence['word_occurrence'] = di
		all_occurrences.append(occurrence)

	except AttributeError:
			pass
			
	print('#',confessionsSource,'#')
	print(di, '\n')
	print('-------------------------------------------------------------------------------------------------------------------------')
		
all_occurrences = []				
confessionsList = ["ShenkarConfessions","bezalelconf","IDCHerzliyaConfessions","sapirconfession","telhaiconfessions","hitconfessionsisrael","RuppinConfession","HUIConfessions","TechnionConfessions","ArielUConfessions","tel.aviv.university.confessions","BGUConfession", "biuconfessions2018","HUJI.Confessions" ]

for confPage in confessionsList:
	getWordsCounter(confPage)

# with open('wordsCounterMoreThanTen.json', 'w', encoding='utf-8') as outfile:
	# json.dump(all_occurrences,outfile, indent=2, ensure_ascii=False)
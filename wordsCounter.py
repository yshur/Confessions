import urllib.request
import re
import json

def getConfessions(confessionsSource):

	file = open('data1.json', 'r', encoding="utf8")
	di = dict()
	for line in file:
		if re.search('content', line):
			words = line.split()
			for word in words:
				if word in di:
					di[word] = di[word]+1
				else:
					di[word]=1
					#print (word, di[word])
	with open('CountWords.json', 'w', encoding='utf-8') as outfile:
		json.dump(di, outfile, ensure_ascii=False)
				
confessionsList = ["ShenkarConfessions","bezalelconf","TechnionConfessions"]

for confPage in confessionsList:
	getConfessions(confPage)
			



	
	




	

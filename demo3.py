import urllib.request
import re
import json
import itertools
# import hebrewStopwords000 as hs

# file = open('data1College.json', 'r', encoding="utf8")
# python_obj = json.load(file)
# list = []

# for line in python_obj:
	# words = line['content'].split()
	# list.extend(words)	
	
# with open('wordsListCollege.json', 'w', encoding='utf-8') as outfile:
    # data = json.dump(list, outfile,indent=2, ensure_ascii=False)	
	
file1 = open('hebrewStopwords.json', 'r', encoding="utf8")
data1 = json.load(file1)
file2 = open('wordsListCollege.json', 'r', encoding="utf8")
data2 = json.load(file2)
print(len(data2))
list = []
for word in data2:
	if word.isdigit():
		del word
	
for x in data1:
	for word in data2:
		word = word.replace('.','')
		word = word.replace(',','')
		word = word.replace('-','')
		word = word.replace(':','')
		word = word.replace(')','')
		word = word.replace('(','')
		word = word.replace(';','')
		word = word.replace('!','')
		word = word.replace('?','')
		word = word.replace('*','')
		word = word.replace('#','')
		
		if word not in data1:
			list.append(word)
			
with open('wordsListCollege1.json', 'w', encoding='utf-8') as outfile:
	data = json.dump(list, outfile,indent=2, ensure_ascii=False)	
		

		


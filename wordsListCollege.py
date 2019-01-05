import urllib.request
import re
import json
import itertools



def wordsList():
	def getWordsListCollege():
		file = open('data1College.json', 'r', encoding="utf8")
		data_file = json.load(file)
		list = []

		for line in data_file:
			words = line['content'].split()
			list.extend(words)	
			
		with open('yy.json', 'w', encoding='utf-8') as outfile:
			data = json.dump(list, outfile,indent=2, ensure_ascii=False)	
			
	def getWordsListCollegeAfterRemoveStopWords():

		file1 = open('hebrewStopwords.json', 'r', encoding="utf8")
		data_file1 = json.load(file1)
		
		file2 = open('yy.json', 'r', encoding="utf8")
		data_file2 = json.load(file2)

		list = []
			
		for df2 in data_file2:
				
			df2 = re.sub(r'\W+', "", df2)	
			if df2 not in data_file1:
				list.append(df2)
			
					
		with open('pp.json', 'w', encoding='utf-8') as outfile:
			data = json.dump(list, outfile,indent=2, ensure_ascii=False)	
			
	getWordsListCollege()
	getWordsListCollegeAfterRemoveStopWords()


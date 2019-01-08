from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
import json
import re



browser = webdriver.Firefox()
browser.get('https://www.ranks.nl/stopwords/hebrew')
stopwords = []
element = browser.find_elements_by_class_name('panel-body')

for i in element:
	words = i.find_elements_by_tag_name('td')
	word = words[0].text
	print(word)
	stopword = word.split()
	print(stopword)
	try:  
		x = {}
		x["words"] = stopword
		stopwords.append(x)
		
	except AttributeError:
			pass

				
with open('hebrewStopwords.json', 'w', encoding='utf-8') as outfile:
    data = json.dump(stopwords, outfile, ensure_ascii=False)

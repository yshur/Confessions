from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys


def getConfessions(confessionsSource):
	browser.get('https://www.facebook.com/'+confessionsSource+'/')

	SCROLL_PAUSE_TIME = 0.5
	
	# Get scroll height
	last_height = browser.execute_script("return document.body.scrollHeight")
	i = 1

	while True:
		# Scroll down to bottom
		browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

		# Wait to load page
		time.sleep(SCROLL_PAUSE_TIME)

		# Calculate new scroll height and compare with last scroll height
		new_height = browser.execute_script("return document.body.scrollHeight")
		# if new_height == last_height:  break
		last_height = new_height
		i = i+1
		if(i>10):
			break
		
	element = browser.find_elements_by_class_name('userContentWrapper')

	for i in element:
		element1 = i.find_element_by_class_name('timestampContent')
		
		element2 = i.find_element_by_tag_name('p')
		element2 = element2.text
		element2 = element2.replace("\n", " ")
		element2 = element2.replace('"', "'")
		
		element3 = i.find_elements_by_class_name('UFILikeSentenceText')
		if len(element3) == 0:
			element3 = '0'
		else:
			element3 = element3[0].find_element_by_tag_name('span')
			element3 = element3.text
		
		element4 = i.find_elements_by_class_name('UFIShareLink')
		if len(element4) == 0:
			element4 = '0'
		else:
			element4 = element4[0].text	
		element5 = i.find_elements_by_class_name('UFIPagerLink')
		if len(element5) == 0:
			element5 = '0'
		else:
			element5 = element5[0].text		
		
		with open(filename, 'a', encoding='utf-8') as f:
			print('{', file=f)
			print('\"source\":\"'+confessionsSource+'\",', file=f)
			print('\"time\":\"'+element1.text+'\",', file=f)
			print('\"content\":\"'+element2+'\",', file=f)
			print('\"likes\":\"'+element3+'\",', file=f)
			print('\"shares\":\"'+element4+'\",', file=f)
			print('\"comments\":\"'+element5+'\"', file=f)
			print('},', file=f)




filename = "confessions.json"
browser = webdriver.Firefox()
confessionsList = ["ShenkarConfessions","bezalelconf","TechnionConfessions"]
with open(filename, 'a', encoding='utf-8') as f:
	print('[', file=f)
for i in confessionsList:
	getConfessions(i)
with open(filename, 'rb+') as filehandle:
	filehandle.seek(-3, os.SEEK_END)
	filehandle.truncate()
with open(filename, 'a', encoding='utf-8') as f:
	print(']', file=f)	
browser.quit()


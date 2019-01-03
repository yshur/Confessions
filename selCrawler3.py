from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
import json
import re
import datetime
import numpy as np

def getConfessions(confessionsSource):
	print(confessionsSource)
	posts 			= []
	browser.get('https://www.facebook.com/'+confessionsSource+'/')

	SCROLL_PAUSE_TIME = 1.5

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
		if(i>400):
			break

	element = browser.find_elements_by_class_name('userContentWrapper')

	for i in element:
		time1 = i.find_element_by_class_name('_5ptz')
		utime = time1.get_attribute("data-utime")
		utime = time1.get_attribute("data-utime")
		time2 = datetime.datetime.fromtimestamp(int(utime)).strftime('%Y-%m-%d %H:%M:%S')
		print(time2)

		contents = i.find_elements_by_tag_name('p')
		if len(contents) == 0:
			content = '';
		else:
			content = contents[0].text
			text_exposed_show = contents[0].find_elements_by_class_name('text_exposed_show')
			if len(text_exposed_show) > 0:
				content = content+text_exposed_show[0].text
			content = content.replace("\n", " ")
			content = content.replace("...", " ")
			content = content.replace('"', "'")

		likes = i.find_elements_by_class_name('UFILikeSentenceText')
		if len(likes) == 0:
			likes = 0
		else:
			likes = likes[0].find_element_by_tag_name('span')
			likes = likes.text
			likesNum = [int(s) for s in likes.split() if s.isdigit()]
			if len(likesNum) > 0:
				likesNum = likesNum[0]
			else:
				likesNum = 0
			likesArr = likes.split(',')
			likes = likesNum+len(likesArr)

		shares = i.find_elements_by_class_name('UFIShareLink')
		if len(shares) == 0:
			shares = 0
		else:
			shares = shares[0].text
			shares = [int(s) for s in shares.split() if s.isdigit()]
			if len(shares) > 0:
				shares = shares[0]
			else:
				shares = 1

		comments = i.find_elements_by_class_name('UFIPagerLink')
		if len(comments) == 0:
			comments = 0
		else:
			comments = comments[0].text
			comments = [int(s) for s in comments.split() if s.isdigit()]
			if len(comments) > 0:
				comments = comments[0]
			else:
				comments = 1

		words = []
		for word in set(content.split()):
			word = processWord(word)
			if len(word) > 0:
				words.append(word)
			
		meanWords = list(set(words) - set(stopWords))
		
		try:
			post = {}
			post["source"] = confessionsSource
			post["time"] = time2
			post["unix-time"] = utime
			post["content"] = content
			post["likes"] = likes
			post["shares"] = shares
			post["comments"] = comments
			post["sum_like"] = likes+shares+comments
			post["words"] = words
			post["mean_words"] = meanWords
			post["issues"] = []
			posts.append(post)

		except AttributeError:
			pass

	filename = confessionsSource+".json"
	with open(filename, mode='w', encoding='utf-8') as f:
	    json.dump(posts, f, indent=2, ensure_ascii=False)

def isChar(char):
	# if char >= '0' and char <= '9':
		# return 1;
	if char >= 'a' and char <= 'z':
		return 1;
	if char >= 'A' and char <= 'Z':
		return 1;
	if char >= 'א' and char <= 'ת':
		return 1;
	return 0
	
def processWord(word):
	chars = list(word)
	word = ''
	for chr in chars:
		if isChar(chr) == 1:
			word = word+chr
	return word
	
browser 		= webdriver.Firefox()
confessionsList = ["HUJI.Confessions"]
# confessionsList = ["HUIConfessions","TechnionConfessions","ArielUConfessions","tel.aviv.university.confessions","BGUConfession", "biuconfessions2018","HUJI.Confessions" ]
stopFile = open("hebrewStopwords.json", mode='r', encoding='utf-8')
stopWords = json.load(stopFile)

for confPage in confessionsList:
	posts = []
	getConfessions(confPage)
# browser.quit()

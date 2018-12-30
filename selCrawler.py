from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
import json
import re

def crawler():
	def getConfessions(confessionsSource):
		print(confessionsSource)
		
		browser.get('https://www.facebook.com/'+confessionsSource+'/')

		SCROLL_PAUSE_TIME = 0.6
		
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
			time2 = time1.get_attribute("title")
			time3 = re.split(' |\/|:', time2)
			if time3[4][-2:] == 'am':
				if time3[3] == '12':
					time3[3] = "00"
				if len(time3[3]) < 2:
					time3[3] = '0'+time3[3]
			else:
				if int(time3[3]) < 12:
					time3[3] = str(int(time3[3])+12)
			time3[4] = time3[4][:-2]
			time2 = time3[2]+'-'+time3[0]+'-'+time3[1]+' '+time3[3]+':'+time3[4]+":00"
			print(time2)
			
			utime = time1.get_attribute("data-utime")
			
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
			
			# shares = i.find_elements_by_class_name('UFIShareLink')
			# if len(shares) == 0:
				# shares = 0
			# else:
				# shares = shares[0].text
				# shares = [int(s) for s in shares.split() if s.isdigit()]
				# shares = shares[0]
				
			# comments = i.find_elements_by_class_name('UFIPagerLink')
			# if len(comments) == 0:
				# comments = 0
			# else:
				# comments = comments[0].text
				# comments = [int(s) for s in comments.split() if s.isdigit()]
				# if len(comments) > 0:
					# comments = comments[0]
				# else:
					# comments = 1
			
			try:
				post = {}
				post["source"] = confessionsSource
				post["time"] = time2
				post["unix-time"] = utime
				post["content"] = content
				post["likes"] = likes
				#post["shares"] = shares
				#post["comments"] = comments
				posts.append(post)

			except AttributeError:
				pass

	filename 		= "data1University.json"
	posts 			= []
	browser 		= webdriver.Firefox()
	confessionsList = ["HUIConfessions","TechnionConfessions","ArielUConfessions","tel.aviv.university.confessions","BGUConfession", "biuconfessions2018","HUJI.Confessions"]

	for confPage in confessionsList:
		getConfessions(confPage)
	# browser.quit()

	with open(filename, 'w', encoding='utf-8') as outfile:
		data = json.dump(posts, outfile, indent=2, ensure_ascii=False)
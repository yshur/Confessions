from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys


browser = webdriver.Firefox()

browser.get('https://www.facebook.com/ShenkarConfessions/')
# assert 'Yahoo' in browser.title

#elem = browser.find_element_by_name('p')  # Find the search box
#print(elem)
#elem.send_keys('seleniumhq' + Keys.RETURN)
SCROLL_PAUSE_TIME = 0.5

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")
i = 1
# file = open("yair.text","w") 

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

with open('yair9.txt', 'a', encoding='utf-8') as f:
	print('[', file=f)

for i in element:
	element1 = i.find_element_by_class_name('timestampContent')  # Find the search box
	element2 = i.find_element_by_tag_name('p')
	#element3 = i.find_element_by_class_name('UFILikeSentenceText')
	#element4 = element3.find_element_by_tag_name('span')  # Find the search box
	#element5 = i.find_element_by_class_name('UFIShareLink')
	#element6 = i.find_element_by_class_name('UFIPagerLink')
	
	with open('yair9.txt', 'a', encoding='utf-8') as f:
		print('{', file=f)
		print('\"time\":\"'+element1.text+'\",', file=f)
		print('\"content\":\"'+element2.text+'\"', file=f)
		# print('\"likes\":\"'+element4.text+'\"', file=f)
		# print('\"shares\":\"'+element5.text+'\",', file=f)
		# print('\"comments\":\"'+element6.text+'\"', file=f)
		print('},', file=f)

with open('yair9.txt', 'rb+') as filehandle:
    filehandle.seek(-3, os.SEEK_END)
    filehandle.truncate()
with open('yair9.txt', 'a', encoding='utf-8') as f:
	print(']', file=f)


# browser.quit()
# file.close() 


from selenium import webdriver
import time
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
	
element1 = browser.find_elements_by_id('js_54')  # Find the search box
element2 = browser.find_elements_by_xpath("//p")
element3 = browser.find_elements_by_class_name('UFILikeSentenceText')
element4 = browser.find_elements_by_class_name('z_c3pyo1brp')  # Find the search box

for i in element1:
	with open('yair2.txt', 'a', encoding='utf-8') as f:
		print(i.text, file=f)


for i in element2:
	with open('yair2.txt', 'a', encoding='utf-8') as f:
		print(i.text, file=f) 

for i in element3:
	span = i.find_element_by_tag_name("span")
	with open('yair2.txt', 'a', encoding='utf-8') as f:
		print(span.text, file=f)
		
for i in element4:
	with open('yair2.txt', 'a', encoding='utf-8') as f:
		print(i.text, file=f) 
		
# browser.quit()
# file.close() 


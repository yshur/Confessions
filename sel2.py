from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import json

# browser = webdriver.Firefox()
browser = webdriver.Chrome('C:\\Users\\Roi Shmueli\\Downloads\\chromedriver_win32\\chromedriver.exe')
browser.get('https://www.facebook.com/ShenkarConfessions/')
# assert 'Yahoo' in browser.title

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
posts = []

for i in element:
	element1 = i.find_element_by_class_name('timestampContent')  # Find the search box
	element2 = i.find_element_by_tag_name('p')

	try:
		post = {}
		post["time"] = element1.text
		post["content"] = element2.text
		posts.append(post)

	except AttributeError:
		pass

print(posts)
with open('data1.json', 'w', encoding='utf-8') as outfile:
    data = json.dump(posts, outfile, ensure_ascii=False)

# browser.quit()
# file.close() 


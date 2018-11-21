from urllib.request import urlopen
from bs4 import BeautifulSoup

html_doc = urlopen("https://www.facebook.com/ShenkarConfessions/")
soup = BeautifulSoup(html_doc.read(), "html5lib")

table_tags = soup.find_all('div')
for x in table_tags:
	th_tags = x.find_all({'class':'_5pcr userContentWrapper'})
	print(th_tags)

# tr_tags = table_tags[1].find_all('tr')
# print(tr_tags[1])
# {'class':'article__link'}
# td_tags = tr_tags[1].find_all('td')
# print(td_tags[8].span.text)
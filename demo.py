import urllib.request
import re
import json


file = open('hebrewStopwords.json', 'r', encoding="utf8")
python_obj = json.load(file)
file2 = open('wordsCounterMoreThanTen.json', 'r', encoding="utf8")
python_obj2 = json.load(file2)
for line in python_obj:
	x = re.findall(line['words'], python_obj2)
	# print(words[0])
	# words.remove(words[0])
	# print(words)
	# for x in list:
		# for word in words:
			# if x == word:
				# print('$$$$$$$$$$$$$$$$$$$$$$')
				# print('The word '+ word +' has been removed is:')
				# words.remove(word)
	# print('After removed words: ',words)
				




		
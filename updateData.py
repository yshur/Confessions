import json

posts  = []
ahevi  = ['א','ה','ו','י']
thilit = ['ב','ו','ל','מ','ת']

def isChar(char):
	if char >= '0' and char <= '9':
		return 1;
	if char >= 'a' and char <= 'z':
		return 1;
	if char >= 'A' and char <= 'Z':
		return 1;
	if char >= 'א' and char <= 'ת':
		return 1;
	return 0

def rmThilit(word):
	len1 = len(word)
	if len1<4:
		return word
	if word[0] not in thilit:
		return word
	else:
		word = word[1:]
		word = rmThilit(word)
		return word	
	
def rmAhevi(word):
	chars = list(word)
	len1 = len(chars)
	if len1<4:
		return word
	word = ''
	for i in range(len1):
		if chars[i] not in ahevi:
			word = word+chars[i]
			continue
		if i<(len1-1):
			if chars[i+1] in ahevi:
				word = word+chars[i]
				continue
		if i>0:
			if chars[i-1] in ahevi:
				word = word+chars[i]
	return word	

def processWord(word):
	chars = list(word)
	word = ''
	for chr in chars:
		if isChar(chr) == 1:
			word = word+chr
	return word

with open('data1.json', 'r', encoding='utf-8') as f:
	file_data = json.load(f)
for fd in file_data:
	if fd['content'] == '':
		continue
	words = fd['content'].split()
	for word in words:
		word = rmThilit(word)
		word = processWord(word)
		word = rmAhevi(word)
		print(word)


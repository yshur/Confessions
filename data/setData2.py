import os
import json
import re
import datetime


keyFile = open("key_words.json", mode='r', encoding='utf-8')
keyWords = json.load(keyFile)

issueFile = open("issues.json", mode='r', encoding='utf-8')
issuesWords = json.load(issueFile)

def processSource(source, name, isUniversity):
	posts = open("data1/"+source+".json", mode='r', encoding='utf-8')
	data1 = json.load(posts)

	posts = []

	# file3 = open('data3.txt', 'a', encoding='utf-8') 

	for post1 in data1:
		# print(post1['likes'])
		
		words = []
		issues = []
		time2 = datetime.datetime.fromtimestamp(int(post1["unix-time"])).isoformat()
				
		for k in keyWords:
			# print(k)
			if k in post1["content"]: 
				# print(keyWords[k])
				# file3.write("keyWord "+k+" = "+keyWords[k]) 
				words.append(keyWords[k])
				
		for k in words:
			# print(issuesWords[k])
			# file3.write("issue of "+k+" = "+issuesWords[k])
			issues.append(issuesWords[k])
			
		try:
			post = {}
			post["source"] 		= post1["source"]
			post["college"] 	= name
			post["isUniversity"] = isUniversity
			post["time"] 		= time2
			post["unix_time"] 	= int(post1["unix-time"])
			post["content"] 	= post1["content"]
			post["len_char"] 	= len(post1["content"])
			post["len_words"] 	= len(post1["content"].split())
			post["likes"] 		= post1["likes"]
			post["shares"] 		= post1["shares"]
			post["comments"] 	= post1["comments"]
			post["sum_like"] 	= post1["sum_like"]
			post["words"] 		= post1["words"]
			post["mean_words"] 	= list(set(words))
			post["issues"] 		= list(set(issues))
			posts.append(post)

		except AttributeError:
			pass
		
	filename = "data2/"+source+"_2.json"
	with open(filename, mode='w', encoding='utf-8') as f:
		json.dump(posts, f, indent=2, ensure_ascii=False)
		
	

collegeArray = {
				"ColmanConfessions": "Hamichlala Leminhal",
				"MTACONFESS": "Akademit Tel Aviv",
				"LevinskyConfessions": "Levinsky",
				"JCTConfessions": "Lev",
				"smkbconfessions": "Saminar Hakibuzim",
				"ShenkarConfessions":"Shenkar",
				"bezalelconf": "Bezalel",
				"IDCHerzliyaConfessions": "IDC BenThumi Herzliya",
				"sapirconfession": "Sapir",
				"telhaiconfessions": "Tel-Hai",
				"hitconfessionsisrael": "HIT Technology Holon",
				"RuppinConfession": "Rupin"
					}
universityArray = {
				"Open.University.of.Israel.Confessions": "Open University",
				"HUIConfessions": "Haifa University",
				"TechnionConfessions": "Technion",
				"ArielUConfessions": "Ariel",
				"tel.aviv.university.confessions": "Tel Aviv University",
				"BGUConfession": "Ben Gurion University",
				"biuconfessions2018": "Bar Ilan University",
				"HUJI.Confessions": "Hebrew University" 
				}
					
for s in collegeArray:
	print(s)
	processSource(s, collegeArray[s], False)
	
for s in universityArray:
	print(s)
	processSource(s, universityArray[s], True)
	
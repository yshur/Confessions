import os
import json
import re
import datetime

def processSource(source, f):
	posts = open("data2/"+source+"_2.json", mode='r', encoding='utf-8')
	data1 = json.load(posts)

	file3 = open('data3/confessions.csv', 'a', encoding='utf-8') 
	for post in data1:
		month 			= str(int(post["time"][5:7]))
		college 		= post["college"].replace(" ", "_")
		isUniversity 	= '1' if post["isUniversity"]==True else '0'
		len_char 		= str(post["len_char"])
		len_words 		= str(post["len_words"])
		likes 			= str(post["likes"])
		shares 			= str(post["shares"])
		comments 		= str(post["comments"])
		Food 			= str(post["issues"]["אוכל"]) if "אוכל" in post["issues"] else '0'
		Clothing 		= str(post["issues"]["בגדים"]) if "בגדים" in post["issues"] else '0'
		Entertainment 	= str(post["issues"]["בידור"]) if "בידור" in post["issues"] else '0'
		health 			= str(post["issues"]["בריאות"]) if "בריאות" in post["issues"] else '0'
		Men 			= str(post["issues"]["גברים"]) if "גברים" in post["issues"] else '0'
		Depression 		= str(post["issues"]["דיכאון"]) if "דיכאון" in post["issues"] else '0'
		Religion 		= str(post["issues"]["דת"]) if "דת" in post["issues"] else '0'
		Relationship 	= str(post["issues"]["זוגיות"]) if "זוגיות" in post["issues"] else '0'
		Society 		= str(post["issues"]["חברה"]) if "חברה" in post["issues"] else '0'
		Holidays 		= str(post["issues"]["חגים"]) if "חגים" in post["issues"] else '0'
		Vacation 		= str(post["issues"]["חופשה"]) if "חופשה" in post["issues"] else '0'
		Technology 		= str(post["issues"]["טכנולוגיה"]) if "טכנולוגיה" in post["issues"] else '0'
		Money 			= str(post["issues"]["כסף"]) if "כסף" in post["issues"] else '0'
		Studies 		= str(post["issues"]["לימודים"]) if "לימודים" in post["issues"] else '0'
		residence 		= str(post["issues"]["מגורים"]) if "מגורים" in post["issues"] else '0'
		social_media 	= str(post["issues"]["מדיה חברתית"]) if "מדיה חברתית" in post["issues"] else '0'
		Music 			= str(post["issues"]["מוזיקה"]) if "מוזיקה" in post["issues"] else '0'
		Weather 		= str(post["issues"]["מזג אוויר"]) if "מזג אוויר" in post["issues"] else '0'
		sex 			= str(post["issues"]["מין"]) if "מין" in post["issues"] else '0'
		Party 			= str(post["issues"]["מסיבה"]) if "מסיבה" in post["issues"] else '0'
		Place_of_study 	= str(post["issues"]["מקום לימודים"]) if "מקום לימודים" in post["issues"] else '0'
		Family 			= str(post["issues"]["משפחה"]) if "משפחה" in post["issues"] else '0'
		women 			= str(post["issues"]["נשים"]) if "נשים" in post["issues"] else '0'
		politics 		= str(post["issues"]["פוליטיקה"]) if "פוליטיקה" in post["issues"] else '0'
		Positive_emotion = str(post["issues"]["רגש חיובי"]) if "רגש חיובי" in post["issues"] else '0'
		Negative_emotion = str(post["issues"]["רגש שלילי"]) if "רגש שלילי" in post["issues"] else '0'
		transportation 	= str(post["issues"]["תחבורה"]) if "תחבורה" in post["issues"] else '0'
		field_of_study 	= str(post["issues"]["תחום לימודים"]) if "תחום לימודים" in post["issues"] else '0'
		# Description		= str(post["issues"]["תיאור"]) if "תיאור" in post["issues"] else '0'

		line = college+','+month+','+f+','+isUniversity+','+len_char+','+len_words+','+likes+','+shares+','+comments+',';
		line = line+Food+','+Clothing+','+Entertainment+','+health+','+Men+','+Depression+','+Religion+',';
		line = line+Relationship+','+Society+','+Holidays+','+Vacation+','+Technology+','+Money+','+Studies+','+residence+',';
		line = line+social_media+','+Music+','+Weather+','+sex+','+Party+','+Place_of_study+','+Family+','+women+',';
		line = line+politics+','+Positive_emotion+','+Negative_emotion+','+transportation+','+field_of_study+'\n';
		
		file3.write(line)
	file3.close()
	# return i
		
	

collegeArray = {
				"ColmanConfessions": "3640",
				"MTACONFESS": "1569",
				"LevinskyConfessions": "559",
				"JCTConfessions": "462",
				"smkbconfessions": "927",
				"ShenkarConfessions":"1862",
				"bezalelconf": "1434",
				"IDCHerzliyaConfessions": "7817",
				"sapirconfession": "2218",
				"telhaiconfessions": "2953",
				"hitconfessionsisrael": "1872",
				"RuppinConfession": "1720"
					}
universityArray = {
				"Open.University.of.Israel.Confessions": "3373",
				"HUIConfessions": "2568",
				"TechnionConfessions": "17411",
				"ArielUConfessions": "11716",
				"tel.aviv.university.confessions": "20059",
				"BGUConfession": "20211",
				"biuconfessions2018": "8317",
				"HUJI.Confessions": "11253" 
				}


line = 'college,month,followers,isUniversity,len_char,len_words,likes,shares,comments,Food,Clothing,Entertainment,health,Men,Depression,Religion,Relationship,Society,Holidays,Vacation,Technology,Money,Studies,residence,social_media,Music,Weather,sex,Party,Place_of_study,Family,women,politics,Positive_emotion,Negative_emotion,transportation,field_of_study\n';
file3 = open('data3/confessions.csv', 'w', encoding='utf-8') 
file3.write(line)
file3.close()	
			
for s,v in collegeArray.items():
	print(s)
	i = processSource(s,v)
	
for s,v in universityArray.items():
	print(s)
	i = processSource(s,v)
	
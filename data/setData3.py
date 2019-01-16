import os
import json
import re
import datetime

def processSource(source):
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
		empty 			= '1' if len(post["issues"])==0 else '0'
		Food 			= '1' if "אוכל" in post["issues"] else '0'
		Clothing 		= '1' if "בגדים" in post["issues"] else '0'
		Entertainment 	= '1' if "בידור" in post["issues"] else '0'
		health 			= '1' if "בריאות" in post["issues"] else '0'
		Men 			= '1' if "גברים" in post["issues"] else '0'
		Depression 		= '1' if "דיכאון" in post["issues"] else '0'
		Religion 		= '1' if "דת" in post["issues"] else '0'
		Relationship 	= '1' if "זוגיות" in post["issues"] else '0'
		Society 		= '1' if "חברה" in post["issues"] else '0'
		Holidays 		= '1' if "חגים" in post["issues"] else '0'
		Vacation 		= '1' if "חופשה" in post["issues"] else '0'
		Technology 		= '1' if "טכנולוגיה" in post["issues"] else '0'
		Money 			= '1' if "כסף" in post["issues"] else '0'
		Studies 		= '1' if "לימודים" in post["issues"] else '0'
		residence 		= '1' if "מגורים" in post["issues"] else '0'
		social_media 	= '1' if "מדיה חברתית" in post["issues"] else '0'
		Music 			= '1' if "מוזיקה" in post["issues"] else '0'
		Weather 		= '1' if "מזג אוויר" in post["issues"] else '0'
		sex 			= '1' if "מין" in post["issues"] else '0'
		Party 			= '1' if "מסיבה" in post["issues"] else '0'
		Place_of_study 	= '1' if "מקום לימודים" in post["issues"] else '0'
		Family 			= '1' if "משפחה" in post["issues"] else '0'
		women 			= '1' if "נשים" in post["issues"] else '0'
		politics 		= '1' if "פוליטיקה" in post["issues"] else '0'
		Positive_emotion = '1' if "רגש חיובי" in post["issues"] else '0'
		Negative_emotion = '1' if "רגש שלילי" in post["issues"] else '0'
		transportation 	= '1' if "תחבורה" in post["issues"] else '0'
		field_of_study 	= '1' if "תחום לימודים" in post["issues"] else '0'
		Description		= '1' if "תיאור" in post["issues"] else '0'

		line = college+','+month+','+isUniversity+','+len_char+','+len_words+','+likes+','+shares+','+comments+',';
		line = line+empty+','+Food+','+Clothing+','+Entertainment+','+health+','+Men+','+Depression+','+Religion+',';
		line = line+Relationship+','+Society+','+Holidays+','+Vacation+','+Technology+','+Money+','+Studies+','+residence+',';
		line = line+social_media+','+Music+','+Weather+','+sex+','+Party+','+Place_of_study+','+Family+','+women+',';
		line = line+politics+','+Positive_emotion+','+Negative_emotion+','+transportation+','+field_of_study+','+Description+'\n';
		
		file3.write(line)
	file3.close()
	# return i
		
	

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


line = 'college,month,isUniversity,len_char,len_words,likes,shares,comments,null,Food,Clothing,Entertainment,health,Men,Depression,Religion,Relationship,Society,Holidays,Vacation,Technology,Money,Studies,residence,social_media,Music,Weather,sex,Party,Place_of_study,Family,women,politics,Positive_emotion,Negative_emotion,transportation,field_of_study,Description\n';
file3 = open('data3/confessions.csv', 'w', encoding='utf-8') 
file3.write(line)
file3.close()	
			
for s in collegeArray:
	print(s)
	i = processSource(s)
	
for s in universityArray:
	print(s)
	i = processSource(s)
	
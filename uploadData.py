import json
from pymongo import MongoClient

def upload_data(name):
	file = open(name+'.json', 'r', encoding="utf8")

	data = json.load(file)
	client = MongoClient('mongodb://db_usr:db_pass2@ds145484.mlab.com:45484/confessions')
	db = client['confessions']
	collection = db.posts
	collection.insert_many(data)

confessionsList = ["ShenkarConfessions","bezalelconf","IDCHerzliyaConfessions",
					"sapirconfession","telhaiconfessions","hitconfessionsisrael",
					"RuppinConfession","HUIConfessions","TechnionConfessions",
					"ArielUConfessions","tel.aviv.university.confessions","BGUConfession",
					"biuconfessions2018","HUJI.Confessions" ]
for file in confessionsList:
	print(file)
	upload_data(file)
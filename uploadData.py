from pymongo import MongoClient
import pprint
import json

def upload_data():
	file = open('xxx.json', 'r', encoding="utf8")

	data = json.load(file)
	client = MongoClient('mongodb://roishmueli1:roi13031985@ds151892.mlab.com:51892/confessions')
	db = client['confessions']
	collection = db.colleges_words 
	collection.insert(data)


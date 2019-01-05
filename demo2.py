from pymongo import MongoClient
import pprint

file = open('wordsCounterMoreThanTen.json', 'r', encoding="utf8")

data = json.load(file)
client = MongoClient('mongodb://roishmueli1:roi13031985@ds151892.mlab.com:51892/confessions')
db = client['confessions']
collection = db.confessions
#collection.insert(data,check_keys=False)
collection.insert(data)


		   

#pprint.pprint(collection.find_one({'unix-time': '1544393442'}))

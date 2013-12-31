#program to parse xml file and store data onto mongodb
import pymongo 
from xml.dom.minidom import parseString

#declaring common variables like 'ip' and 'xml_file' for parsing
ip = 'localhost'
xml_file = 'sitemap.xml'

#function for setting mongo connection
def mongoConnection(ip):
	mongo = pymongo.Connection(ip)
	db = mongo.python_test
	collection = db.xml_parsed
	return collection

#function for file reading
def readFile(fileName):
	file = open(fileName,'r')
	data = file.read()
	file.close()
	return data

#function for storing data onto mongo
def mongoStore():
	dom = parseString(data)
	xmlTag = dom.getElementsByTagName('loc')
	print "MONGO KEY "+" VALUE "
	for loc in xmlTag:
		attribute = loc.localName
		value = loc.childNodes[0].data
		mongo_key = collection.insert({attribute:value})
		print mongo_key, value

#calling functions to parse xml file and store in mongodb
collection = mongoConnection(ip)
data = readFile(xml_file)
mongoStore()
print "xml parsed completed and data are stored onto mongodb"




	


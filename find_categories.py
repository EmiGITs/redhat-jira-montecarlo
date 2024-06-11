from pymongo import MongoClient

client = MongoClient()

from pymongo import MongoClient

# Provide the connection details
hostname = 'localhost'
port = 27017  # Default MongoDB port
# Create a MongoClient instance
client = MongoClient(hostname, port)

db = client['JiraRepos']
mongo_collection=db['RedHat']


x = mongo_collection.distinct('fields.issuetype.name')
print(len(x))
print(x)


client.close()
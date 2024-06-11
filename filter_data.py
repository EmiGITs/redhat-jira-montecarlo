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

#x = mongo_collection.find_one({"fields.issuetype.name": "Bug"})
x = mongo_collection.count_documents({"fields.issuetype.name": "New Feature"})
print(x)
#print(x["fields"]["issuetype"]["name"])


client.close()
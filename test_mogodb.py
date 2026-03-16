from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://Adityatechnologies:<@password>@networksecurity.opffssa.mongodb.net/?appName=networksecurity"

# create a client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
  client.admin.command('ping')
  print("Pinged your deployement. you successfully connected to MongoDB!")
except Exception as e:
  print(e)
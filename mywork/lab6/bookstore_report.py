import os
from pymongo import MongoClient 

MONGODB_ATLAS_URL = os.getenv("MONGODB_ATLAS_URL")
MONGODB_ATLAS_USER = os.getenv("MONGODB_ATLAS_USER")
MONGODB_ATLAS_PWD = os.getenv("MONGODB_ATLAS_PWD")

def main():
	client = MongoClient(
		MONGODB_ATLAS_URL,
		username = MONGODB_ATLAS_USER,
		password = MONGODB_ATLAS_PWD
	)

	db = client["bookstore"]
	authors = db["authors"]

	total_author = authors.count_documents({})

	print(f"Total Authors: {total_author}")

	for author in authors.find({},  {"name": 1, "nationality": 1, }):
		print (f"Name: {author['name']} , Nationality: {author['nationality']}")

	client.close()

if __name__ == "__main__":
	main()


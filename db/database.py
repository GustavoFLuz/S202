import pymongo


class Database:
    def __init__(self, database, collection, dataset):
        connectionString = "mongodb+srv://root:1234@cluster0.f3maf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)



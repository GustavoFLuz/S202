import pymongo

class Database:
    def __init__(self, database, collection, dataset=None):
        connectionString = "mongodb+srv://root:1234@cluster0.f3maf.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        self.clusterConnection = pymongo.MongoClient(
            connectionString
        )
        self.db = self.clusterConnection[database]
        self.collection = self.db[collection]
        if dataset:
            self.dataset = dataset

    def resetDatabase(self):
        self.db.drop_collection(self.collection)
        self.collection.insert_many(self.dataset)

    def create(self, titulo, autor, ano, preco):
        return self.collection.insert_one({"titulo": titulo, "autor": autor, "ano": ano, "preco": preco})

    def read(self):
        return self.collection.find({})

    def update(self, titulo, preco):
        return self.collection.update_one(
            {"titulo": titulo},
            {
                "$set": {"preco": preco},
                "$currentDate": {"lastModified": True}
            }
        )

    def delete(self, titulo):
        return self.collection.delete_one({"titulo": titulo})

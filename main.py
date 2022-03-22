from db.database import Database
from writeJson.WriteAJson import writeAJson
from dataset.produto_database import dataset as produtos
from dataset.carro_dataset import dataset as carro
from dataset.pessoa_dataset import dataset as pessoa

compras = Database(database="s202aggre", collection="produtos", dataset=produtos)
carro = Database(database="s202aggre", collection="carro", dataset=carro)
pessoas = Database(database="s202aggre", collection="pessoas", dataset=pessoa)

compras.resetDatabase()
carro.resetDatabase()
pessoas.resetDatabase()


result = compras.collection.aggregate([
    {"$lookup":
        {
            "from": "pessoas",
            "localField": "cliente_id",
            "foreignField": "_id",
            "as": "dono"
        }
     },
    {"$group":{
        "_id": "$dono.nome",
        "total": {"$sum": "$total"}
    }},
    {"$sort": {"total": 1}},
    {"$unwind": '$_id'},
    {"$project": {
        "nome": 1,
        "total": 1,
        "desconto": {
            "$cond": {"if": {"$gte": ["$total", 10]}, "then": True, "else": False}
        }
    }
    }


])

writeAJson(result, "result")

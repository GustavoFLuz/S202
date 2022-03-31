from unicodedata import name
from db.database import Database
from writeJson.WriteAJson import writeAJson

db = Database("s202json", "livros")
db.resetDatabase();

db.create("Clean Code", "Robert C. Martin", 2008, 31.0)
db.create("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 1997, 31.0)
db.create("1984", "George Orwell", 1949, 19.9)
writeAJson(db.read(), "livros")

db.update("Clean Code", 33.0)

db.delete("1984")

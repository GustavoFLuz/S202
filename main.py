from db.database import Database
from writeJson.WriteAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")

#pokemons com duas evolucoes
pokemon2evo = db.executeQuery({"next_evolution":{"$size" : 2}})
writeAJson(pokemon2evo, "Pokemons-com-2-evolucoes")

#pokemons que nao aparecem em ovos
pokemonNotInEgg = db.executeQuery({"egg": "Not in Eggs"})
writeAJson(pokemonNotInEgg, "Pokemons-que-nao-aparecem-em-ovos")

#pokemons que aparecem em ovos
pokemonInEgg = db.executeQuery({"egg": {"$ne": "Not in Eggs"}})
writeAJson(pokemonInEgg, "Pokemons-que-aparecem-em-ovos")

#pokemons com unico tipo
pokemonUnicoTipo = db.executeQuery({"type": {"$size": 1}})
writeAJson(pokemonUnicoTipo, "Pokemons-unico-tipo")

#pokemon com candy count >= 50
pokemonCandyCount = db.executeQuery({"candy_count": {"$gte": 50}})
writeAJson(pokemonCandyCount, "Pokemon-candy-gte50")

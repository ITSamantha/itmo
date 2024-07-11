from owlready2 import *

import VideoGame


class Ontology:

    def __init__(self, path=r"file://ontology/videogames.owl"):
        self.__ontology = get_ontology(path).load()
        owlready2.sync_reasoner()

    def getOntology(self):
        return self.__ontology

    def getGenres(self):
        return self.__ontology.search(type=self.__ontology.Genre)

    def getTypes(self):
        return self.__ontology.search(type=self.__ontology.Type)

    def getMechanics(self):
        return self.__ontology.search(type=self.__ontology.Mechanic)

    def getMainCharacters(self):
        return self.__ontology.search(type=self.__ontology.MainCharacter)

    def getVideoGames(self):
        return self.__ontology.search(type=self.__ontology.VideoGame)

    def choosePreferenceGames(self, videoGame):
        allVideoGames = self.getVideoGames()
        if videoGame.getAgeLimit() is not None:
            age = videoGame.getAgeLimit()
            for i, game in enumerate(list(allVideoGames)):
                if not (game.hasAgeLimit and game.hasAgeLimit <= age):
                    if game in allVideoGames:
                        allVideoGames.remove(game)
        if videoGame.getRating() is not None:
            rating = videoGame.getRating()
            for i, game in enumerate(list(allVideoGames)):
                if not (game.hasRating and game.hasRating >= rating):
                    if game in allVideoGames:
                        allVideoGames.remove(game)
        if videoGame.getReleaseYear() is not None:
            year = videoGame.getReleaseYear()
            for i, game in enumerate(list(allVideoGames)):
                if not (game.hasReleaseYear and game.hasReleaseYear >= year):
                    allVideoGames.remove(game)
        if len(videoGame.getGenres()) != 0:
            genres = videoGame.getGenres()
            for _, game in enumerate(list(allVideoGames)):
                if game.hasGenre:
                    for _, genre in enumerate(game.hasGenre):
                        if not (genre.name in genres):
                            if game in allVideoGames:
                                allVideoGames.remove(game)
        if len(videoGame.getMechanics()) != 0:
            mechanics = videoGame.getMechanics()
            for _, game in enumerate(list(allVideoGames)):
                if game.hasMechanic:
                    for _, mechanic in enumerate(game.hasMechanic):
                        if not (mechanic.name in mechanics):
                            if game in allVideoGames:
                                allVideoGames.remove(game)
        if len(videoGame.getTypes()) != 0:
            types = videoGame.getTypes()
            for _, game in enumerate(list(allVideoGames)):
                if game.hasType:
                    for _, type in enumerate(game.hasType):
                        if not (type.name in types):
                            if game in allVideoGames:
                                allVideoGames.remove(game)
        if videoGame.getMainCharacter() is not None:
            mainCharacter = videoGame.getMainCharacter()
            for i, game in enumerate(list(allVideoGames)):
                if not (game.hasMainCharacter and game.hasMainCharacter.name == mainCharacter):
                    if game in allVideoGames:
                        allVideoGames.remove(game)
        for i, game in enumerate(allVideoGames):
            allVideoGames[i] = VideoGame.VideoGame(genres=game.hasGenre if game.hasGenre else None,
                                                   mainCharacter=game.hasMainCharacter if game.hasMainCharacter else None,
                                                   types=game.hasType if game.hasType else None,
                                                   ageLimit=int(game.hasAgeLimit) if game.hasAgeLimit else None,
                                                   mechanics=game.hasMechanic if game.hasMechanic else None,
                                                   rating=game.hasRating if game.hasRating else None,
                                                   releaseYear=game.hasReleaseYear if game.hasReleaseYear else None,
                                                   description=game.hasDescription if game.hasDescription else None,
                                                   name=game.name)
        print(*allVideoGames)

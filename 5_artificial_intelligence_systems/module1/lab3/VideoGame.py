class VideoGame:

    def __init__(self, genres=None, mainCharacter=None, mechanics=None, types=None, ageLimit=None, rating=None,
                 releaseYear=None, description=None, name=None):
        self.__genres: list[str] = genres
        self.__mainCharacter: str = mainCharacter
        self.__mechanics: list[str] = mechanics
        self.__types: list[str] = types
        self.__ageLimit: int = ageLimit
        self.__rating: float = rating
        self.__releaseYear: int = releaseYear
        self.__description: str = description
        self.__name: str = name

    def getGenres(self):
        return self.__genres

    def setGenres(self, genres):
        self.__genres = genres

    def getMainCharacter(self):
        return self.__mainCharacter

    def setMainCharacter(self, mainCharacter):
        self.__mainCharacter = mainCharacter

    def getMechanics(self):
        return self.__mechanics

    def setMechanics(self, mechanics):
        self.__mechanics = mechanics

    def getTypes(self):
        return self.__types

    def setTypes(self, types):
        self.__types = types

    def getAgeLimit(self):
        return self.__ageLimit

    def setAgeLimit(self, ageLimit):
        self.__ageLimit = ageLimit

    def getRating(self):
        return self.__rating

    def setRating(self, rating):
        self.__rating = rating

    def getReleaseYear(self):
        return self.__releaseYear

    def setReleaseYear(self, releaseYear):
        self.__releaseYear = releaseYear

    def getDescription(self):
        return self.__description

    def setDescription(self, description):
        self.__description = description

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def __str__(self):
        return (
            f"Название: {self.__name} | Возрастные ограничения: {str(self.__ageLimit) + '+' if self.__ageLimit is not None else '-'}\n"
            f"\tРейтинг: {self.__rating if self.__rating is not None else '-'} | Год выпуска: {int(self.__releaseYear) if self.__releaseYear is not None else '-'}\n"
            f"\tОписание: {self.__description if self.__description is not None else '-'}\n"
            f"\tМеханики: {[el.name for el in self.__mechanics] if self.__mechanics is not None else '-'}\n"
            f"\tЖанры: {[el.name for el in self.__genres] if self.__genres is not None else '-'}\n"
            f"\tТипы: {[el.name for el in self.__types] if self.__types is not None else '-'}\n"
            f"\tГлавный герой: {self.__mainCharacter.name if self.__mainCharacter is not None else '-'}\n\n")

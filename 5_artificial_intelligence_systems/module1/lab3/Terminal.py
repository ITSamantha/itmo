from Ontology import Ontology
from VideoGame import VideoGame
from exceptions.IncorrectValueException import IncorrectValueException
from validators.ArgsValidator import ArgsValidator

MAX_FOR_PARAMETER = 1
SEPARATOR = ','


class Terminal:

    def __init__(self):
        self.__videoGame = None
        self.__ontology = Ontology()

    def work(self):
        try:
            print('Добрый день! Данная программа поможет Вам найти подходящую игру:)')
            self.enterArguments()
            self.getPreferGame()
        except IncorrectValueException as ex:
            print(ex.message)
            return

    def enterArguments(self):
        print('Вам необходимо будет ввести информацию, чтобы мы подобрали игру, соответствующую именно Вам!')
        genres = self.__enterGenres()
        mainCharacter = self.__enterMainCharacter()
        mechanics = self.__enterMechanics()
        types = self.__enterTypes()
        age = self.__enterAge()
        rating = self.__enterRating()
        year = self.__enterReleaseYear()
        self.__videoGame = VideoGame(genres=genres, mainCharacter=mainCharacter, mechanics=mechanics, types=types,
                                     ageLimit=age, rating=rating, releaseYear=year)

    def __enterGenres(self):
        print(
            f'\nВведите жанры, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных жанров:')
        genres = [element.name for element in self.__ontology.getGenres()]
        print(*genres, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), genres)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterGenres()

    def __enterMainCharacter(self):
        print(
            f'\nВведите главного героя, который Вам подходит (только одного). Если Вы не хотите учитывать данный '
            f'параметр, введите "-".')
        print(f'Список возможных главных героев:')
        mainCharacters = [element.name for element in self.__ontology.getMainCharacters()]
        print(*mainCharacters, sep=SEPARATOR)
        try:
            return ArgsValidator.validateOneString(input("Ваши данные:"), mainCharacters)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterMainCharacter()

    def __enterMechanics(self):
        print(
            f'\nВведите механики, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных механик:')
        mechanics = [element.name for element in self.__ontology.getMechanics()]
        print(*mechanics, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), mechanics)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterMechanics()

    def __enterTypes(self):
        print(
            f'\nВведите типы, которые Вам подходят, через запятую. Если Вы не хотите учитывать данный параметр, '
            f'введите "-".')
        print(f'Список возможных типов:')
        types = [element.name for element in self.__ontology.getTypes()]
        print(*types, sep=SEPARATOR)
        try:
            return ArgsValidator.validateLists(input("Ваши данные:"), types)
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterTypes()

    def __enterAge(self):
        print(
            f'\nВведите Ваш возраст. Если Вы не хотите учитывать данный '
            f'параметр, введите "-".')
        try:
            return ArgsValidator.validateAge(input("Ваши данные:"))
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterAge()

    def __enterRating(self):
        print(
            f'\nВведите рейтинг игры. Если Вы не хотите учитывать данный '
            f'параметр, введите "-".')
        try:
            return ArgsValidator.validateRating(input("Ваши данные:"))
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterRating()

    def __enterReleaseYear(self):
        print(
            f'\nВведите год выпуска. Если Вы не хотите учитывать данный '
            f'параметр, введите "-".')
        try:
            return ArgsValidator.validateYear(input("Ваши данные:"))
        except IncorrectValueException as ex:
            print(ex.message)
            return self.__enterReleaseYear()

    def getPreferGame(self):
        print(f'Итак, подобранные специально для Вас игры...')
        self.__ontology.choosePreferenceGames(self.__videoGame)

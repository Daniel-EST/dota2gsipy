from .map import Map
from .hero.hero import Hero
from .player import Player
from .provider import Provider


class GameState:
    def __init__(self, 
        map: Map = None,
        player: Player = None, 
        hero: Hero = None,
        provider: Provider = None
    ):
        self.__map = map
        self.__player = player
        self.__hero = hero
        self.__provider: provider
    
    @property
    def map(self):
        return self.__map
    
    @property
    def player(self):
        return self.__player
    
    @property
    def hero(self):
        return self.__hero
    
    @property
    def provider(self):
        return self.__provider

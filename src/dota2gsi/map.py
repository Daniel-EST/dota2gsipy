from typing import DefaultDict, Union
from enum import Enum

from collections import defaultdict


class DOTA2GameState(Enum):
    Undefined = 0
    DOTA_GAMERULES_STATE_DISCONNECT = 1
    DOTA_GAMERULES_STATE_GAME_IN_PROGRESS = 2
    DOTA_GAMERULES_STATE_HERO_SELECTION = 3
    DOTA_GAMERULES_STATE_INIT = 4
    DOTA_GAMERULES_STATE_LAST = 5
    DOTA_GAMERULES_STATE_POST_GAME = 6
    DOTA_GAMERULES_STATE_PRE_GAME = 7
    DOTA_GAMERULES_STATE_STRATEGY_TIME = 8
    DOTA_GAMERULES_STATE_WAIT_FOR_PLAYERS_TO_LOAD = 9
    DOTA_GAMERULES_STATE_CUSTOM_GAME_SETUP = 10

class Map: 
    def __init__(self, payload: DefaultDict[str, Union[str, int]]):
        map = defaultdict(lambda: None, payload['map'])
        self.__name = map['name']
        self.__match_id = map['matchid']
        self.__game_time = map['game_time']
        self.__clock_time = map['clock_time']
        self.__daytime = map['daytime']
        self.__nightstalker_night = map['nightstalker_night']
        self.__radiant_score = map['radiant_score']
        self.__dire_score = map['dire_score']
        self.__state = DOTA2GameState[map['game_state']] if map['game_state'] in DOTA2GameState.__members__ else DOTA2GameState.Undefined 
        self.__paused = map['paused']
        self.__custom_game_name = map['customgamename']
        self.__win_team = map['win_team']
        self.__ward_purchase_cooldown = map['ward_purchase_cooldown']

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def match_id(self) -> str:
        return self.__match_id

    @property
    def game_time(self) -> int:
        return self.__game_time

    @property
    def clock_time(self) -> int:
        return self.__clock_time

    @property
    def daytime(self) -> bool:
        return self.__daytime

    @property
    def nightstalker_night(self) -> bool:
        return self.__nightstalker_night

    @property
    def radiant_score(self) -> int:
        return self.__radiant_score

    @property
    def dire_score(self) -> int:
        return self.__dire_score

    @property
    def state(self) -> DOTA2GameState:
        return self.__state

    @property
    def paused(self) -> bool:
        return self.__paused

    @property
    def matchid(self) -> int:
        return self.__matchid

    @property
    def custom_game_name(self) -> int:
        return self.__custom_game_name

    @property
    def win_team(self) -> str:
        return self.__win_team

    @property
    def ward_purchase_cooldown(self) -> int:
        return self.__ward_purchase_cooldown

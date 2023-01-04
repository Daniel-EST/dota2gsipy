from typing import DefaultDict, Union
from collections import defaultdict


class Player: 
    def __init__(self, payload: DefaultDict[str, Union[str, int]]):
        player = defaultdict(lambda: None, payload['player'])
        self.__steam_id = player["steamid"]
        self.__account_id = player["accountid"]
        self.__name = player["name"]
        self.__activity = player["activity"]
        self.__kills = player["kills"]
        self.__deaths = player["deaths"]
        self.__assists = player["assists"]
        self.__last_hits = player["last_hits"]
        self.__denies = player["denies"]
        self.__kill_streak = player["kill_streak"]
        self.__commands_issued = player["commands_issued"]
        self.__kill_list = player["kill_list"]
        self.__team_name = player["team_name"]
        self.__gold = player["gold"]
        self.__gold_reliable = player["gold_reliable"]
        self.__gold_unreliable = player["gold_unreliable"]
        self.__gold_from_hero_kills = player["gold_from_hero_kills"]
        self.__gold_from_creep_kills = player["gold_from_creep_kills"]
        self.__gold_from_income = player["gold_from_income"]
        self.__gold_from_shared = player["gold_from_shared"]
        self.__gold_per_minute = player["gpm"]
        self.__experience_per_minute = player["xpm"]

    @property
    def steam_id(self) -> int:
        return self.__steam_id

    @property
    def account_id(self) -> int:
        return self.__account_id

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def activity(self) -> str:
        return self.__activity

    @property
    def kills(self) -> int:
        return self.__kills

    @property
    def deaths(self) -> int:
        return self.__deaths

    @property
    def assists(self) -> int:
        return self.__assists
    
    @property
    def last_hits(self) -> int:
        return self.__last_hits
    @property
    def denies(self) -> int:
        return self.__denies

    @property
    def kill_streak(self) -> int:
        return self.__kill_streak

    @property
    def commands_issued(self) -> int:
        return self.__commands_issued
    
    @property
    def kill_list(self):
        return self.__kill_list

    @property
    def team_name(self) -> str:
        return self.__team_name

    @property
    def gold(self) -> int:
        return self.__gold

    @property
    def gold_reliable(self) -> int:
        return self.__gold_reliable
    
    @property
    def gold_unreliable(self) -> int:
        return self.__gold_unreliable

    @property
    def gold_from_hero_kills(self) -> int:
        return self.__gold_from_hero_kills

    @property
    def gold_from_creep_kills(self) -> int:
        return self.__gold_from_creep_kills

    @property
    def gold_from_income(self) -> int:
        return self.__gold_from_income
    
    @property
    def gold_from_shared(self) -> int:
        return self.__gold_from_shared

    @property
    def gold_per_minute(self) -> int:
        return self.__gold_per_minute
    
    @property
    def experience_per_minute(self) -> int:
        return self.__experience_per_minute

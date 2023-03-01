from typing import Dict, DefaultDict, Union, List, Tuple
from collections import defaultdict

from .ability import Ability
from .item import Item


class Hero: 
    def __init__(self, payload: DefaultDict[str, Union[str, int, float]]):
        hero = defaultdict(lambda: None, payload['hero'])
        self.__pos = (hero['xpos'], hero['ypos'])
        self.__id = hero['id']
        self.__name = hero['name']
        self.__level = hero['level']
        self.__experience = hero['xp']
        self.__alive = hero['alive']
        self.__respawn_seconds = hero['respawn_seconds']
        self.__buyback_cost = hero['buyback_cost']
        self.__buyback_cooldown = hero['buyback_cooldown']
        self.__health = hero['health']
        self.__max_health = hero['max_health']
        self.__health_percent = hero['health_percent']
        self.__mana = hero['mana']
        self.__max_mana = hero['max_mana']
        self.__mana_percent = hero['mana_percent']
        self.__silenced = hero['silenced']
        self.__stunned = hero['stunned']
        self.__disarmed = hero['disarmed']
        self.__magic_immune = hero['magicimmune']
        self.__hexed = hero['hexed']
        self.__muted = hero['muted']
        self.__broken = hero['break']
        self.__aghanims_scepter = hero['aghanims_scepter']
        self.__aghanims_shard = hero['aghanims_shard']
        self.__smoked = hero['smoked']
        self.__debuffed = hero['has_debuff']
        self.__talents = [
            hero['talent_1'], 
            hero['talent_2'],
            hero['talent_3'],
            hero['talent_4'],
            hero['talent_5'],
            hero['talent_6'],
            hero['talent_7'],
            hero['talent_8'],
        ]
        self.__abilities = self.__parse_abilities(hero['abilities'])
        self.__inventory = self.__parse_item('slot', hero['items'])
        self.__stash = self.__parse_item('stash', hero['items'])
        self.__teleport = self.__parse_item('teleport', hero['items'])
        self.__neutral = self.__parse_item('neutral', hero['items'])

    def __parse_abilities(self, payload: DefaultDict[str, Dict[str, Union[str, int, bool]]]):
        if payload == None:
            return None
        
        abilities = []
        for ability in payload.keys():
            abilities.append(Ability(
                payload[ability]
            ))
        
        return abilities
    
    def __parse_item(self, type:str, payload: DefaultDict[str, Dict[str, Union[str, int, bool]]]):
        if payload == None:
            return None
        
        items = []
        for item in payload.keys():
            if type in item: 
                items.append(Item(
                    payload[item]
                ))
            
        return items

    @property
    def pos(self) -> Tuple[int]:
        return self.__pos

    @property
    def id(self) -> int:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    @property
    def level(self) -> int:
        return self.__level

    @property
    def experience(self) -> int:
        return self.__experience

    @property
    def alive(self) -> bool:
        return self.__alive

    @property
    def respawn_seconds(self) -> int:
        return self.__respawn_seconds

    @property
    def buyback_cost(self) -> int:
        return self.__buyback_cost

    @property
    def buyback_cooldown(self) -> int:
        return self.__buyback_cooldown

    @property
    def health(self) -> int:
        return self.__health

    @property
    def max_health(self) -> int:
        return self.__max_health

    @property
    def health_percent(self) -> float:
        return self.__health_percent

    @property
    def mana(self) -> int:
        return self.__mana

    @property
    def max_mana(self) -> int:
        return self.__max_mana

    @property
    def mana_percent(self) -> float:
        return self.__mana_percent

    @property
    def silenced(self) -> bool:
        return self.__silenced

    @property
    def stunned(self) -> bool:
        return self.__stunned

    @property
    def disarmed(self) -> bool:
        return self.__disarmed

    @property
    def magic_immune(self) -> bool:
        return self.__magic_immune

    @property
    def hexed(self) -> bool:
        return self.__hexed

    @property
    def muted(self) -> bool:
        return self.__muted

    @property
    def broken(self) -> bool:
        return self.__broken

    @property
    def aghanims_scepter(self) -> bool:
        return self.__aghanims_scepter

    @property
    def aghanims_shard(self) -> bool:
        return self.__aghanims_shard

    @property
    def smoked(self) -> bool:
        return self.__smoked

    @property
    def debuffed(self) -> bool:
        return self.__debuffed

    @property
    def talents(self) -> List[bool]:
        return self.__talents
    
    @property
    def abilities(self) -> List[Ability]:
        return self.__abilities

    @property
    def inventory(self) -> List[Item]:
        return self.__inventory

    @property
    def stash(self) -> List[Item]:
        return self.__stash

    @property
    def teleport(self) -> Item:
        return self.__teleport

    @property
    def neutral(self) -> Item:
        return self.__neutral

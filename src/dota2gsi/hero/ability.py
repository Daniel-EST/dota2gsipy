from typing import DefaultDict, Union
from collections import defaultdict


class Ability: 
    def __init__(self, payload: DefaultDict[str, Union[str, int]]):
        ability = defaultdict(lambda: None, payload)
        self.__name = ability['name']
        self.__level = ability['level']
        self.__can_cast = ability['can_cast']
        self.__passive = ability['passive']
        self.__ability_active = ability['ability_active']
        self.__cooldown = ability['cooldown']
        self.__ultimate = ability['ultimate']
        self.__charges = ability['charges']
        self.__max_charges = ability['max_charges']
        self.__charge_cooldown = ability['charge_cooldown']

    @property
    def name(self) -> str:
        return self.__name

    @property
    def level(self) -> int:
        return self.__level

    @property
    def can_cast(self) -> bool:
        return self.__can_cast
    
    @property
    def passive(self) -> bool:
        return self.__passive

    @property
    def ability_active(self) -> bool:
        return self.__ability_active

    @property
    def cooldown(self) -> int:
        return self.__cooldown

    @property
    def ultimate(self) -> bool:
        return self.__ultimate

    @property
    def charges(self) -> int:
        return self.__charges

    @property
    def max_charges(self) -> int:
        return self.__max_charges
    
    @property
    def charge_cooldown(self) -> int:
        return self.__charge_cooldown

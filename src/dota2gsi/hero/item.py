from typing import DefaultDict, Union
from collections import defaultdict


class Item: 
    def __init__(self, payload: DefaultDict[str, Union[str, int]]):
        item = defaultdict(lambda: None, payload)
        self.__name = item['name']
        self.__purchaser = item['purchaser']
        self.__can_cast = item['can_cast']
        self.__cooldown = item['cooldown']
        self.__passive = item['passive']
        self.__charges = item['charges']

    @property
    def name(self):
        return self.__name

    @property
    def purchaser(self):
        return self.__purchaser

    @property
    def can_cast(self):
        return self.__can_cast
    
    @property
    def cooldown(self):
        return self.__cooldown
    
    @property
    def passive(self):
        return self.__passive
    
    @property
    def charges(self):
        return self.__charges

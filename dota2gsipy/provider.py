from typing import DefaultDict, Union
from collections import defaultdict


class Provider: 
    def __init__(self, payload: DefaultDict[str, Union[str, int]]):
        provider = defaultdict(lambda: None, payload['provider'])
        self.__name = provider['name']
        self.__appid = provider['appid']
        self.__version = provider['version']
        self.__timestamp = provider['timestamp']

    @property
    def name(self) -> str:
        return self.__name

    @property
    def appid(self) -> int:
        return self.__appid

    @property
    def version(self) -> int:
        return self.__version
    
    @property
    def timestamp(self) -> int:
        return self.__timestamp

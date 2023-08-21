# dota2gsipy
A Python library to interface the Game State Integration in Dota 2.

The dota2gsipy library facilitates the integration of Valve's Dota 2 game state into Python applications. It listens for HTTP POST requests from the game on a specific address and port, parses the game state, and makes it available for use in the application.

After starting the `GSIServer` instance, it will continuously listen for incoming HTTP requests. Upon a received request, the contents will be parsed into a `GameState` object.

## What is Game State Integration
Game State Integration has bit been officially released for Dota 2. However, it is already possible access some of their information provided by the game. GSI has been available for Counter-Strike: Global Offensive and it is really similiar from the current Dota 2 GSI version. Learn more about [Counter-Strike Game State Integration here](https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Game_State_Integration).

## Installation
Using pip:

```
pip install dota2gsipy==0.1.0
```

## Usage
1. Create a custom `gamestate_integration_*.cfg` in `game/dota/cfg/gamestate_integration/`, for example:  

`gamestate_integration_test.cfg`
```
"Dota 2 Integration Configuration"
{
    "uri"           "http://localhost:4000/"
    "timeout"       "5.0"
    "buffer"        "0.1"
    "throttle"      "0.1"
    "heartbeat"     "30.0"
    "auth"
    {
        "token"      "TOKENHERE"
    }
    "data"
    {
        "provider"      "1"
        "map"           "1"
        "player"        "1"
        "hero"          "1"
        "abilities"     "1"
        "items"         "1"
    }
}
```

2. Create a `GSIServer` instance providing address, port and your token defined by the GSI configuration file.

```python
from dota2gsipy.server import GSIServer

server = GSIServer(("127.0.0.1", 4000),"TOKENHERE")
server.start_server()

while True:
    print(f"Gold: {server.game_state.player.gold}")
```

### Item, and Hero names
Full list of item names can be found [here](http://dota2.gamepedia.com/Cheats#Item_names) and a full list of heroes can be located [here](http://dota2.gamepedia.com/Cheats#Hero_names).

##### Examples:
```python
from dota2gsipy.server import GSIServer

server = GSIServer(("127.0.0.1", 4000),"TOKENHERE")
server.start_server()

print(f"Hero: {server.game_state.hero.name}")
```

## Null value handling
In case the payload does not contain the requested information, this value will be returned as `None`.

## Credits
[antonpup](https://github.com/antonpup/) for his C# Game State Integration library.
[mdhedelund](https://github.com/mdhedelund) for a CS:GO GSI Python library.

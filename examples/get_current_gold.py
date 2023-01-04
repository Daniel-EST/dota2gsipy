from src.dota2gsi.server import GSIServer

server = GSIServer(("127.0.0.1", 4000),'YOURTOKENHERE')
server.start_server()

while True:
    print(f'Gold: {server.game_state.player.gold}')
    print(f'Name: {server.game_state.player.name}')
    print(f'Hero name: {server.game_state.hero.name}')
    print(f'Pos: {server.game_state.hero.pos}')
    print(f'Talents: {server.game_state.hero.talents}')

import logging
import json

from typing import DefaultDict, Union

from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from collections import defaultdict

from .gamestate import GameState
from .hero.hero import Hero
from .map import Map
from .player import Player
from .provider import Provider

logging.getLogger(__name__).addHandler(logging.NullHandler())


class GSIServer(HTTPServer):
    def __init__(self, server_address, token):
        super(GSIServer, self).__init__(server_address, RequestHandler)
        self.auth_token = token
        self.game_state = GameState()

        self.running = False

    def start_server(self) -> None:
        try:
            thread = Thread(target=self.serve_forever)
            thread.start()
            first_time = True
            while self.running == False:
                if first_time == True:
                    logging.info("Dota 2 GSI Server starting...")
                first_time = False
            logging.info("Dota 2 GSI Server started.")

        except (KeyboardInterrupt, SystemExit):
            self.shutdown()
            pass

        except:
            logging.error("Server failed to start.")

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        print(self.headers)
        body = self.rfile.read(length).decode('utf-8')

        payload = defaultdict(
            lambda: None, 
            json.loads(body)
        )

        if not self.authenticate_payload(payload):
            logging.info("Connection refused: auth token does not match")
            self.send_header('Content-type', 'text/html')
            self.send_response(401)
            self.end_headers()
            return False
        
        self.server.running = True
        self.server.game_state = GameState(
            map=Map(payload),
            player=Player(payload),
            hero=Hero(payload),
            provider=Provider(payload)
        )

        self.send_header('Content-type', 'text/html')
        self.send_response(200)
        self.end_headers()

    def authenticate_payload(self, payload: DefaultDict[str, Union[str, int]]) -> bool:
        if 'auth' in payload and 'token' in payload['auth']:
            return payload['auth']['token'] == self.server.auth_token
        else:
            return False

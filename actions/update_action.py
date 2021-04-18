from file_drivers import cache_db
from utils.gcli import println
from detector import steam_detector, epic_detector
import env

import requests
import json

def run ():
	steam_detector.update_games_cache ()
	epic_detector.update_games_cache ()

	println ("Información actualizada correctamente")

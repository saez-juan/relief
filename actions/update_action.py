from file_drivers import cache_db
from utils.gcli import println
from detector import steam_detector, epic_detector

import requests
import json

def run ():
	cache_db.update("api", None)

	steam_detector.update_games_cache ()
	epic_detector.update_games_cache ()

	println ("Información actualizada correctamente")

from file_drivers import cache_db
from utils.gcli import println
from detector import steam_detector, epic_detector
import env

import requests
import json

def run ():
	__update_cache ()

	__get_api_info ("steam")

	println ("Información actualizada correctamente")

def __update_cache ():

	# Steam
	cache_db.update ("installed.steam", None)
	steam_ids = steam_detector.get_games_ids ()
	cache_db.update ("installed.steam", steam_ids)

	# Epic
	cache_db.update ("installed.epic", None)
	epic_ids = epic_detector.get_games_ids ()
	cache_db.update ("installed.epic", epic_ids)

def __get_api_info (platform):
	cached_ids = cache_db.get ("installed." + platform)
	api_response = requests.post (env.API_URL, {
		platform: cached_ids
	})

	games_info = json.loads (api_response.text)
	cache_db.update ("api." + platform, games_info.get (platform))
from file_drivers import cache_db

from utils.colors import paint
from utils.gcli import println, print_item

from detector import steam_detector, epic_detector

def run ():
	is_cached_info = cache_db.get ("api") != None

	if not is_cached_info:
		println ("No hay datos recopilados.")
		println ("Probá ejecutar: {}".format (paint ("update", "yellow")))
		return None

	print_games ("Steam", "steam")

def print_games (header, platform):
	games_info = cache_db.get ("api." + platform)

	if games_info == None:
		return
	
	println (paint (header, "cyan"))

	for game in games_info:
		print_item (game["name"])

from file_drivers import cache_db

from utils.colors import paint
from utils.gcli import println, print_item

from detector import steam_detector, epic_detector

support_colors = {
	"full"    : "green",
	"partial" : "yellow",
	"none"    : "white"
}

def run ():
	print_legend ()

	cached_info = cache_db.get ("api")

	if cached_info == None:
		println ("No hay datos recopilados.")
		println ("Probá ejecutar: {}".format (paint ("update", "yellow")))
		return None

	if cached_info.get ("steam") != None:
		print_games ("Steam", "steam")
		print () #-> SLFE

	if cached_info.get ("epic") != None:
		print_games ("Epic Games", "epic")

def print_games (header, platform):
	games_info = cache_db.get ("api." + platform)

	if games_info == None:
		return
	
	println (paint (header, "cyan"))

	for game in games_info:
		print_item (game["name"], bullet_color=support_colors[game["support"]])

def print_legend ():
	println (paint ("Leyenda", "cyan"))

	print_item ("Soporte completo", bullet_color=support_colors["full"])
	print_item ("Soporte parcial", bullet_color=support_colors["partial"])
	print_item ("No soportado", bullet_color=support_colors["none"])

	print () #-> SLFE
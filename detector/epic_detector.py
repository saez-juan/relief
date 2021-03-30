from file_drivers import config
import os
from utils.colors import paint
from utils.gcli import println

epic_config = None
lib_path = None

exclude_games = []

def initialize ():
	global epic_config
	epic_config = config.get ("EpicGames")

def get_all_games ():
	global epic_config, lib_path

	if epic_config == None:
		println (paint ("Detector de Epic Games no inicializado", "yellow"))
		return

	lib_path = epic_config.get ("lib-path")

	if lib_path == None:
		println (paint ("Librería de Epic Games no encontrada...", "yellow"))
		return

	manifest_files = __get_manifest_files ()
	installed_games = __get_installed_games (manifest_files)

	return list (filter (lambda g: g not in exclude_games, installed_games))


def __get_manifest_files ():
	global lib_path
	lib_files = os.listdir (lib_path)

	item_files = filter (lambda f: ".item" in f, lib_files)

	return list (item_files)

def __get_installed_games (manifest_files):
	global lib_path

	games = []

	for uri in manifest_files:
		complete_route = os.path.join (lib_path, uri)

		with open (complete_route, "r") as file_stream:
			for line in file_stream.readlines ():
				if "\"DisplayName\"" in line:
					splitted_line = line.split ("\"")
					games.append (splitted_line[3])
			
			file_stream.close ()
	
	return games
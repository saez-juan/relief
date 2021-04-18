from file_drivers import config, cache_db
import os
from utils.colors import paint
from utils.gcli import println, print_item

import requests
import json
import env

from detector.utils import get_mounted_disks, find_file

lib_path = None

excluded_ids = ["228980"]

def start ():
	global lib_path
	lib_path = config.get ("Libraries.steam-lib")

def initialize ():
	global lib_path

	println (paint ("Steam", "cyan"))

	print_item ("Buscando ruta")

	lib_path = config.get ("Search.steam-key-file.path")

	if lib_path == None:
		print_item ("Instalación de Steam no encontrada", bullet_color="red")
		return None

	print_item ("Guardando ruta en caché")

	config.update ("Libraries.steam-lib", lib_path)

	print_item ("Obteniendo IDs de juegos instalados")

	update_games_cache ()

	print_item ("Inicialización exitosa", bullet_color="green")

def get_games_ids ():
	global lib_path

	if lib_path == None:
		println (paint ("Detector de Steam no inicializado", "yellow"))
		return

	if lib_path == None:
		println (paint ("Librería de Steam no encontrada...", "yellow"))
		return None

	cached_games = cache_db.get ("installed.steam")
	installed_games = None

	if cached_games == None:
		manifest_files = __get_manifest_files ()
		installed_games = __get_installed_games (manifest_files)

		cache_db.update ("installed.steam", installed_games)
	else:
		installed_games = list (map (lambda g: g, cached_games))

	return list (filter (lambda g: g not in excluded_ids, installed_games))

def update_games_cache ():
	cache_db.update ("installed.steam", None)
	steam_ids = get_games_ids ()	
	cache_db.update ("installed.steam", steam_ids)

	__fetch_api_info ()

def __fetch_api_info ():
	cached_ids = cache_db.get ("installed.steam")

	if cached_ids == None:
		return None
	
	api_response = requests.post (env.API_URL, {
		"steam": cached_ids
	})

	games_info = json.loads (api_response.text)
	cache_db.update ("api.steam", games_info.get ("steam"))

def __get_manifest_files ():
	global lib_path
	lib_files = os.listdir (lib_path)

	acf_files = filter (lambda f: ".acf" in f, lib_files)

	return list (acf_files)

def __get_installed_games (manifest_files):
	global lib_path

	games_ids = []

	for uri in manifest_files:
		complete_route = os.path.join (lib_path, uri)

		current_game = {}

		with open (complete_route, "r") as file_stream:
			for line in file_stream.readlines ():
				if "\"appid\"" in line:
					splitted_line = line.split ("\"")
					games_ids.append (splitted_line[3])
			
			file_stream.close ()

	return games_ids

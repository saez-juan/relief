from file_drivers import config, cache_db
import os
from utils.colors import paint
from utils.gcli import println, print_item

import requests
import json

from detector.utils import get_mounted_disks, find_file

lib_path = None

excluded_ids = []

def start ():
	global lib_path
	lib_path = config.get ("Libraries.epic-lib")

def initialize ():
	global lib_path

	println (paint ("Epic Games", "cyan"))

	print_item ("Buscando ruta")

	lib_path = config.get ("Search.epic-key-file.path")

	if lib_path == None:
		print_item ("Instalación de Epic Games no encontrada", bullet_color="red")
		return None

	print_item ("Formateando la ruta")

	splitted_lib_path = lib_path.split(os.sep)
	splitted_lib_path.append ("Manifests")
	lib_path = os.path.join (os.sep.join (splitted_lib_path))

	print_item ("Guardando ruta en caché")

	config.update ("Libraries.epic-lib", lib_path)

	print_item ("Obteniendo IDs de juegos instalados")

	update_games_cache ()

	print_item ("Inicialización exitosa", bullet_color="green")

def get_games_ids ():
	global lib_path

	if lib_path == None:
		println (paint ("Detector de Epic Games no inicializado", "yellow"))
		return

	manifest_files = __get_manifest_files ()

	cached_games = cache_db.get ("installed.epic")
	installed_games = None

	if cached_games == None:
		manifest_files = __get_manifest_files ()
		installed_games = __get_installed_games (manifest_files)

		cache_db.update ("installed.epic", installed_games)
	else:
		installed_games = list (map (lambda g: g, cached_games))

	return list (filter (lambda g: g not in excluded_ids, installed_games))

def update_games_cache ():
	cache_db.update ("installed.epic", None)
	epic_ids = get_games_ids ()
	cache_db.update ("installed.epic", epic_ids)

	__fetch_api_info ()

def __fetch_api_info ():
	cached_ids = cache_db.get ("installed.epic")

	if cached_ids == None:
		return None

	api_url = config.get ("General.api-url")

	api_response = requests.post (api_url, {
		"epic": cached_ids
	})

	games_info = json.loads (api_response.text)
	cache_db.update ("api.epic", games_info.get ("epic"))

def __get_manifest_files ():
	global lib_path
	lib_files = os.listdir (lib_path)

	item_files = filter (lambda f: ".item" in f, lib_files)

	return list (item_files)

def __get_installed_games (manifest_files):
	global lib_path

	games_ids = []

	for uri in manifest_files:
		complete_route = os.path.join (lib_path, uri)

		with open (complete_route, "r") as file_stream:
			for line in file_stream.readlines ():
				if "\"CatalogItemId\"" in line:
					splitted_line = line.split (":", 1)
					raw_name = splitted_line[1]

					appid = raw_name[2:len (raw_name) - 3] \
						.replace ("\\", "")
					
					games_ids.append (appid)
	
	return games_ids
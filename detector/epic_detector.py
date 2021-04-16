from file_drivers import config, cache_db
import os
from utils.colors import paint
from utils.gcli import println, print_item

from detector.utils import get_mounted_disks, find_file

lib_path = None

excluded_ids = []

def start ():
	global lib_path

	lib_path = config.get ("Libraries.epic-lib")

def initialize ():
	global lib_path

	println (paint ("Epic Games", "cyan"))

	epic_config = config.get ("Libraries.epic-path")
	lib_path = ""

	print_item ("Obteniendo lista de discos montados")

	mounted_disks = get_mounted_disks ()

	key_file = "Launcher.manifest"

	for disk_letter in mounted_disks:
		print_item ("Buscando librería en disco " + disk_letter)
		
		search_result = find_file (disk_letter, key_file)
		
		if search_result != None:
			lib_path = search_result

	if lib_path == None:
		print_item ("No se encontró la librería", bullet_color="red")
		return

	print_item ("Formateando la ruta")

	splitted_lib_path = lib_path.split(os.sep)
	splitted_lib_path.pop ()
	splitted_lib_path.append ("Manifests")
	lib_path = os.path.join (os.sep.join (splitted_lib_path))

	print_item ("Guardando ruta en caché")

	config.update ("Libraries.epic-lib", lib_path)

	print_item ("Inicialización exitosa", bullet_color="green")
	print () #-> SLFE

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
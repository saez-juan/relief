from file_drivers import config
import os
from utils.colors import paint
from utils.gcli import println, print_item

from detector.utils import get_mounted_disks, find_file

lib_path = None

excluded_ids = ["228980"]

def start ():
	global lib_path
	
	lib_path = config.get ("Libraries.steam-lib")

def initialize ():
	global lib_path

	println (paint ("Steam", "cyan"))

	print_item ("Obteniendo lista de discos montados")

	mounted_disks = get_mounted_disks ()

	key_file = "libraryfolders.vdf"

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
	lib_path = os.path.join (os.sep.join (splitted_lib_path))

	print_item ("Guardando ruta en caché")

	config.update ("Libraries.steam-lib", lib_path)

	print_item ("Inicialización exitosa", bullet_color="green")
	print () #-> SLFE

def get_games_list ():
	global lib_path

	if lib_path == None:
		println (paint ("Detector de Steam no inicializado", "yellow"))
		return

	if lib_path == None:
		println (paint ("Librería de Steam no encontrada...", "yellow"))
		return None

	manifest_files = __get_manifest_files ()
	installed_games = __get_installed_games (manifest_files)

	return list (filter (lambda g: g["id"] not in excluded_ids, installed_games))

def __get_manifest_files ():
	global lib_path
	lib_files = os.listdir (lib_path)

	acf_files = filter (lambda f: ".acf" in f, lib_files)

	return list (acf_files)

def __get_installed_games (manifest_files):
	global lib_path

	games = []

	for uri in manifest_files:
		complete_route = os.path.join (lib_path, uri)

		current_game = {}

		with open (complete_route, "r") as file_stream:
			for line in file_stream.readlines ():
				if "\"appid\"" in line:
					splitted_line = line.split ("\"")
					current_game["id"] = splitted_line[3]

				if "\"name\"" in line:
					splitted_line = line.split ("\"")
					current_game["name"] = splitted_line[3]
			
			games.append (current_game)
			
			file_stream.close ()
	
	return games

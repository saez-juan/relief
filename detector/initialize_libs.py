from utils.gcli import print_item
import os
from file_drivers import config

from detector.utils import get_mounted_disks, find_file

def find_steam_lib ():
	steam_config = config.get ("Steam")
	lib_path = ""

	print_item ("Obteniendo lista de discos montados", bullet_color="green")

	mounted_disks = get_mounted_disks ()

	print_item ("Lista de discos montados obtenida", bullet_color="green")

	key_file = "libraryfolders.vdf"

	for disk_letter in mounted_disks:
		print_item ("Buscando librería en disco " + disk_letter, bullet_color="green")
		
		search_result = find_file (disk_letter, key_file)
		
		if search_result != None:
			print_item ("Librería encontrada en disco " + disk_letter, bullet_color="green")
			lib_path = search_result

	if lib_path == None:
		print_item ("No se pudo encontrar la librería", bullet_color="red")
		return

	print_item ("Formateando la ruta", bullet_color="green")

	splitted_lib_path = lib_path.split(os.sep)
	splitted_lib_path.pop ()
	lib_path = os.path.join (os.sep.join (splitted_lib_path))

	print_item ("Guardando ruta en caché", bullet_color="green")

	steam_config["lib-path"] = lib_path
	config.update (steam_config, "Steam")

def find_epic_lib ():
	epic_config = config.get ("EpicGames")
	lib_path = ""

	print_item ("Obteniendo lista de discos montados", bullet_color="green")

	mounted_disks = get_mounted_disks ()

	print_item ("Lista de discos montados obtenida", bullet_color="green")

	key_file = "Launcher.manifest"

	for disk_letter in mounted_disks:
		print_item ("Buscando librería en disco " + disk_letter, bullet_color="green")
		
		search_result = find_file (disk_letter, key_file)
		
		if search_result != None:
			print_item ("Librería encontrada en disco " + disk_letter, bullet_color="green")
			lib_path = search_result

	if lib_path == None:
		print_item ("No se pudo encontrar la librería", bullet_color="red")
		return

	print_item ("Formateando la ruta", bullet_color="green")

	splitted_lib_path = lib_path.split(os.sep)
	splitted_lib_path.pop ()
	splitted_lib_path.append ("Manifests")
	lib_path = os.path.join (os.sep.join (splitted_lib_path))

	print_item ("Guardando ruta en caché", bullet_color="green")

	epic_config["lib-path"] = lib_path
	config.update (epic_config, "EpicGames")

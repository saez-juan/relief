import os
import psutil

from utils.colors import paint
from utils.gcli import println, print_item

from file_drivers import config

def search_all ():
	println (paint ("Búsqueda general", "cyan"))

	print_item ("Obteniendo lista de archivos clave")

	search_files = config.get ("Search")
	file_names = list (map (lambda f: f["file"], search_files.values ()))

	print_item ("Obteniendo lista de discos montados")

	mounted_disks = get_mounted_disks ()
	search_result = find_files (mounted_disks, file_names)

	print_item ("Guardando rutas en caché")

	founded_file_names = list (search_result.keys ())

	for k in search_files.keys ():
		expected_file = search_files[k].get ("file")

		if expected_file in founded_file_names:
			config.update ("Search.{}.path".format (k), search_result[expected_file])

	print_item ("Búsqueda finalizada", bullet_color="green")

def get_mounted_disks ():
	all_disks = map (lambda disk_info: disk_info.mountpoint, psutil.disk_partitions ())
	return list (all_disks)

def find_files (disk_letters, file_names):
	founded_files = {}

	exclusion_depth = 2
	exclude_folders = [
		"Windows",
		"$Recycle.Bin",
		"$SysReset",
		"$WinREAgent",
		"OneDriveTemp",
		"Recovery"
	]

	for dl in disk_letters:
		prev_root = ""

		print_item ("Buscando archivos en disco {}".format (dl))

		for root, dirs, files in os.walk (dl):

			fixed_root = "/".join (root.split ("\\")[0:exclusion_depth])

			for ef in exclude_folders:
				if ef.lower () in fixed_root.lower ():
					continue

			for fn in file_names:
				if fn in files:
					founded_files[fn] = os.path.join (root)

			if len (file_names) == len (founded_files.keys ()):
				break

	return founded_files

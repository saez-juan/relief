import config
import os
import psutil

steam_config = None

def initialize ():
	global steam_config

	steam_config = config.get ("Steam")


def run ():
	global steam_config

	if steam_config == None:
		print ("    Detector de Steam no inicializado")
		return

	lib_path = get_lib_path ()
	print (lib_path)


def get_lib_path ():
	global steam_config

	lib_path = steam_config.get ("lib-path")

	if lib_path != "?":
		return lib_path

	lib_path = find_lib (None)

	return lib_path

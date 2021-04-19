from file_drivers import cache_db
from os import path, makedirs
import shutil

from datetime import datetime

root_path = path.expanduser ("~/AppData/LocalLow/Relief")
save_path = path.join (root_path, "current")
backup_path = path.join (root_path, "backups")

def run ():
	if not path.exists (save_path):
		makedirs (save_path)

	make_backup ()

	steam_games = cache_db.get ("api.steam")
	if steam_games != None:
		steam_saving (steam_games)

def make_backup ():
	now = datetime.now ()

	backup_date = now.strftime ("%d_%m_%Y_%H_%M_%S")

	shutil.move (save_path, path.join (backup_path, backup_date))

def steam_saving (games_info):
	save_subpath = path.join (save_path, "Steam")

	if not path.exists (save_subpath):
		makedirs (save_subpath)

	for g in games_info:
		save_subpath_game = path.join (save_subpath, g["appid"])
		
		#if not path.exists (save_subpath_game):
		#    makedirs (save_subpath_game)
		
		for sd in g["save-dirs"]:
			compiled_path = compile_path (sd)

			if path.exists (compiled_path):
				shutil.copytree (compiled_path, save_subpath_game)
			
		
def compile_path (raw_path):
	formatted_path = raw_path \
		.replace ("$HOME", "~")
		
	return path.expanduser (formatted_path)
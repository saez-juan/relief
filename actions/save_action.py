from file_drivers import cache_db
from os import path, makedirs
import shutil
from save_system import git

from datetime import datetime

root_path = path.expanduser ("~/AppData/LocalLow/Relief")

def run ():
	if not path.exists(root_path):
		makedirs (root_path)

	git.intialize_repository (root_path)

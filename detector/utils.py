import psutil
import os

def get_mounted_disks ():
	all_disks = map (lambda disk_info: disk_info.mountpoint, psutil.disk_partitions ())
	return list (all_disks)

def find_file (disk_letter, filename):
	exclude_dirs = [
		os.environ["windir"].lower (),
		os.path.expanduser ("~\\AppData").lower ()
	]

	for root, dirs, files in os.walk (disk_letter):
		if root.lower () in exclude_dirs:
			continue

		if filename in files:
			return os.path.join(root, filename)
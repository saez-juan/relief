import toml
import yaml

from os import path
from utils.dicts import keychain_in_dict, get_merge_dict, parse_keychain, dict_merge

# --

__file_path = "file_drivers/config.toml"

__current_execution_info = {
	"parsed": False,
	"config-dict": {}
}

# --

def start ():
	global __current_execution_info, __file_path

	if not path.exists (__file_path):
		initialize ()

	with open (__file_path, "r") as file_info:
		raw_file_info = "\n".join(file_info.readlines ())
		__current_execution_info["parsed"] = True
		__current_execution_info["config-dict"] = toml.loads (raw_file_info)
		file_info.close ()

def initialize ():
	initial_config = {
		"General": {
			"first-init": True
		},
		"Libraries": {
			"steam-lib": "?",
			"epic-lib": "?",
			"riot-lib": "?"
		}
	}
	
	new_file = open (__file_path, "w+")
	toml_string = toml.dumps (initial_config)
	new_file.write (toml_string)
	new_file.close ()

# --

def get (keychain, debug=False):
	global __current_execution_info

	parsed      = __current_execution_info["parsed"]
	config_dict = __current_execution_info["config-dict"]
	keys        = parse_keychain (keychain)
	
	if not parsed:
		if debug:
			print ("No se compiló el archivo de versión")
		return None

	expected_value = keychain_in_dict (keychain, config_dict)

	if expected_value == None:
		if debug:
			print ("La info \"{}\" no existe", keychain)
		return None

	return expected_value

def update (keychain, value):
	global __current_execution_info, __file_path

	config_dict = __current_execution_info["config-dict"]

	merge_dict = get_merge_dict (keychain, value)
	dict_merge (config_dict, merge_dict)

	__current_execution_info["config-dict"] = config_dict

	with open (__file_path, "w+") as config_file:
		toml_content = toml.dumps (config_dict)
		config_file.write (toml_content)
		config_file.close ()


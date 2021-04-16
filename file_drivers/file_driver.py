import yaml
from os import path
from utils.dicts import keychain_in_dict, dict_merge, parse_keychain, get_merge_dict

class FileDriver:
	__file_path = ""
	
	__parsed = False
	__dict = {}

	def __init__ (self, filepath, initial_state):
		self.__file_path = filepath

		if not path.exists (self.__file_path):
			self.initialize (initial_state)

		with open (self.__file_path, "r") as file_info:
			raw_file_info = "\n".join(file_info.readlines ())

			self.__parsed = True
			self.__dict   = yaml.safe_load (raw_file_info)

	def initialize (self, initial_state):
		with open (self.__file_path, "w+") as new_file:
			yaml_string = yaml.dump (initial_state)
			new_file.write (yaml_string)

	def get (self, keychain):
		keys = parse_keychain (keychain)

		if not self.__parsed:
			return None

		expected_value = keychain_in_dict (keychain, self.__dict)

		if expected_value == None:
			return None

		return expected_value

	def update (self, keychain, value):
		merge_dict = get_merge_dict (keychain, value)
		dict_merge (self.__dict, merge_dict)

		with open (self.__file_path, "w+") as file_stream:
			yaml_content = yaml.dump (self.__dict)
			file_stream.write (yaml_content)

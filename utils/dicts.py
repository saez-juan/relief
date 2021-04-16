import collections

def keychain_in_dict (keychain, dictionary):
	current_branch = dictionary
	keys = parse_keychain (keychain)

	for k in keys:
		if current_branch == None or not isinstance (current_branch, dict):
			return None
		
		expected_branch = current_branch.get (k)
		
		if expected_branch != None:
			current_branch = expected_branch
		else:
			return None
	
	return current_branch

def get_merge_dict (keychain, value):
	merge_dict = {}
	keys = parse_keychain (keychain)

	for k in reversed (keys):
		if len (merge_dict.keys ()) == 0:
			merge_dict[k] = value
		else:
			new_dict = {}
			new_dict[k] = merge_dict
			merge_dict = new_dict

	return merge_dict

def parse_keychain (keychain):
	return keychain.split (".")

def dict_merge (dct, merge_dct):
	for k, v in merge_dct.items ():
		if (k in dct and isinstance(dct[k], dict)
				and isinstance(merge_dct[k], collections.Mapping)):
			dict_merge(dct[k], merge_dct[k])
		else:
			dct[k] = merge_dct[k]

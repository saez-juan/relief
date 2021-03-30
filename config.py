import toml

__parsed_file = False
__config_dict = {}

def initialize ():
    global __parsed_file, __config_dict

    with open ("config.toml", "r") as file_info:
        raw_file_info = "\n".join(file_info.readlines ())
        __parsed_file = True
        __config_dict = toml.loads (raw_file_info)
        file_info.close ()

def get (key, debug=False):
    global __parsed_file, __config_dict
    
    if not __parsed_file:
        if debug:
            print ("No se compiló el archivo de versión")
        return None

    if __config_dict.get (key) == None:
        if debug:
            print ("La info \"{}\" no existe", key)
        return None

    return __config_dict[key]

def update (update_dict, into=None):
    global __config_dict

    if into != None and __config_dict.get (into) != None:
        __config_dict[into] = update_dict
    else:
        __config_dict = __config_dict | update_dict

    with open ("config.toml", "w") as writeable_file:
        toml_content = toml.dumps (__config_dict)
        writeable_file.write (toml_content)
        writeable_file.close ()

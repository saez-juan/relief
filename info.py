import toml

__parsed_file = False
__info_dict = {}

def initialize ():
    global __parsed_file, __info_dict

    with open ("version-info.toml", "r") as file_info:
        raw_file_info = "\n".join(file_info.readlines ())
        __parsed_file = True
        __info_dict = toml.loads (raw_file_info)
        file_info.close ()

def get (key, debug=False):
    global __parsed_file, __info_dict
    
    if not __parsed_file:
        if debug:
            print ("No se compiló el archivo de versión")
        return None

    if __info_dict.get (key) == None:
        if debug:
            print ("La info \"{}\" no existe", key)
        return None

    return __info_dict.get (key)

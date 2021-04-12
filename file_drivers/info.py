import toml
from utils.dicts import keychain_in_dict

__current_execution_info = {
    "parsed": False,
    "info-dict": {}
}

__file_path = "file_drivers/version-info.toml"

def start ():
    global __current_execution_info, __file_path

    with open (__file_path, "r") as file_info:
        raw_file_info = "\n".join(file_info.readlines ())

        __current_execution_info["parsed"] = True
        __current_execution_info["info-dict"] = toml.loads (raw_file_info)

        file_info.close ()

def get (keychain, debug=False):
    global __current_execution_info

    parsed    = __current_execution_info["parsed"]
    info_dict = __current_execution_info["info-dict"]

    expected_value = keychain_in_dict (keychain, info_dict)
    
    if not parsed:
        if debug:
            print ("No se compiló el archivo de versión")
        return None

    if expected_value == None:
        if debug:
            print ("La info \"{}\" no existe", key)
        return None

    return expected_value

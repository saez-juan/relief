
from actions import \
    version_action, \
    list_action, \
    relief_action, \
    save_action, \
    clear_action

import colors

def exec_action (action):
    actions_dict = {
        "version" : version_action.run,
        "list"    : list_action.run,
        "relief"  : relief_action.run,
        "save"    : save_action.run,
        "clear"   : clear_action.run,
        "cls"     : clear_action.run,
        "exit"    : "null"
    }

    print () #-> SLFE

    if actions_dict.get (action) == None:
        print ("    Acción " + colors.paint (action, "red") + " desconocida")
    else:
        actions_dict[action] ()

    print () #-> SLFE
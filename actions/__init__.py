
from actions import version_action, list_action, relief_action, save_action

def exec_action (action):
    actions_dict = {
        "version" : version_action.run,
        "list"    : list_action.run,
        "relief"  : relief_action.run,
        "save"    : save_action.run,
        "exit"    : "null"
    }

    print () #-> SLFE

    if actions_dict.get (action) == None:
        print ("Acción \"{}\" desconocida".format (action))
    else:
        actions_dict[action] ()

    print () #-> SLFE
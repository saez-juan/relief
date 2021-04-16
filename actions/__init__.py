from actions import \
    version_action, \
    list_action, \
    relief_action, \
    save_action, \
    clear_action, \
    update_action

from utils.colors import paint
from utils.gcli import println

def exec_action (action):
    actions_dict = {
        "version" : version_action.run,
        "list"    : list_action.run,
        "relief"  : relief_action.run,
        "update"  : update_action.run,
        "save"    : save_action.run,
        "clear"   : clear_action.run,
        "cls"     : clear_action.run,
        "exit"    : "null"
    }

    print () #-> SLFE

    if actions_dict.get (action) == None:
        println ("Acción " + paint (action, "red") + " desconocida")
    else:
        actions_dict[action] ()

    print () #-> SLFE
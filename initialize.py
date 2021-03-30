from file_drivers import config
import os
from utils.colors import paint
from utils.gcli import println

import detector

def initialize ():
    general_config = config.get ("General")

    if general_config.get ("first-init") == False:
        return
    
    println ("Se detectó que es la primera vez que se inicia {}.".format (paint ("Relief", "magenta")))
    println ("Ahora comenzará el proceso de inicialización.\n")
    println ("{}\n".format (paint ("Puede tardar unos minutos...", "yellow")))

    detector.initialize_once ()

    general_config["first-init"] = False
    config.update (general_config, "General")

    os.system ("cls")

from file_drivers import config, info
import os
from utils.colors import paint
from utils.gcli import println

from detector import steam_detector, epic_detector

# --

def initialize ():
    steam_detector.initialize ()
    epic_detector.initialize ()

def start ():
    config.start ()
    info.start ()

    steam_detector.start ()
    epic_detector.start ()

# --

def initialization_process ():
    first_init = config.get ("General.first-init")

    if first_init == False:
        return
    
    println ("Se detectó que es la primera vez que se inicia {}.".format (paint ("Relief", "magenta")))
    println ("Ahora comenzará el proceso de inicialización.\n")
    println ("{}\n".format (paint ("Puede tardar unos minutos...", "yellow")))

    initialize ()

    config.update ("General.first-init", False)

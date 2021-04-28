from utils.colors import paint
from utils.gcli import RELIEF
from file_drivers import config

def run ():
    current_version = config.get ("General.version")

    HEADER = RELIEF + " " + str (current_version) + "\n  por " + paint ("Juan Saez", "yellow")

    print (HEADER)
from file_drivers import config
from utils.gcli import RELIEF, println
from utils.colors import paint

def run ():
    current_version = config.get ("General.version")
    println (current_version + " | Desarrollado por " + paint ("Juan Saez", "yellow"))

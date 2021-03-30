from utils.colors import paint
from utils.gcli import print_item, println

from detector import initialize_libs, steam_detector, epic_detector

def initialize ():
    steam_detector.initialize ()
    epic_detector.initialize ()


def initialize_once ():
    println (paint ("Detector de juegos", "cyan"))

    print_item ("Buscando librería de Steam", bullet_color="green")
    initialize_libs.find_steam_lib ()

    print_item ("Buscando librería de Epic Games")
    initialize_libs.find_epic_lib ()

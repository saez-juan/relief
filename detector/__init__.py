from colors import paint
from gcli import print_item, println

import detector.initialize_libs

def initialize ():
    steam_detector.initialize ()

def initialize_once ():
    println (paint ("Detector de juegos", "cyan"))

    print_item ("Buscando librería de Steam", bullet_color="green")
    steam_lib_path = initialize_libs.find_steam_lib ()

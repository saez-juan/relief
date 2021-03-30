import colors
from detector import steam_detector

def run ():
    print ("    Lista de juegos instalados")
    print ("        {}: ".format (colors.paint ("Steam", "blue")))
    steam_detector.run ()

    # TODO: detectar juegos
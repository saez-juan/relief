from utils.colors import paint
from utils.gcli import print_item, println

from detector import steam_detector, epic_detector

def start ():
    steam_detector.start ()
    epic_detector.initialize ()

from utils.colors import paint
from utils.gcli import println, print_item

from detector import steam_detector, epic_detector

def run ():
    steam_games = steam_detector.get_all_games ()
    epic_games = epic_detector.get_all_games ()

    print_games ("Steam", steam_games)
    print () #-> SLFE
    print_games ("Epic Games", epic_games)

    # TODO: detectar juegos

def print_games (platform, games):
    if games == None:
        return
    
    println (paint (platform, "cyan"))

    for game in games:
        print_item (game)
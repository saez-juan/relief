from file_drivers import config
import os
from save_system import git
from utils.colors import paint
from utils.gcli import println, RELIEF
import search

from detector import steam_detector, epic_detector

# --

def initialize ():
	search.search_all ()
	print () #-> SLFE
	steam_detector.initialize ()
	print () #-> SLFE
	epic_detector.initialize ()
	print () #-> SLFE
	git.initialize ()

	os.system ("cls")

def start ():
	steam_detector.start ()
	epic_detector.start ()

# --

def initialization_process ():
	first_init = config.get ("General.first-init")

	if first_init == False:
		return
	
	println ("Se detectó que es la primera vez que se inicia {}.".format (RELIEF))
	println ("Ahora comenzará el proceso de inicialización.\n")
	println ("{}\n".format (paint ("Puede tardar unos minutos...", "yellow")))

	initialize ()

	config.update ("General.first-init", False)

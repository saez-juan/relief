# Glosario:
#   SLFE: Salto de línea con fines estéticos

import os
import actions
import platform
import detector
from utils import colors
import startup
from actions import relief_action
import traceback
from utils.gcli import println, RELIEF

PS1 = "[" + RELIEF + "]> "
EXIT_CMD = "exit"

def main ():
	global EXIT_CMD, PS1

	if platform.system () != "Windows":
		print () #-> SLFE
		println (RELIEF + " solo está disponible para Windows")
		return
	
	os.system ("cls")

	startup.start ()
	startup.initialization_process ()
	
	relief_action.run ()
	print () #-> SLFE

	last_command = ""
	
	while True:
		last_command = input (PS1).lower ()
		
		if last_command == EXIT_CMD:
			break
		else:
			actions.exec_action (last_command)

if __name__ == "__main__":
	try:
		main ()
	except KeyboardInterrupt:
		print () #-> SLFE
	except Exception as e:
		traceback.print_exc ()
	finally:
		print () #-> SLFE
		println (colors.paint ("Saliendo...", "yellow"))
		print () #-> SLFE
		exit (0)
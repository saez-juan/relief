# Glosario:
#   SLFE: Salto de línea con fines estéticos

import actions
from file_drivers import info, config
import platform
import detector
from utils import colors
from initialize import initialize
from actions import relief_action
import traceback
from utils.gcli import println

PS1 = "[" + colors.paint ("Relief", "magenta") + "]> "
EXIT_CMD = "exit"

def main ():
	global EXIT_CMD, PS1
	if platform.system () != "Windows":
		print ("\n    Relief solo está disponible para Windows\n")
		return

	#-> Preprocesamiento

	config.initialize ()
	detector.initialize ()
	info.initialize ()

	initialize ()

	#-> Preprocesamiento

	relief_action.run ()
	print () #-> SLFE

	last_command = ""

	try:
		while True:
			last_command = input (PS1).lower ()

			if last_command == EXIT_CMD:
				break
			else:
				actions.exec_action (last_command)
	except KeyboardInterrupt:
		print () #-> SLFE
	except Exception as e:
		traceback.print_exc ()
	finally:
		print () #-> SLFE
		println (colors.paint ("Saliendo...", "yellow"))
		exit ()

if __name__ == "__main__":
	main ()
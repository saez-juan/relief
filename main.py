# Glosario:
#   SLFE: Salto de línea con fines estéticos

import actions
import info
from actions import relief_action
import traceback

EXIT_CMD = "exit"

def main ():
	#-> Preprocesamiento

	info.initialize ()

	#-> Preprocesamiento

	relief_action.run ()
	print () #-> SLFE

	last_command = ""

	try:
		while True:
			last_command = input ("[Relief]> ").lower ()

			if last_command == EXIT_CMD:
				break
			else:
				actions.exec_action (last_command)
	except KeyboardInterrupt:
		print () #-> SLFE
	except Exception as e:
		traceback.print_exc ()
	finally:
		print ("\nSaliendo...")
		exit ()

if __name__ == "__main__":
	main ()
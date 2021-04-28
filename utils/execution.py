import subprocess
from utils.gcli import print_item

class Action:
    def __init__ (self, id, command, display=None):
        self.id = id
        self.command = command
        self.display = display

def exec_process (cmd, path):
	return subprocess.Popen (
		cmd,
		cwd=path,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True
	).wait ()

def exec_actions (actions_array, path, tabs=1):
	status_codes = []

	for action in actions_array:
		if action.display != None:
			print_item (action.display, tabs=tabs)

		result = exec_process(action.command, path)

		if result != 0:
			return action.id

	return None
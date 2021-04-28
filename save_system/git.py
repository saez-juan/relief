import subprocess
from file_drivers import config
from os import path, makedirs, listdir
from utils.gcli import print_item
from utils.colors import paint
from utils.execution import Action, exec_actions

def initialize ():
	folder_path = config.get ("General.save-path")
	
	if not path.exists (folder_path):
		makedirs (folder_path)

	if not ".git" in listdir (folder_path):
		repo_url = config.get ("Git.repo")
		__initialize_repository (folder_path, repo_url)

def __initialize_repository (folder_path, repo_url):
	action_list = [
		Action (
			"initialize-repository",
			["git", "init"],
			"Inicializando repositorio"
		),
		Action (
			"add-origin",
			["git", "remote", "add", "origin", repo_url],
			"Linkeando con repositorio remoto"
		),
		Action (
			"checkout-branch",
			["git", "checkout", "-b", "games"],
			"Cambiando a rama {}".format (paint ("games", "yellow"))
		),
		Action (
			"pull-games",
			["git", "pull", "origin", "games"],
			"Intentado descargar guardados previos"
		)
	]

	exec_error = exec_actions (action_list, folder_path)

	if exec_error == "pull-games":
		exec_error = __create_games_branch (folder_path)

	if exec_error == None:
		print_item ("Repositorio configurado exitosamente", bullet_color="green")
	else:
		print_item (
			"Ocurrió un error interno en la inicialización del repositorio ({})".format (paint (exec_error, "red")),
			bullet_color="red"
		)

	return exec_error

def __create_games_branch (folder_path):
	print_item ("Configurando rama {}".format ("games", "yellow"))

	print_item ("Creando {} inicial".format (paint ("README", "cyan")), tabs=2)

	with open ("save_system/readme-init.md", "r") as readme_init:
		readme_file = open (path.join (folder_path, "README.md"), "w+")
		readme_file.writelines (readme_init.readlines ())
		readme_file.close ()

	subaction_list = [
		Action (
			"add-files",
			["git", "add", "."],
			"Añadiendo archivo al repositorio"
		),
		Action (
			"commit-changes",
			["git", "commit", "-m", "\"Initial commit\""],
			"Escribiendo cambios"
		),
		Action (
			"push-changes",
			["git", "push", "origin", "games"],
			"Subiendo cambios al repositorio remoto"
		)
	]

	exec_error = exec_actions(subaction_list, folder_path, tabs=2)

	if exec_error == None:
		print_item ("Rama {} configurada exitosamente".format (
			paint ("games", "yellow")
		),
		bullet_color="green",
		tabs=2
	)
	else:
		print_item (
			"Ocurrió un error creando la rama {}. ({})".format (
				paint ("games", "yellow"),
				paint (exec_error, "red")
			),
			bullet_color="red",
			tabs=2
		)

	return exec_error
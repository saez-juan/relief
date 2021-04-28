from os import path
from file_drivers.file_driver import FileDriver



config = FileDriver (
	"file_drivers/config.yaml", {
		"General": {
			"first-init": True,
			"version": "v0.2",
			"save-path": path.expanduser ("~/AppData/LocalLow/Relief"),
			"api-url": "https://relief-server.herokuapp.com/"
		},
		"Libraries": {
			"steam-lib": "?",
			"epic-lib": "?"
		},
		"Search": {
			"steam-key-file": {
				"file": "libraryfolders.vdf",
				"path": "?"
			},
			"epic-key-file": {
				"file": "Launcher.manifest",
				"path": "?"
			}
		},
		"Git": {
			"repository-url": "?",
			"protocol": "https"
		}
	}
)

cache_db = FileDriver (
	"file_drivers/cache_db.yaml", {
		"api": None,
		"installed": None
	}
)

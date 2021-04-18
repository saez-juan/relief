from file_drivers.file_driver import FileDriver

config = FileDriver (
	"file_drivers/config.yaml", {
		"General": {
			"first-init": True
		},
		"Libraries": {
			"steam-lib": "?",
			"epic-lib": "?",
			"riot-lib": "?"
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
		}
	}
)

cache_db = FileDriver (
	"file_drivers/cache_db.yaml", {
		"api": None,
		"installed": None
	}
)

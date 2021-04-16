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
		}
	}
)

cache_db = FileDriver (
	"file_drivers/cache_db.yaml", {
		"api": None,
		"installed": None
	}
)

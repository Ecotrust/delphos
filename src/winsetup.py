from py2exe.build_exe import py2exe
from distutils.core import setup

import matplotlib

opts = {
    "py2exe": {
        "includes": [],
	"excludes": ['backend_gtkagg', 'backend_wxagg'],
	"dll_excludes": ['libgdk_pixbuf-2.0-0.dll', 'libgobject-2.0-0.dll', 'libgdk-win32-2.0-0.dll'],
        "packages": ["sqlalchemy", "pyExcelerator", "matplotlib", "pytz"],
        "dist_dir": "bin",
    }
}
 
setup(options = opts,
      console=[{"script": "start_gui.py"}],
      data_files=[matplotlib.get_py2exe_datafiles()]
)

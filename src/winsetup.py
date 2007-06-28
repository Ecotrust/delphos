from py2exe.build_exe import py2exe
from distutils.core import setup
 
opts = {
    "py2exe": {
        "includes": [],
        "packages": ["sqlalchemy"],
        "dist_dir": "bin",
    }
}
 
setup(options = opts,
      console=[{"script": "start_delphos.py"}] )
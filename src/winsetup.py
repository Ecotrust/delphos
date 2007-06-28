from distutils.core import setup
import glob
import py2exe

opts = {
    "py2exe": {
        "includes": "sqlalchemy",
        "optimize": 2,
                "dist_dir": "dist",
    }
}
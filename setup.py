try:
    from setuptools import setup
except:
    from distutils.core import setup
import os
import sys

APP = "main.py"
DATA_FILES = ["VERSION.txt", "SettingsWindow.ui"]


if sys.platform == "win32":
    for f in os.listdir(os.path.dirname(__file__), "Resources"):
        DATA_FILES.append(("Resources", [os.path.dirname(__file__), "Resources", f]))

    setup(
        name="Minecraft Universal In-Game Timer",
        windows=[
            {
                "script": APP,
                "icon_resources": [(1, os.path.join(os.path.dirname(__file__), "Resources", "icons.ico"))]
            }
        ],
        data_files=DATA_FILES,
        options={"py2exe": {
            "packages": ["PyQt5", "nbt"],
            "bundle_files": 1,
            "compressed": True,
        }},
        zipfile=None,
        setup_requires=["py2exe"],
    )


elif sys.platform == "darwin":
    setup(
        name="Minecraft Universal In-Game Timer",
        app=[APP],
        data_files=DATA_FILES,
        options={"py2app": {
            "packages": ["PyQt5", "nbt"],
            "iconfile": os.path.join(os.path.dirname(__file__), "Resources", "icons.icns"),
            "resources": "Resources",
        }},
        setup_requires=["py2app"],
    )

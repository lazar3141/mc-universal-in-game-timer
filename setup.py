from setuptools import setup
import os

APP = ["main.py"]
DATA_FILES = ["VERSION.txt", "SettingsWindow.ui"]
OPTIONS = {
    "includes": ["utils"],
    "packages": ["PyQt5", "nbt"],
    "iconfile": os.path.join(os.path.dirname(__file__), "Resources", "icons.icns"),
    "resources": "Resources"
}


setup(
    name="Minecraft Universal In-Game Timer",
    app=APP,
    data_files=DATA_FILES,
    options={"py2app": OPTIONS},
    setup_requires=["py2app"],
)

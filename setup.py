
#* This file uses py2app to make only a .app bundle for MacOS by running `python3 setup.py py2app`.
#* Windows and Linux executables are made separately with PyInstaller (https://pyinstaller.readthedocs.io/en/stable/index.html).

from setuptools import setup

import os


setup(
    name="Minecraft Universal In-Game Timer",
    app=["main.py"],
    data_files=["VERSION.txt", "SettingsWindow.ui"],
    options={"py2app": {
        "packages": ["PyQt5", "nbt"],
        "iconfile": os.path.join("Resources", "icons.icns"),
        "resources": "Resources",
    }},
    setup_requires=["py2app"],
)

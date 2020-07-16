"""
    Minecraft Universal In-Game Timer
    Copyright (C) 2020  NinjaSnail1080  (Discord User: @NinjaSnail1080#8581)

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import uic
from nbt.nbt import NBTFile

import sys
import os

import utils

DIRECTORY = os.path.dirname(__file__)

__version__ = open(os.path.join(DIRECTORY, "VERSION.txt")).read()

SETTINGS = QSettings(QSettings.NativeFormat, QSettings.UserScope, "Minecraft Universal In-Game Timer")


def get_last_played_level(mc_dir=None):
    levels = []
    if mc_dir is None:
        mc_dir = SETTINGS.value("MinecraftDirectory", utils.get_default_minecraft_dir())

    mc_saves = os.path.join(mc_dir, "saves")
    for world in os.listdir(mc_saves):
        try:
            levels.append(NBTFile(os.path.join(mc_saves, world, "level.dat")))
        except:
            continue
    return sorted(levels, key=lambda t: int(str(t["Data"]["LastPlayed"])), reverse=True)[0]["Data"]


class SettingsWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        uic.loadUi(os.path.join(DIRECTORY, "SettingsWindow.ui"), self)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)

        self.author_text.linkActivated.connect(self.open_link)
        self.author_text.setText(f"By NinjaSnail1080\u3000|\u3000<a href='https://github.com/NinjaSnail1080/mc-universal-in-game-timer'>Github</a> (v{__version__})")

        self.browse_field.setText(SETTINGS.value("MinecraftDirectory", utils.get_default_minecraft_dir()))

        self.browse_button.clicked.connect(self.browse_for_mc_dir)

        self.opacity_slider.setMinimum(10)
        self.opacity_slider.setMaximum(100)
        self.opacity_slider.setSingleStep(1)
        self.opacity_slider.setTickInterval(10)
        self.opacity_slider.setTickPosition(QSlider.TicksBothSides)
        self.opacity_slider.valueChanged.connect(self.change_opacity_percentage)
        self.opacity_slider.setValue(int(float(SETTINGS.value("Opacity", 0.5)*100)))

        if SETTINGS.value("Theme", "dark") == "dark":
            self.dark_theme_button.setChecked(True)
        else:
            self.light_theme_button.setChecked(True)

        self.continue_button.setText("Save  (double-click)")
        self.continue_button.clicked.connect(self.save_and_exit_settings)

        self.setFixedSize(420, 420)
        self.show()

    def browse_for_mc_dir(self):
        browse = QFileDialog(self)
        browse.setFileMode(QFileDialog.DirectoryOnly)
        if browse.exec_():
            mc_dir = browse.selectedFiles()[0]
            self.browse_field.setText(mc_dir)

    def change_opacity_percentage(self):
        self.opacity_text.setText(f"Opacity: {self.opacity_slider.value()}%")

    def open_link(self, link):
        QDesktopServices.openUrl(QUrl(link))

    def save_and_exit_settings(self):
        if self.browse_field.text() == "":
            SETTINGS.setValue("MinecraftDirectory", utils.get_default_minecraft_dir())
        else:
            SETTINGS.setValue("MinecraftDirectory", self.browse_field.text())
        SETTINGS.setValue("Opacity", self.opacity_slider.value() / 100)
        if self.dark_theme_button.isChecked():
            SETTINGS.setValue("Theme", "dark")
        elif self.light_theme_button.isChecked():
            SETTINGS.setValue("Theme", "light")

        self.close()
        self.new = TimerWindow()
        self.new.show()


class TimerWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowOpacity(float(SETTINGS.value("Opacity", 0.5)))

        with open(os.path.join(DIRECTORY, "Resources", "Minecraftia-Regular-1.ttf"), "rb") as f:
            self.small_font = QFont(QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFontFromData(f.read()))[0], 12)
        with open(os.path.join(DIRECTORY, "Resources", "Minecraftia-Regular-2.ttf"), "rb") as f:
            self.large_font = QFont(QFontDatabase.applicationFontFamilies(QFontDatabase.addApplicationFontFromData(f.read()))[0], 24)

        self.timer = QTimer()
        self.timer.setTimerType(Qt.PreciseTimer)
        self.timer.timeout.connect(self.update_igt)

        self.igt = QLabel("--:--:--.---")
        self.igt.setAlignment(Qt.AlignCenter)
        if SETTINGS.value("Theme", "dark") == "dark":
            self.igt.setStyleSheet("color: white;")
        self.igt.setFont(self.large_font)
        self.setCentralWidget(self.igt)

        self.toolbar = QToolBar("Main toolbar")
        self.toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(self.toolbar)

        if SETTINGS.value("Theme", "dark") == "dark":
            self.close_button = QAction(QIcon(os.path.join(DIRECTORY, "Resources", "white_x")), "", self)
            self.settings_button = QAction(QIcon(os.path.join(DIRECTORY, "Resources", "white_gear")), "", self)
        else:
            self.close_button = QAction(QIcon(os.path.join(DIRECTORY, "Resources", "black_x")), "", self)
            self.settings_button = QAction(QIcon(os.path.join(DIRECTORY, "Resources", "black_gear")), "", self)
        self.close_button.triggered.connect(self.close_window)
        self.settings_button.triggered.connect(self.open_settings)

        self.world_name = QLabel("Searching...")
        if SETTINGS.value("Theme", "dark") == "dark":
            self.world_name.setStyleSheet("color: white;")
        self.world_name.setFont(self.small_font)

        self.left_spacer = QWidget()
        self.left_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_spacer = QWidget()
        self.right_spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.toolbar.addAction(self.close_button)
        self.toolbar.addWidget(self.left_spacer)
        self.toolbar.addWidget(self.world_name)
        self.toolbar.addWidget(self.right_spacer)
        self.toolbar.addAction(self.settings_button)
        self.toolbar.setMovable(False)
        self.toolbar.setContextMenuPolicy(Qt.PreventContextMenu)
        self.toolbar.setStyleSheet("border: none;")

        if SETTINGS.value("Theme", "dark") == "dark":
            self.setStyleSheet("background-color: black;")
        self.move(int(SETTINGS.value("TimerPosX", 0)), int(SETTINGS.value("TimerPosY", 0)))

        self.show()
        self.timer.start(500)

    def update_igt(self):
        try:
            level_data = get_last_played_level()
            try:
                self.world_name.setText(f"{str(level_data['LevelName'])} ({str(level_data['Version']['Name'])})")
            except:
                self.world_name.setText(f"{str(level_data['LevelName'])} (Pre 1.9)")

            ticks = int(str(level_data["Time"]))
            seconds = ticks // 20
            h = str(seconds // 60 // 60)
            m = str(seconds // 60 % 60)
            s = str(seconds % 60)
            ms = str(int(ticks % 20 / 2 * 100))

            self.igt.setText(f"{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}.{ms.zfill(3)}")
            self.setFixedWidth(max([self.toolbar.sizeHint().width(), self.igt.sizeHint().width()]) + 16)
        except FileNotFoundError:
            self.world_name.setText("ERROR:  No World Found")
            self.world_name.setStyleSheet("color: red;")
            self.igt.setText("--:--:--.---")
            self.setFixedWidth(max([self.toolbar.sizeHint().width(), self.igt.sizeHint().width()]) + 16)

    def close_window(self):
        SETTINGS.setValue("TimerPosX", self.x())
        SETTINGS.setValue("TimerPosY", self.y())
        self.timer.stop()
        self.close()

    def open_settings(self):
        self.close_window()
        self.setStyleSheet("")
        SettingsWindow(self)

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        try:
            delta = QPoint(event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()
        except AttributeError:
            pass


if __name__ == "__main__":
    app = QApplication([])
    if sys.platform == "darwin":
        app.setStyle(QStyleFactory.create("macintosh"))
    else:
        app.setStyle(QStyleFactory.create("Fusion"))

    window = TimerWindow()
    app.exec_()
    sys.exit()

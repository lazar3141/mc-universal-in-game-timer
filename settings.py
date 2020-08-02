# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SettingsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(420, 420)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.light_theme_button = QtWidgets.QRadioButton(self.centralwidget)
        self.light_theme_button.setObjectName("light_theme_button")
        self.gridLayout.addWidget(self.light_theme_button, 19, 5, 1, 2)
        self.dark_theme_button = QtWidgets.QRadioButton(self.centralwidget)
        self.dark_theme_button.setObjectName("dark_theme_button")
        self.gridLayout.addWidget(self.dark_theme_button, 19, 2, 1, 2, QtCore.Qt.AlignRight)
        self.continue_button = QtWidgets.QPushButton(self.centralwidget)
        self.continue_button.setObjectName("continue_button")
        self.gridLayout.addWidget(self.continue_button, 22, 0, 1, 8)
        self.theme_text = QtWidgets.QLabel(self.centralwidget)
        self.theme_text.setObjectName("theme_text")
        self.gridLayout.addWidget(self.theme_text, 15, 0, 1, 8, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.browse_text = QtWidgets.QLabel(self.centralwidget)
        self.browse_text.setObjectName("browse_text")
        self.gridLayout.addWidget(self.browse_text, 2, 0, 1, 8, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.browse_field = QtWidgets.QLineEdit(self.centralwidget)
        self.browse_field.setObjectName("browse_field")
        self.gridLayout.addWidget(self.browse_field, 6, 0, 1, 7)
        self.welcome_text = QtWidgets.QLabel(self.centralwidget)
        self.welcome_text.setObjectName("welcome_text")
        self.gridLayout.addWidget(self.welcome_text, 0, 0, 1, 8, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.browse_button = QtWidgets.QPushButton(self.centralwidget)
        self.browse_button.setObjectName("browse_button")
        self.gridLayout.addWidget(self.browse_button, 6, 7, 1, 1)
        self.opacity_slider = QtWidgets.QSlider(self.centralwidget)
        self.opacity_slider.setOrientation(QtCore.Qt.Horizontal)
        self.opacity_slider.setObjectName("opacity_slider")
        self.gridLayout.addWidget(self.opacity_slider, 14, 2, 1, 5)
        self.opacity_min_text = QtWidgets.QLabel(self.centralwidget)
        self.opacity_min_text.setObjectName("opacity_min_text")
        self.gridLayout.addWidget(self.opacity_min_text, 14, 1, 1, 1)
        self.opacity_text = QtWidgets.QLabel(self.centralwidget)
        self.opacity_text.setObjectName("opacity_text")
        self.gridLayout.addWidget(self.opacity_text, 8, 0, 1, 8, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.opacity_max_text = QtWidgets.QLabel(self.centralwidget)
        self.opacity_max_text.setObjectName("opacity_max_text")
        self.gridLayout.addWidget(self.opacity_max_text, 14, 7, 1, 1)
        self.author_text = QtWidgets.QLabel(self.centralwidget)
        self.author_text.setObjectName("author_text")
        self.gridLayout.addWidget(self.author_text, 1, 0, 1, 8, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.browse_leave_empty_text = QtWidgets.QLabel(self.centralwidget)
        self.browse_leave_empty_text.setObjectName("browse_leave_empty_text")
        self.gridLayout.addWidget(self.browse_leave_empty_text, 7, 0, 1, 8, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Minecraft Universal In-Game Timer | Settings"))
        self.light_theme_button.setText(_translate("SettingsWindow", "Light"))
        self.dark_theme_button.setText(_translate("SettingsWindow", "Dark"))
        self.continue_button.setText(_translate("SettingsWindow", "Continue"))
        self.theme_text.setText(_translate("SettingsWindow", "Theme"))
        self.browse_text.setText(_translate("SettingsWindow", "Select your Minecraft directory, unless it\'s already filled in below:"))
        self.welcome_text.setText(_translate("SettingsWindow", "Welcome to the Universal In-Game Timer for Minecraft!"))
        self.browse_button.setText(_translate("SettingsWindow", "Browse"))
        self.opacity_min_text.setText(_translate("SettingsWindow", "10%"))
        self.opacity_text.setText(_translate("SettingsWindow", "Opacity"))
        self.opacity_max_text.setText(_translate("SettingsWindow", "100%"))
        self.author_text.setText(_translate("SettingsWindow", "By NinjaSnail1080"))
        self.browse_leave_empty_text.setText(_translate("SettingsWindow", "(If left empty, it\'ll look for the default Minecraft directory)"))

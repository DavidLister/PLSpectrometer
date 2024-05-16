# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'spectrometer_newFmcxoc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1641, 1072)
        MainWindow.setStyleSheet(u"background-color: rgb(209, 209, 209);\n"
"\n"
"")
        self.actionnew = QAction(MainWindow)
        self.actionnew.setObjectName(u"actionnew")
        self.actionsave = QAction(MainWindow)
        self.actionsave.setObjectName(u"actionsave")
        self.actionsave_as = QAction(MainWindow)
        self.actionsave_as.setObjectName(u"actionsave_as")
        self.actioncopy = QAction(MainWindow)
        self.actioncopy.setObjectName(u"actioncopy")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.abort_button = QPushButton(self.centralwidget)
        self.abort_button.setObjectName(u"abort_button")
        self.abort_button.setGeometry(QRect(20, 960, 101, 51))
        font = QFont()
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.abort_button.setFont(font)
        self.abort_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 18px;\n"
"}")
        self.abort_button.setAutoDefault(False)
        self.abort_button.setFlat(False)
        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.frame1.setGeometry(QRect(10, 30, 381, 161))
        self.frame1.setFrameShape(QFrame.Box)
        self.frame1.setFrameShadow(QFrame.Plain)
        self.frame1.setLineWidth(1)
        self.current_wavelength_lbl = QLabel(self.frame1)
        self.current_wavelength_lbl.setObjectName(u"current_wavelength_lbl")
        self.current_wavelength_lbl.setGeometry(QRect(10, 70, 231, 21))
        font1 = QFont()
        font1.setPointSize(10)
        self.current_wavelength_lbl.setFont(font1)
        self.shutter_btn = QPushButton(self.frame1)
        self.shutter_btn.setObjectName(u"shutter_btn")
        self.shutter_btn.setGeometry(QRect(270, 110, 101, 41))
        self.shutter_btn.setStyleSheet(u"")
        self.shutter_btn.setCheckable(True)
        self.shutter_btn.setChecked(False)
        self.status_lbl = QLabel(self.frame1)
        self.status_lbl.setObjectName(u"status_lbl")
        self.status_lbl.setGeometry(QRect(10, 100, 111, 21))
        self.status_lbl.setFont(font1)
        self.spect_select_lbl = QLabel(self.frame1)
        self.spect_select_lbl.setObjectName(u"spect_select_lbl")
        self.spect_select_lbl.setGeometry(QRect(10, 10, 121, 21))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.spect_select_lbl.setFont(font2)
        self.radioButton = QRadioButton(self.frame1)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 40, 71, 21))
        self.radioButton.setFont(font1)
        self.radioButton_2 = QRadioButton(self.frame1)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(100, 40, 81, 21))
        self.radioButton_2.setFont(font1)
        self.spect_select_lbl_2 = QLabel(self.frame1)
        self.spect_select_lbl_2.setObjectName(u"spect_select_lbl_2")
        self.spect_select_lbl_2.setGeometry(QRect(10, 130, 231, 21))
        self.spect_select_lbl_2.setFont(font2)
        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName(u"frame2")
        self.frame2.setGeometry(QRect(10, 230, 381, 171))
        self.frame2.setFrameShape(QFrame.Box)
        self.frame2.setFrameShadow(QFrame.Plain)
        self.frame2.setLineWidth(1)
        self.measured_value_lbl = QLabel(self.frame2)
        self.measured_value_lbl.setObjectName(u"measured_value_lbl")
        self.measured_value_lbl.setGeometry(QRect(210, 10, 161, 16))
        self.measured_value_lbl.setFont(font2)
        self.measured_value_input = QLineEdit(self.frame2)
        self.measured_value_input.setObjectName(u"measured_value_input")
        self.measured_value_input.setGeometry(QRect(210, 30, 113, 20))
        self.measured_value_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.measured_value_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.recalibrate_button = QPushButton(self.frame2)
        self.recalibrate_button.setObjectName(u"recalibrate_button")
        self.recalibrate_button.setGeometry(QRect(270, 110, 101, 51))
        self.recalibrate_button.setFont(font)
        self.recalibrate_button.setMouseTracking(False)
        self.recalibrate_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"	\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	\n"
"	background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"	\n"
"}")
        self.recalibrate_button.setCheckable(False)
        self.recalibrate_button.setAutoDefault(False)
        self.recalibrate_button.setFlat(False)
        self.literature_value_lbl = QLabel(self.frame2)
        self.literature_value_lbl.setObjectName(u"literature_value_lbl")
        self.literature_value_lbl.setGeometry(QRect(10, 10, 171, 16))
        self.literature_value_lbl.setFont(font2)
        self.literature_value_input = QLineEdit(self.frame2)
        self.literature_value_input.setObjectName(u"literature_value_input")
        self.literature_value_input.setGeometry(QRect(10, 30, 113, 20))
        self.literature_value_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.literature_value_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.offset_lbl = QLabel(self.frame2)
        self.offset_lbl.setObjectName(u"offset_lbl")
        self.offset_lbl.setGeometry(QRect(10, 110, 151, 16))
        self.offset_lbl.setFont(font2)
        self.corrected_lbl = QLabel(self.frame2)
        self.corrected_lbl.setObjectName(u"corrected_lbl")
        self.corrected_lbl.setGeometry(QRect(10, 140, 251, 16))
        self.corrected_lbl.setFont(font2)
        self.current_position_lbl = QLabel(self.frame2)
        self.current_position_lbl.setObjectName(u"current_position_lbl")
        self.current_position_lbl.setGeometry(QRect(10, 60, 241, 16))
        self.current_position_lbl.setFont(font2)
        self.current_position_input = QLineEdit(self.frame2)
        self.current_position_input.setObjectName(u"current_position_input")
        self.current_position_input.setGeometry(QRect(10, 80, 113, 20))
        self.current_position_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.current_position_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.frame3.setGeometry(QRect(10, 440, 381, 71))
        self.frame3.setFrameShape(QFrame.Box)
        self.frame3.setFrameShadow(QFrame.Plain)
        self.frame3.setLineWidth(1)
        self.move_input = QLineEdit(self.frame3)
        self.move_input.setObjectName(u"move_input")
        self.move_input.setGeometry(QRect(10, 40, 113, 20))
        self.move_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.move_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.move_input.setDragEnabled(False)
        self.move_input.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.go_to_lbl = QLabel(self.frame3)
        self.go_to_lbl.setObjectName(u"go_to_lbl")
        self.go_to_lbl.setGeometry(QRect(10, 10, 141, 21))
        self.go_to_lbl.setFont(font2)
        self.move_button = QPushButton(self.frame3)
        self.move_button.setObjectName(u"move_button")
        self.move_button.setGeometry(QRect(270, 10, 101, 51))
        self.move_button.setFont(font)
        self.move_button.setMouseTracking(False)
        self.move_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"	\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	\n"
"	background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"	\n"
"}")
        self.move_button.setCheckable(False)
        self.move_button.setAutoDefault(False)
        self.move_button.setFlat(False)
        self.frame4 = QFrame(self.centralwidget)
        self.frame4.setObjectName(u"frame4")
        self.frame4.setGeometry(QRect(10, 550, 381, 211))
        self.frame4.setFrameShape(QFrame.Box)
        self.frame4.setFrameShadow(QFrame.Plain)
        self.frame4.setLineWidth(1)
        self.scan_start_input = QLineEdit(self.frame4)
        self.scan_start_input.setObjectName(u"scan_start_input")
        self.scan_start_input.setGeometry(QRect(10, 30, 71, 20))
        self.scan_start_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scan_start_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.scan_start_lbl = QLabel(self.frame4)
        self.scan_start_lbl.setObjectName(u"scan_start_lbl")
        self.scan_start_lbl.setGeometry(QRect(10, 10, 101, 16))
        self.scan_start_lbl.setFont(font2)
        self.scan_end_lbl = QLabel(self.frame4)
        self.scan_end_lbl.setObjectName(u"scan_end_lbl")
        self.scan_end_lbl.setGeometry(QRect(130, 10, 101, 16))
        self.scan_end_lbl.setFont(font2)
        self.scan_step_input = QLineEdit(self.frame4)
        self.scan_step_input.setObjectName(u"scan_step_input")
        self.scan_step_input.setGeometry(QRect(10, 80, 71, 20))
        self.scan_step_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scan_step_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.scan_button = QPushButton(self.frame4)
        self.scan_button.setObjectName(u"scan_button")
        self.scan_button.setGeometry(QRect(270, 10, 101, 51))
        self.scan_button.setFont(font)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"	\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	\n"
"	background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"	\n"
"}")
        self.scan_button.setCheckable(False)
        self.scan_button.setAutoDefault(False)
        self.scan_button.setFlat(False)
        self.scan_step_lbl = QLabel(self.frame4)
        self.scan_step_lbl.setObjectName(u"scan_step_lbl")
        self.scan_step_lbl.setGeometry(QRect(10, 60, 111, 16))
        self.scan_step_lbl.setFont(font2)
        self.scan_end_input = QLineEdit(self.frame4)
        self.scan_end_input.setObjectName(u"scan_end_input")
        self.scan_end_input.setGeometry(QRect(130, 30, 71, 20))
        self.scan_end_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.scan_end_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.file_name_lbl = QLabel(self.frame4)
        self.file_name_lbl.setObjectName(u"file_name_lbl")
        self.file_name_lbl.setGeometry(QRect(10, 110, 121, 21))
        self.file_name_lbl.setFont(font2)
        self.file_name_input = QLineEdit(self.frame4)
        self.file_name_input.setObjectName(u"file_name_input")
        self.file_name_input.setGeometry(QRect(10, 130, 231, 20))
        self.file_name_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sample_id_lbl = QLabel(self.frame4)
        self.sample_id_lbl.setObjectName(u"sample_id_lbl")
        self.sample_id_lbl.setGeometry(QRect(10, 160, 121, 21))
        self.sample_id_lbl.setFont(font2)
        self.sample_ID_input = QLineEdit(self.frame4)
        self.sample_ID_input.setObjectName(u"sample_ID_input")
        self.sample_ID_input.setGeometry(QRect(10, 180, 231, 20))
        self.sample_ID_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.count_time_lbl = QLabel(self.frame4)
        self.count_time_lbl.setObjectName(u"count_time_lbl")
        self.count_time_lbl.setGeometry(QRect(130, 60, 121, 16))
        self.count_time_lbl.setFont(font2)
        self.count_time_input = QLineEdit(self.frame4)
        self.count_time_input.setObjectName(u"count_time_input")
        self.count_time_input.setGeometry(QRect(130, 80, 71, 20))
        self.count_time_input.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.count_time_input.setInputMethodHints(Qt.ImhDigitsOnly)
        self.repeat_btn = QPushButton(self.frame4)
        self.repeat_btn.setObjectName(u"repeat_btn")
        self.repeat_btn.setGeometry(QRect(320, 70, 51, 23))
        self.repeat_btn.setCheckable(True)
        self.perform_scan_lbl = QLabel(self.centralwidget)
        self.perform_scan_lbl.setObjectName(u"perform_scan_lbl")
        self.perform_scan_lbl.setGeometry(QRect(10, 520, 211, 21))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setWeight(75)
        self.perform_scan_lbl.setFont(font3)
        self.move_spectrometer_lbl = QLabel(self.centralwidget)
        self.move_spectrometer_lbl.setObjectName(u"move_spectrometer_lbl")
        self.move_spectrometer_lbl.setGeometry(QRect(10, 410, 181, 21))
        self.move_spectrometer_lbl.setFont(font3)
        self.recalibrate_lbl = QLabel(self.centralwidget)
        self.recalibrate_lbl.setObjectName(u"recalibrate_lbl")
        self.recalibrate_lbl.setGeometry(QRect(10, 200, 251, 21))
        self.recalibrate_lbl.setFont(font3)
        self.position_lbl = QLabel(self.centralwidget)
        self.position_lbl.setObjectName(u"position_lbl")
        self.position_lbl.setGeometry(QRect(10, 0, 201, 21))
        self.position_lbl.setFont(font3)
        self.frame5 = QFrame(self.centralwidget)
        self.frame5.setObjectName(u"frame5")
        self.frame5.setGeometry(QRect(10, 800, 381, 151))
        self.frame5.setFrameShape(QFrame.Box)
        self.frame5.setFrameShadow(QFrame.Plain)
        self.frame5.setLineWidth(1)
        self.label = QLabel(self.frame5)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(230, 60, 61, 16))
        self.optimize_btn = QPushButton(self.frame5)
        self.optimize_btn.setObjectName(u"optimize_btn")
        self.optimize_btn.setGeometry(QRect(10, 20, 101, 51))
        self.optimize_btn.setFont(font)
        self.optimize_btn.setMouseTracking(False)
        self.optimize_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"	\n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"	\n"
"	background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"	\n"
"}")
        self.optimize_btn.setCheckable(False)
        self.optimize_btn.setAutoDefault(False)
        self.optimize_btn.setFlat(False)
        self.optimize_stp_btn = QPushButton(self.frame5)
        self.optimize_stp_btn.setObjectName(u"optimize_stp_btn")
        self.optimize_stp_btn.setGeometry(QRect(10, 80, 101, 51))
        self.optimize_stp_btn.setFont(font)
        self.optimize_stp_btn.setMouseTracking(False)
        self.optimize_stp_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 0, 0);\n"
"	font: 18px;\n"
"}")
        self.optimize_stp_btn.setCheckable(False)
        self.optimize_stp_btn.setAutoDefault(False)
        self.optimize_stp_btn.setFlat(False)
        self.optimize_lbl = QLabel(self.centralwidget)
        self.optimize_lbl.setObjectName(u"optimize_lbl")
        self.optimize_lbl.setGeometry(QRect(10, 770, 91, 21))
        self.optimize_lbl.setFont(font3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1641, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)

        self.abort_button.setDefault(False)
        self.recalibrate_button.setDefault(False)
        self.move_button.setDefault(False)
        self.scan_button.setDefault(False)
        self.optimize_btn.setDefault(False)
        self.optimize_stp_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionnew.setText(QCoreApplication.translate("MainWindow", u"new", None))
        self.actionsave.setText(QCoreApplication.translate("MainWindow", u"save", None))
        self.actionsave_as.setText(QCoreApplication.translate("MainWindow", u"save as", None))
        self.actioncopy.setText(QCoreApplication.translate("MainWindow", u"copy", None))
        self.abort_button.setText(QCoreApplication.translate("MainWindow", u"Abort", None))
        self.current_wavelength_lbl.setText(QCoreApplication.translate("MainWindow", u"Position (nm):", None))
        self.shutter_btn.setText(QCoreApplication.translate("MainWindow", u"Shutter Opened", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"Status: Idle", None))
        self.spect_select_lbl.setText(QCoreApplication.translate("MainWindow", u"Spectrometer", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"double", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"single", None))
        self.spect_select_lbl_2.setText(QCoreApplication.translate("MainWindow", u"Pulse Frequency (Hz): 2000 ", None))
        self.measured_value_lbl.setText(QCoreApplication.translate("MainWindow", u"Measured Value (nm)", None))
        self.recalibrate_button.setText(QCoreApplication.translate("MainWindow", u"Recalibrate", None))
        self.literature_value_lbl.setText(QCoreApplication.translate("MainWindow", u"Expected Value (nm)", None))
        self.literature_value_input.setText(QCoreApplication.translate("MainWindow", u"365.016", None))
        self.offset_lbl.setText(QCoreApplication.translate("MainWindow", u"Offset (nm):", None))
        self.corrected_lbl.setText(QCoreApplication.translate("MainWindow", u"Position After Correction (nm):", None))
        self.current_position_lbl.setText(QCoreApplication.translate("MainWindow", u"Position Before Correction (nm)", None))
        self.move_input.setText("")
        self.go_to_lbl.setText(QCoreApplication.translate("MainWindow", u"Go to Value (nm)", None))
        self.move_button.setText(QCoreApplication.translate("MainWindow", u"Move", None))
        self.scan_start_lbl.setText(QCoreApplication.translate("MainWindow", u"Start (nm)", None))
        self.scan_end_lbl.setText(QCoreApplication.translate("MainWindow", u"End (nm)", None))
        self.scan_button.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.scan_step_lbl.setText(QCoreApplication.translate("MainWindow", u"Step Size (nm)", None))
        self.file_name_lbl.setText(QCoreApplication.translate("MainWindow", u"File Name", None))
        self.sample_id_lbl.setText(QCoreApplication.translate("MainWindow", u"Sample ID", None))
        self.count_time_lbl.setText(QCoreApplication.translate("MainWindow", u"Count Time (s)", None))
        self.repeat_btn.setText(QCoreApplication.translate("MainWindow", u"Repeat", None))
        self.perform_scan_lbl.setText(QCoreApplication.translate("MainWindow", u"Perform Scan", None))
        self.move_spectrometer_lbl.setText(QCoreApplication.translate("MainWindow", u"Move Spectrometer", None))
        self.recalibrate_lbl.setText(QCoreApplication.translate("MainWindow", u"Recalibrate Spectrometer", None))
        self.position_lbl.setText(QCoreApplication.translate("MainWindow", u"Position and Movement", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"counts/s:", None))
        self.optimize_btn.setText(QCoreApplication.translate("MainWindow", u"Go", None))
        self.optimize_stp_btn.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.optimize_lbl.setText(QCoreApplication.translate("MainWindow", u"Optimize", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
    # retranslateUi


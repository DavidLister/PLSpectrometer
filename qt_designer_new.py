# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'spectrometer_new.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1641, 1072)
        MainWindow.setStyleSheet("background-color: rgb(209, 209, 209);\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.abort_button = QtWidgets.QPushButton(self.centralwidget)
        self.abort_button.setGeometry(QtCore.QRect(20, 960, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.abort_button.setFont(font)
        self.abort_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    font: 18px;\n"
"}")
        self.abort_button.setAutoDefault(False)
        self.abort_button.setDefault(False)
        self.abort_button.setFlat(False)
        self.abort_button.setObjectName("abort_button")
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setGeometry(QtCore.QRect(10, 30, 381, 161))
        self.frame1.setFrameShape(QtWidgets.QFrame.Box)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame1.setLineWidth(1)
        self.frame1.setObjectName("frame1")
        self.current_wavelength_lbl = QtWidgets.QLabel(self.frame1)
        self.current_wavelength_lbl.setGeometry(QtCore.QRect(10, 70, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.current_wavelength_lbl.setFont(font)
        self.current_wavelength_lbl.setObjectName("current_wavelength_lbl")
        self.shutter_btn = QtWidgets.QPushButton(self.frame1)
        self.shutter_btn.setGeometry(QtCore.QRect(270, 110, 101, 41))
        self.shutter_btn.setStyleSheet("")
        self.shutter_btn.setCheckable(True)
        self.shutter_btn.setChecked(False)
        self.shutter_btn.setObjectName("shutter_btn")
        self.status_lbl = QtWidgets.QLabel(self.frame1)
        self.status_lbl.setGeometry(QtCore.QRect(10, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.status_lbl.setFont(font)
        self.status_lbl.setObjectName("status_lbl")
        self.spect_select_lbl = QtWidgets.QLabel(self.frame1)
        self.spect_select_lbl.setGeometry(QtCore.QRect(10, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spect_select_lbl.setFont(font)
        self.spect_select_lbl.setObjectName("spect_select_lbl")
        self.radioButton = QtWidgets.QRadioButton(self.frame1)
        self.radioButton.setGeometry(QtCore.QRect(10, 40, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame1)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 40, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.spect_select_lbl_2 = QtWidgets.QLabel(self.frame1)
        self.spect_select_lbl_2.setGeometry(QtCore.QRect(10, 130, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.spect_select_lbl_2.setFont(font)
        self.spect_select_lbl_2.setObjectName("spect_select_lbl_2")
        self.frame2 = QtWidgets.QFrame(self.centralwidget)
        self.frame2.setGeometry(QtCore.QRect(10, 230, 381, 171))
        self.frame2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame2.setLineWidth(1)
        self.frame2.setObjectName("frame2")
        self.measured_value_lbl = QtWidgets.QLabel(self.frame2)
        self.measured_value_lbl.setGeometry(QtCore.QRect(210, 10, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.measured_value_lbl.setFont(font)
        self.measured_value_lbl.setObjectName("measured_value_lbl")
        self.measured_value_input = QtWidgets.QLineEdit(self.frame2)
        self.measured_value_input.setGeometry(QtCore.QRect(210, 30, 113, 20))
        self.measured_value_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.measured_value_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.measured_value_input.setObjectName("measured_value_input")
        self.recalibrate_button = QtWidgets.QPushButton(self.frame2)
        self.recalibrate_button.setGeometry(QtCore.QRect(270, 110, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.recalibrate_button.setFont(font)
        self.recalibrate_button.setMouseTracking(False)
        self.recalibrate_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.recalibrate_button.setCheckable(False)
        self.recalibrate_button.setAutoDefault(False)
        self.recalibrate_button.setDefault(False)
        self.recalibrate_button.setFlat(False)
        self.recalibrate_button.setObjectName("recalibrate_button")
        self.literature_value_lbl = QtWidgets.QLabel(self.frame2)
        self.literature_value_lbl.setGeometry(QtCore.QRect(10, 10, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.literature_value_lbl.setFont(font)
        self.literature_value_lbl.setObjectName("literature_value_lbl")
        self.literature_value_input = QtWidgets.QLineEdit(self.frame2)
        self.literature_value_input.setGeometry(QtCore.QRect(10, 30, 113, 20))
        self.literature_value_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.literature_value_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.literature_value_input.setObjectName("literature_value_input")
        self.offset_lbl = QtWidgets.QLabel(self.frame2)
        self.offset_lbl.setGeometry(QtCore.QRect(10, 110, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.offset_lbl.setFont(font)
        self.offset_lbl.setObjectName("offset_lbl")
        self.corrected_lbl = QtWidgets.QLabel(self.frame2)
        self.corrected_lbl.setGeometry(QtCore.QRect(10, 140, 251, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.corrected_lbl.setFont(font)
        self.corrected_lbl.setObjectName("corrected_lbl")
        self.current_position_lbl = QtWidgets.QLabel(self.frame2)
        self.current_position_lbl.setGeometry(QtCore.QRect(10, 60, 241, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.current_position_lbl.setFont(font)
        self.current_position_lbl.setObjectName("current_position_lbl")
        self.current_position_input = QtWidgets.QLineEdit(self.frame2)
        self.current_position_input.setGeometry(QtCore.QRect(10, 80, 113, 20))
        self.current_position_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.current_position_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.current_position_input.setObjectName("current_position_input")
        self.frame3 = QtWidgets.QFrame(self.centralwidget)
        self.frame3.setGeometry(QtCore.QRect(10, 440, 381, 71))
        self.frame3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame3.setLineWidth(1)
        self.frame3.setObjectName("frame3")
        self.move_input = QtWidgets.QLineEdit(self.frame3)
        self.move_input.setGeometry(QtCore.QRect(10, 40, 113, 20))
        self.move_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.move_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.move_input.setText("")
        self.move_input.setDragEnabled(False)
        self.move_input.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.move_input.setObjectName("move_input")
        self.go_to_lbl = QtWidgets.QLabel(self.frame3)
        self.go_to_lbl.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.go_to_lbl.setFont(font)
        self.go_to_lbl.setObjectName("go_to_lbl")
        self.move_button = QtWidgets.QPushButton(self.frame3)
        self.move_button.setGeometry(QtCore.QRect(270, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.move_button.setFont(font)
        self.move_button.setMouseTracking(False)
        self.move_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.move_button.setCheckable(False)
        self.move_button.setAutoDefault(False)
        self.move_button.setDefault(False)
        self.move_button.setFlat(False)
        self.move_button.setObjectName("move_button")
        self.frame4 = QtWidgets.QFrame(self.centralwidget)
        self.frame4.setGeometry(QtCore.QRect(10, 550, 381, 211))
        self.frame4.setFrameShape(QtWidgets.QFrame.Box)
        self.frame4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame4.setLineWidth(1)
        self.frame4.setObjectName("frame4")
        self.scan_start_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_start_input.setGeometry(QtCore.QRect(10, 30, 71, 20))
        self.scan_start_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scan_start_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_start_input.setObjectName("scan_start_input")
        self.scan_start_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_start_lbl.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scan_start_lbl.setFont(font)
        self.scan_start_lbl.setObjectName("scan_start_lbl")
        self.scan_end_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_end_lbl.setGeometry(QtCore.QRect(130, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scan_end_lbl.setFont(font)
        self.scan_end_lbl.setObjectName("scan_end_lbl")
        self.scan_step_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_step_input.setGeometry(QtCore.QRect(10, 80, 71, 20))
        self.scan_step_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scan_step_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_step_input.setObjectName("scan_step_input")
        self.scan_button = QtWidgets.QPushButton(self.frame4)
        self.scan_button.setGeometry(QtCore.QRect(270, 10, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.scan_button.setFont(font)
        self.scan_button.setMouseTracking(False)
        self.scan_button.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.scan_button.setCheckable(False)
        self.scan_button.setAutoDefault(False)
        self.scan_button.setDefault(False)
        self.scan_button.setFlat(False)
        self.scan_button.setObjectName("scan_button")
        self.scan_step_lbl = QtWidgets.QLabel(self.frame4)
        self.scan_step_lbl.setGeometry(QtCore.QRect(10, 60, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.scan_step_lbl.setFont(font)
        self.scan_step_lbl.setObjectName("scan_step_lbl")
        self.scan_end_input = QtWidgets.QLineEdit(self.frame4)
        self.scan_end_input.setGeometry(QtCore.QRect(130, 30, 71, 20))
        self.scan_end_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scan_end_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.scan_end_input.setObjectName("scan_end_input")
        self.file_name_lbl = QtWidgets.QLabel(self.frame4)
        self.file_name_lbl.setGeometry(QtCore.QRect(10, 110, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.file_name_lbl.setFont(font)
        self.file_name_lbl.setObjectName("file_name_lbl")
        self.file_name_input = QtWidgets.QLineEdit(self.frame4)
        self.file_name_input.setGeometry(QtCore.QRect(10, 130, 231, 20))
        self.file_name_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.file_name_input.setObjectName("file_name_input")
        self.sample_id_lbl = QtWidgets.QLabel(self.frame4)
        self.sample_id_lbl.setGeometry(QtCore.QRect(10, 160, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.sample_id_lbl.setFont(font)
        self.sample_id_lbl.setObjectName("sample_id_lbl")
        self.sample_ID_input = QtWidgets.QLineEdit(self.frame4)
        self.sample_ID_input.setGeometry(QtCore.QRect(10, 180, 231, 20))
        self.sample_ID_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.sample_ID_input.setObjectName("sample_ID_input")
        self.count_time_lbl = QtWidgets.QLabel(self.frame4)
        self.count_time_lbl.setGeometry(QtCore.QRect(130, 60, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.count_time_lbl.setFont(font)
        self.count_time_lbl.setObjectName("count_time_lbl")
        self.count_time_input = QtWidgets.QLineEdit(self.frame4)
        self.count_time_input.setGeometry(QtCore.QRect(130, 80, 71, 20))
        self.count_time_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.count_time_input.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.count_time_input.setObjectName("count_time_input")
        self.repeat_btn = QtWidgets.QPushButton(self.frame4)
        self.repeat_btn.setGeometry(QtCore.QRect(320, 70, 51, 23))
        self.repeat_btn.setCheckable(True)
        self.repeat_btn.setObjectName("repeat_btn")
        self.perform_scan_lbl = QtWidgets.QLabel(self.centralwidget)
        self.perform_scan_lbl.setGeometry(QtCore.QRect(10, 520, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.perform_scan_lbl.setFont(font)
        self.perform_scan_lbl.setObjectName("perform_scan_lbl")
        self.move_spectrometer_lbl = QtWidgets.QLabel(self.centralwidget)
        self.move_spectrometer_lbl.setGeometry(QtCore.QRect(10, 410, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.move_spectrometer_lbl.setFont(font)
        self.move_spectrometer_lbl.setObjectName("move_spectrometer_lbl")
        self.recalibrate_lbl = QtWidgets.QLabel(self.centralwidget)
        self.recalibrate_lbl.setGeometry(QtCore.QRect(10, 200, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.recalibrate_lbl.setFont(font)
        self.recalibrate_lbl.setObjectName("recalibrate_lbl")
        self.position_lbl = QtWidgets.QLabel(self.centralwidget)
        self.position_lbl.setGeometry(QtCore.QRect(10, 0, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.position_lbl.setFont(font)
        self.position_lbl.setObjectName("position_lbl")
        self.frame5 = QtWidgets.QFrame(self.centralwidget)
        self.frame5.setGeometry(QtCore.QRect(10, 800, 381, 151))
        self.frame5.setFrameShape(QtWidgets.QFrame.Box)
        self.frame5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame5.setLineWidth(1)
        self.frame5.setObjectName("frame5")
        self.label = QtWidgets.QLabel(self.frame5)
        self.label.setGeometry(QtCore.QRect(230, 60, 61, 16))
        self.label.setObjectName("label")
        self.optimize_btn = QtWidgets.QPushButton(self.frame5)
        self.optimize_btn.setGeometry(QtCore.QRect(10, 20, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.optimize_btn.setFont(font)
        self.optimize_btn.setMouseTracking(False)
        self.optimize_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(64, 137, 255);\n"
"    font: 18px;\n"
"    min-width: 2em;\n"
"    padding: 6px;\n"
"    \n"
"}\n"
"\n"
"QPushButton::pressed{\n"
"    \n"
"    background-color: rgb(64, 137, 255);\n"
"    min-width: 5em;\n"
"    padding: 6px;\n"
"    \n"
"}")
        self.optimize_btn.setCheckable(False)
        self.optimize_btn.setAutoDefault(False)
        self.optimize_btn.setDefault(False)
        self.optimize_btn.setFlat(False)
        self.optimize_btn.setObjectName("optimize_btn")
        self.optimize_stp_btn = QtWidgets.QPushButton(self.frame5)
        self.optimize_stp_btn.setGeometry(QtCore.QRect(10, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.optimize_stp_btn.setFont(font)
        self.optimize_stp_btn.setMouseTracking(False)
        self.optimize_stp_btn.setStyleSheet("QPushButton{\n"
"    background-color: rgb(255, 0, 0);\n"
"    font: 18px;\n"
"}")
        self.optimize_stp_btn.setCheckable(False)
        self.optimize_stp_btn.setAutoDefault(False)
        self.optimize_stp_btn.setDefault(False)
        self.optimize_stp_btn.setFlat(False)
        self.optimize_stp_btn.setObjectName("optimize_stp_btn")
        self.optimize_lbl = QtWidgets.QLabel(self.centralwidget)
        self.optimize_lbl.setGeometry(QtCore.QRect(10, 770, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.optimize_lbl.setFont(font)
        self.optimize_lbl.setObjectName("optimize_lbl")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1641, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionnew = QtWidgets.QAction(MainWindow)
        self.actionnew.setObjectName("actionnew")
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        self.actionsave_as = QtWidgets.QAction(MainWindow)
        self.actionsave_as.setObjectName("actionsave_as")
        self.actioncopy = QtWidgets.QAction(MainWindow)
        self.actioncopy.setObjectName("actioncopy")
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.abort_button.setText(_translate("MainWindow", "Abort"))
        self.current_wavelength_lbl.setText(_translate("MainWindow", "Position (nm):"))
        self.shutter_btn.setText(_translate("MainWindow", "Shutter Opened"))
        self.status_lbl.setText(_translate("MainWindow", "Status: Idle"))
        self.spect_select_lbl.setText(_translate("MainWindow", "Spectrometer"))
        self.radioButton.setText(_translate("MainWindow", "double"))
        self.radioButton_2.setText(_translate("MainWindow", "single"))
        self.spect_select_lbl_2.setText(_translate("MainWindow", "Pulse Frequency (Hz): 2000 "))
        self.measured_value_lbl.setText(_translate("MainWindow", "Measured Value (nm)"))
        self.recalibrate_button.setText(_translate("MainWindow", "Recalibrate"))
        self.literature_value_lbl.setText(_translate("MainWindow", "Expected Value (nm)"))
        self.literature_value_input.setText(_translate("MainWindow", "365.016"))
        self.offset_lbl.setText(_translate("MainWindow", "Offset (nm):"))
        self.corrected_lbl.setText(_translate("MainWindow", "Position After Correction (nm):"))
        self.current_position_lbl.setText(_translate("MainWindow", "Position Before Correction (nm)"))
        self.go_to_lbl.setText(_translate("MainWindow", "Go to Value (nm)"))
        self.move_button.setText(_translate("MainWindow", "Move"))
        self.scan_start_lbl.setText(_translate("MainWindow", "Start (nm)"))
        self.scan_end_lbl.setText(_translate("MainWindow", "End (nm)"))
        self.scan_button.setText(_translate("MainWindow", "Scan"))
        self.scan_step_lbl.setText(_translate("MainWindow", "Step Size (nm)"))
        self.file_name_lbl.setText(_translate("MainWindow", "File Name"))
        self.sample_id_lbl.setText(_translate("MainWindow", "Sample ID"))
        self.count_time_lbl.setText(_translate("MainWindow", "Count Time (s)"))
        self.repeat_btn.setText(_translate("MainWindow", "Repeat"))
        self.perform_scan_lbl.setText(_translate("MainWindow", "Perform Scan"))
        self.move_spectrometer_lbl.setText(_translate("MainWindow", "Move Spectrometer"))
        self.recalibrate_lbl.setText(_translate("MainWindow", "Recalibrate Spectrometer"))
        self.position_lbl.setText(_translate("MainWindow", "Position and Movement"))
        self.label.setText(_translate("MainWindow", "counts/s:"))
        self.optimize_btn.setText(_translate("MainWindow", "Go"))
        self.optimize_stp_btn.setText(_translate("MainWindow", "Stop"))
        self.optimize_lbl.setText(_translate("MainWindow", "Optimize"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionnew.setText(_translate("MainWindow", "new"))
        self.actionsave.setText(_translate("MainWindow", "save"))
        self.actionsave_as.setText(_translate("MainWindow", "save as"))
        self.actioncopy.setText(_translate("MainWindow", "copy"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qtdesigner.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TemperatureSensor(object):
    def setupUi(self, TemperatureSensor):
        TemperatureSensor.setObjectName("TemperatureSensor")
        TemperatureSensor.resize(333, 248)
        self.centralwidget = QtWidgets.QWidget(TemperatureSensor)
        self.centralwidget.setObjectName("centralwidget")
        self.temperature_label = QtWidgets.QLabel(self.centralwidget)
        self.temperature_label.setGeometry(QtCore.QRect(10, 10, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.temperature_label.setFont(font)
        self.temperature_label.setObjectName("temperature_label")
        self.start_button = QtWidgets.QPushButton(self.centralwidget)
        self.start_button.setGeometry(QtCore.QRect(10, 170, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")
        self.stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.stop_button.setGeometry(QtCore.QRect(120, 170, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.stop_button.setFont(font)
        self.stop_button.setObjectName("stop_button")
        self.temperature_output = QtWidgets.QLabel(self.centralwidget)
        self.temperature_output.setGeometry(QtCore.QRect(190, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.temperature_output.setFont(font)
        self.temperature_output.setText("")
        self.temperature_output.setObjectName("temperature_output")
        self.range_label = QtWidgets.QLabel(self.centralwidget)
        self.range_label.setGeometry(QtCore.QRect(10, 40, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.range_label.setFont(font)
        self.range_label.setObjectName("range_label")
        self.range_output = QtWidgets.QLabel(self.centralwidget)
        self.range_output.setGeometry(QtCore.QRect(190, 40, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.range_output.setFont(font)
        self.range_output.setText("")
        self.range_output.setObjectName("range_output")
        self.interval_label = QtWidgets.QLabel(self.centralwidget)
        self.interval_label.setGeometry(QtCore.QRect(10, 100, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.interval_label.setFont(font)
        self.interval_label.setObjectName("interval_label")
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(230, 170, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.refresh_button.setFont(font)
        self.refresh_button.setObjectName("refresh_button")
        self.interval_input = QtWidgets.QLineEdit(self.centralwidget)
        self.interval_input.setGeometry(QtCore.QRect(190, 100, 111, 22))
        self.interval_input.setObjectName("interval_input")
        self.voltage_label = QtWidgets.QLabel(self.centralwidget)
        self.voltage_label.setGeometry(QtCore.QRect(10, 130, 161, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.voltage_label.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.voltage_label.setFont(font)
        self.voltage_label.setObjectName("voltage_label")
        self.voltage_output = QtWidgets.QLabel(self.centralwidget)
        self.voltage_output.setGeometry(QtCore.QRect(190, 130, 111, 21))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(160, 160, 160))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.voltage_output.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.voltage_output.setFont(font)
        self.voltage_output.setText("")
        self.voltage_output.setObjectName("voltage_output")
        TemperatureSensor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TemperatureSensor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 333, 26))
        self.menubar.setObjectName("menubar")
        TemperatureSensor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TemperatureSensor)
        self.statusbar.setObjectName("statusbar")
        TemperatureSensor.setStatusBar(self.statusbar)

        self.retranslateUi(TemperatureSensor)
        QtCore.QMetaObject.connectSlotsByName(TemperatureSensor)

    def retranslateUi(self, TemperatureSensor):
        _translate = QtCore.QCoreApplication.translate
        TemperatureSensor.setWindowTitle(_translate("TemperatureSensor", "MainWindow"))
        self.temperature_label.setText(_translate("TemperatureSensor", "Temperature (°C):"))
        self.start_button.setText(_translate("TemperatureSensor", "Start"))
        self.stop_button.setText(_translate("TemperatureSensor", "Stop"))
        self.range_label.setText(_translate("TemperatureSensor", "Maximum Range (°C):"))
        self.interval_label.setText(_translate("TemperatureSensor", "Collection Interval (s):"))
        self.refresh_button.setText(_translate("TemperatureSensor", "Refresh"))
        self.interval_input.setText(_translate("TemperatureSensor", "1"))
        self.voltage_label.setText(_translate("TemperatureSensor", "Resistor Voltage (V):"))
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui\mian.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(210, 384)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 191, 431))
        self.widget.setObjectName("widget")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.widget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 191, 426))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label_2)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_14.setObjectName("label_14")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.combox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.combox.setObjectName("combox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.combox)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_15.setObjectName("label_15")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.typebox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.typebox.setObjectName("typebox")
        self.typebox.addItem("")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.typebox)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.readButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.readButton.setObjectName("readButton")
        self.gridLayout_2.addWidget(self.readButton, 0, 0, 1, 1)
        self.comButton = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.comButton.setObjectName("comButton")
        self.gridLayout_2.addWidget(self.comButton, 0, 1, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 1, 0, 1, 2)
        self.formLayout_4.setLayout(4, QtWidgets.QFormLayout.SpanningRole, self.gridLayout_2)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_16.setObjectName("label_16")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.sn = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.sn.setObjectName("sn")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.sn)
        self.save_id = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.save_id.setObjectName("save_id")
        self.formLayout_4.setWidget(6, QtWidgets.QFormLayout.SpanningRole, self.save_id)
        self.line_6 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.formLayout_4.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.line_6)
        self.line_4 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.formLayout_4.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.line_4)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.wifi = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.wifi.setObjectName("wifi")
        self.formLayout_4.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.wifi)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.wifi_pass = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.wifi_pass.setObjectName("wifi_pass")
        self.formLayout_4.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.wifi_pass)
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.tcp_ip = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.tcp_ip.setObjectName("tcp_ip")
        self.formLayout_4.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.tcp_ip)
        self.save_wifi = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.save_wifi.setObjectName("save_wifi")
        self.formLayout_4.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.save_wifi)
        self.line_5 = QtWidgets.QFrame(self.formLayoutWidget_2)
        self.line_5.setEnabled(False)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.formLayout_4.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.line_5)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.upload_path = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.upload_path.setObjectName("upload_path")
        self.formLayout_4.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.upload_path)
        self.uploa_data = QtWidgets.QPushButton(self.formLayoutWidget_2)
        self.uploa_data.setObjectName("uploa_data")
        self.formLayout_4.setWidget(16, QtWidgets.QFormLayout.SpanningRole, self.uploa_data)
        self.formLayout_3.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.formLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 210, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "恒达设备助手"))
        self.label_2.setText(_translate("MainWindow", "恒达设备助手"))
        self.label_14.setText(_translate("MainWindow", "串口地址"))
        self.label_15.setText(_translate("MainWindow", "设备类型"))
        self.typebox.setItemText(0, _translate("MainWindow", "绝缘表"))
        self.readButton.setText(_translate("MainWindow", "读取设备"))
        self.comButton.setText(_translate("MainWindow", "刷新串口"))
        self.label_16.setText(_translate("MainWindow", "设备编号"))
        self.save_id.setText(_translate("MainWindow", "写入设备编号"))
        self.label_18.setText(_translate("MainWindow", "wifi名称"))
        self.label_19.setText(_translate("MainWindow", "wifi密码"))
        self.label_20.setText(_translate("MainWindow", "服务地址"))
        self.save_wifi.setText(_translate("MainWindow", "写入网路设置"))
        self.label_3.setText(_translate("MainWindow", "上传地址"))
        self.uploa_data.setText(_translate("MainWindow", "上传数据"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

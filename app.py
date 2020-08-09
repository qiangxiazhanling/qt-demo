import sys
import py_fun
from PyQt5 import QtWidgets, QtCore
from main_win import Ui_MainWindow


def init_ui(ui): 
  ui.comButton.clicked.connect(lambda :py_fun.port_list(ui))
  ui.readButton.clicked.connect(lambda :py_fun.read_equipment(ui))
  ui.save_id.clicked.connect(lambda :py_fun.write_jy_sn(ui))
  ui.save_wifi.clicked.connect(lambda :py_fun.write_jy_net_setting(ui))
  ui.uploa_data.clicked.connect(lambda :py_fun.upload_jys_data(ui))

app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
init_ui(ui)

mainWindow.show()
py_fun.port_list(ui)
sys.exit(app.exec_())
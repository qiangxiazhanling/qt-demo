import sys
import py_fun
import threading
from PyQt5 import QtWidgets, QtCore
from main_win import Ui_MainWindow


def init_ui(ui): 
  ui.comButton.clicked.connect(lambda :threading.Thread(target=py_fun.port_list, args=(ui,), name='port_list').start())
  ui.readButton.clicked.connect(lambda :threading.Thread(target=py_fun.read_equipment, args=(ui,), name='read_equipment').start())
  ui.save_id.clicked.connect(lambda :threading.Thread(target=py_fun.write_jy_sn, args=(ui,), name='py_fun.write_jy_sn').start())
  ui.save_wifi.clicked.connect(lambda :threading.Thread(target=py_fun.write_jy_net_setting, args=(ui,), name='py_fun.write_jy_net_setting').start())
  ui.uploa_data.clicked.connect(lambda :threading.Thread(target=py_fun.upload_jys_data, args=(ui,), name='py_fun.upload_jys_data').start())
  # ui.readButton.clicked.connect(lambda :py_fun.read_fs_equipment(ui))
  # ui.save_id.clicked.connect(lambda :py_fun.write_fs_sn(ui))
  # ui.save_wifi.clicked.connect(lambda :py_fun.write_fs_setting(ui))
  # ui.uploa_data.clicked.connect(lambda :py_fun.upload_fs_data(ui))
  # ui.typebox.currentIndexChanged.connect(lambda :py_fun.clear(ui))
  # ui.combox.currentIndexChanged.connect(lambda :py_fun.clear(ui))
  ui.statusbar.showMessage('欢迎')
 
app = QtWidgets.QApplication(sys.argv)
mainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(mainWindow)
init_ui(ui)
# mainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())
mainWindow.show()
py_fun.port_list(ui)
sys.exit(app.exec_())
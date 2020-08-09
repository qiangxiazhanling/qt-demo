from PyQt5.QtCore import QIODevice, QByteArray, QDate, QTime, QDateTime, Qt
from PyQt5.QtSerialPort import QSerialPortInfo, QSerialPort
from PyQt5.QtWidgets import QMessageBox, QWidget

jy_end = 64

jyid4 = []

def get_jy_port(comName):
  port = QSerialPort(comName)
  port.setBaudRate(QSerialPort.Baud57600)
  port.setParity(QSerialPort.NoParity)
  port.setDataBits(QSerialPort.Data8)
  port.setStopBits(QSerialPort.OneStop)
  port.setFlowControl(QSerialPort.NoFlowControl)
  return port

def port_list(ui):
  for port in QSerialPortInfo.availablePorts():
    ui.combox.addItem(port.portName())
def read_equipment(ui):
  comName = ui.combox.currentText()
  arduino = QSerialPortInfo(comName)
  if arduino.isBusy():
    show_warning(ui)
  else:
    port = get_jy_port(comName)
    if port.open(QIODevice.ReadWrite):
      now = QDate.currentDate()
      time = QTime.currentTime()
      port.write(bytes.fromhex('7e05f5e0ff07a8'+now.toString(Qt.ISODate).replace('-','')+ str(time.hour()) +str(time.minute())+'00')) 
      port.setReadBufferSize(jy_end)
      if port.waitForBytesWritten():
        read_hex = []
        while True:
          if port.waitForReadyRead():
            data = port.read(jy_end)
            read_hex+= to_hex(data)
            if (len(read_hex) == jy_end):
              break
        jyid4.append(read_hex[1])
        jyid4.append(read_hex[2])
        jyid4.append(read_hex[3])
        jyid4.append(read_hex[4])
        ui.sn.setText(str(int(read_hex[1]+read_hex[2]+read_hex[3]+read_hex[4],16)))
      port.close()

def write_jy_sn(ui):
  comName = ui.combox.currentText()
  arduino = QSerialPortInfo(comName)
  if arduino.isBusy():
    show_warning(ui)
  else:
    port = get_jy_port(comName)
    if port.open(QIODevice.ReadWrite):
      id4 = hex(int(ui.sn.text())).replace('0x','')
      inx = 8 - len(id4)
      for i in range(0,inx):
        id4 = '0' + id4 
      port.write(bytes.fromhex('7E05F5E0FF0AA1'+id4+'0000000000')) 
      port.setReadBufferSize(jy_end)
      if port.waitForBytesWritten():
        read_hex = []
        while True:
          if port.waitForReadyRead():
            data = port.read(jy_end)
            read_hex+= to_hex(data)
            if (len(read_hex) == jy_end):
              break
      port.close()


def write_jy_net_setting(ui):
  comName = ui.combox.currentText()
  arduino = QSerialPortInfo(comName)
  if (len(jyid4) == 0):
      return ''
  if arduino.isBusy():
    show_warning(ui)
  else:
    port = get_jy_port(comName)
    szWifi = ui.wifi.text() + ',' + ui.wifi_pass.text()
    szIP = ui.tcp_id.text()+',5555'
    wifi_len = hexFillZero(hex(len(szWifi)).replace('0x','')) 
    ip_len = hexFillZero(hex(len(szIP)).replace('0x',''))
    hex_wifi = ''
    hex_ip = ''
    for it in szWifi:
      hex_wifi += hexFillZero(hex(ord(it)).replace('0x','')) 
    for it in szIP:
      hex_ip += hexFillZero(hex(ord(it)).replace('0x',''))
    print(hex_wifi)
    print(hex_ip)
    if port.open(QIODevice.ReadWrite):  
      odra = '7E'+''.join(jyid4)+'1EA2'+wifi_len+ip_len+hex_wifi+hex_ip
      port.write(bytes.fromhex(odra)) 
      port.setReadBufferSize(jy_end)
      if port.waitForBytesWritten():
        read_hex = []
        while True:
          if port.waitForReadyRead():
            data = port.read(jy_end)
            read_hex+= to_hex(data)
            if (len(read_hex) == jy_end):
              break
        print(read_hex)
      port.close()

def upload_jys_data(ui):
  comName = ui.combox.currentText()
  arduino = QSerialPortInfo(comName)
  if (len(jyid4) == 0):
      return ''
  if arduino.isBusy():
    show_warning(ui)
  else:
    for i in range(0,256): 
      port = get_jy_port(comName)
      if port.open(QIODevice.ReadWrite):  
          num = hex(i).replace('0x','')
          inx = ''
          for l in range(0, 4-len(num)):
            inx += '0'
          print(inx+num)
          order = '7E05F5E0FF0481'+inx+num+'00'
          print(order)
          port.write(bytes.fromhex(order)) 
          port.setReadBufferSize(300)
          if port.waitForBytesWritten():
            read_hex = []
            nowlen = -1
            while True:
              if port.waitForReadyRead():
                data = port.read(300)
                read_hex+= to_hex(data)
                if (nowlen == -1 and len(read_hex) > 5):
                  nowlen = int(read_hex[5], 16) + 6
                if(len(read_hex) == nowlen):
                  break
            if int(''.join(read_hex[slice(69, 73)]),16) == 99999999:
              break
    for i in range(256,512): 
      port = get_jy_port(comName)
      if port.open(QIODevice.ReadWrite):  
          num = hex(i).replace('0x','')
          inx = ''
          for l in range(0, 4-len(num)):
            inx += '0'
          print(inx+num)
          order = '7E05F5E0FF0481'+inx+num+'00'
          print(order)
          port.write(bytes.fromhex(order)) 
          port.setReadBufferSize(300)
          if port.waitForBytesWritten():
            read_hex = []
            nowlen = -1
            while True:
              if port.waitForReadyRead():
                data = port.read(300)
                read_hex+= to_hex(data)
                if (nowlen == -1 and len(read_hex) > 5):
                  nowlen = int(read_hex[5], 16) + 6
                if(len(read_hex) == nowlen):
                  break
            if int(''.join(read_hex[slice(69, 73)]),16) == 99999999:
              break          
      port.close()

def to_hex(bytes_list):
  hex_list = []
  for it in bytes_list:
    h = hex(it).replace('0x','')
    if (len(h) == 1):
      h = '0' + h
    hex_list.append(h) 
  return hex_list

def hexFillZero(b):
  if len(b) != 1:
     return b
  return '0'+b



def show_warning(ui):
  QMessageBox.warning(QWidget,'标题','警告框消息正文',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
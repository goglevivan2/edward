from PyQt5 import QtWidgets,QtGui,QtCore
import app_design as design
import edward

class DecryptApp(QtWidgets.QMainWindow,design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_decrypt.pressed.connect(self.decrypt_file)
        self.pushButton_clear.pressed.connect(self.clear_system)

    def decrypt_file(self):
        result = edward.Encryptor(self.lineEdit_path.text())
        self.textBrowser_message.clear()
        self.textBrowser_message.append(result.return_decrypt_message())

    def clear_system(self):
        self.textBrowser_message.clear()
        self.lineEdit_path.clear()


app =QtWidgets.QApplication([])
window=DecryptApp()
window.setFixedSize(303, 347)
window.setWindowTitle("Decoder")
window.setWindowIcon(QtGui.QIcon('img\icon.ico'))
window.show()
app.exec_()
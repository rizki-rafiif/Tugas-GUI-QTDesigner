from PyQt5 import QtCore, QtGui, QtWidgets

## membuat kelas
class Ui_mainWindow(object):
    # fungsi untuk setting ui nya
    def setupUi(self, mainWindow):
        # membuat window nya
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(453, 598)     # ukuran windownya

        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.judul = QtWidgets.QLabel(self.centralwidget)
        self.judul.setGeometry(QtCore.QRect(110, 20, 241, 31))

        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.judul.setFont(font)
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.judul.setObjectName("judul")


        ### kolom lineEdit
        self.kolomNim = QtWidgets.QLineEdit(self.centralwidget)
        self.kolomNim.setGeometry(QtCore.QRect(120, 410, 271, 20))
        self.kolomNim.setObjectName("kolomNim")
        self.kolomNama = QtWidgets.QLineEdit(self.centralwidget)
        self.kolomNama.setGeometry(QtCore.QRect(120, 440, 271, 20))
        self.kolomNama.setObjectName("kolomNama")
        self.kolomJurusan = QtWidgets.QLineEdit(self.centralwidget)
        self.kolomJurusan.setGeometry(QtCore.QRect(120, 470, 271, 20))
        self.kolomJurusan.setObjectName("kolomJurusan")
        self.kolomNoTelpon = QtWidgets.QLineEdit(self.centralwidget)
        self.kolomNoTelpon.setGeometry(QtCore.QRect(120, 500, 271, 20))
        self.kolomNoTelpon.setObjectName("kolomNoTelpon")


        ### label
        self.labelNim = QtWidgets.QLabel(self.centralwidget)
        self.labelNim.setGeometry(QtCore.QRect(60, 410, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNim.setFont(font)
        self.labelNim.setObjectName("labelNim")
        self.labelNama = QtWidgets.QLabel(self.centralwidget)
        self.labelNama.setGeometry(QtCore.QRect(60, 440, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNama.setFont(font)
        self.labelNama.setObjectName("labelNama")
        self.labelJurusan = QtWidgets.QLabel(self.centralwidget)
        self.labelJurusan.setGeometry(QtCore.QRect(60, 470, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelJurusan.setFont(font)
        self.labelJurusan.setObjectName("labelJurusan")
        self.labelNoTelpon = QtWidgets.QLabel(self.centralwidget)
        self.labelNoTelpon.setGeometry(QtCore.QRect(60, 500, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelNoTelpon.setFont(font)
        self.labelNoTelpon.setObjectName("labelNoTelpon")



        ### button
        # code untuk button tambah
        self.buttonTambah = QtWidgets.QPushButton(self.centralwidget)
        self.buttonTambah.setGeometry(QtCore.QRect(120, 540, 61, 23))
        self.buttonTambah.setFont(font)
        self.buttonTambah.setObjectName("buttonTambah")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        # code untuk button edit
        self.buttonEdit = QtWidgets.QPushButton(self.centralwidget)
        self.buttonEdit.setGeometry(QtCore.QRect(190, 540, 61, 23))
        self.buttonEdit.setFont(font)
        self.buttonEdit.setObjectName("buttonEdit")
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)

        # code untuk button clear
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget)
        self.buttonClear.setGeometry(QtCore.QRect(260, 540, 61, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonClear.setFont(font)
        self.buttonClear.setObjectName("buttonClear")

        # code untuk button hapus
        self.buttonHapus = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHapus.setGeometry(QtCore.QRect(330, 540, 61, 23))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.buttonHapus.setFont(font)
        self.buttonHapus.setObjectName("buttonHapus")

        ### list widget
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(65, 81, 331, 281))
        self.listWidget.setObjectName("listWidget")


        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

        ######################
        ## untuk memberi menghubungkan dengan fungsi aksi pada button
        self.buttonTambah.clicked.connect(self.buttonTambahClick)
        self.buttonEdit.clicked.connect(self.buttonEditClick)
        self.buttonClear.clicked.connect(self.listWidget.clear)
        self.buttonHapus.clicked.connect(self.buttonHapusClick)

    ## untuk fungsi dari aksi button
    # fungsi untuk button tambah
    def buttonTambahClick(self):
        self.listWidget.addItem(
            self.kolomNim.text() + ' - ' +
            self.kolomNama.text() + ' - ' +
            self.kolomJurusan.text() + ' - ' +
            self.kolomNoTelpon.text()
        )
        # dibawah ini biar abis ditambahkan, line editnya kosong
        self.kolomNama.clear()
        self.kolomNim.clear()
        self.kolomJurusan.clear()
        self.kolomNoTelpon.clear()

    # fungsi untuk button edit
    def buttonEditClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)
        self.listWidget.addItem(
            self.kolomNim.text() + ' - ' +
            self.kolomNama.text() + ' - ' +
            self.kolomJurusan.text() + ' - ' +
            self.kolomNoTelpon.text()
        )
        # dibawah ini biar abis ditambahkan, line editnya kosong
        self.kolomNama.clear()
        self.kolomNim.clear()
        self.kolomJurusan.clear()
        self.kolomNoTelpon.clear()

    # fungsi untuk button hapus
    def buttonHapusClick(self):
        row = self.listWidget.currentRow()
        if row >= 0:
            self.listWidget.takeItem(row)


    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.judul.setText(_translate("mainWindow", "Data Mahasiswa"))
        self.buttonTambah.setText(_translate("mainWindow", "Tambah"))
        self.labelNim.setText(_translate("mainWindow", "Nim"))
        self.labelNama.setText(_translate("mainWindow", "Nama"))
        self.labelJurusan.setText(_translate("mainWindow", "Jurusan"))
        self.labelNoTelpon.setText(_translate("mainWindow", "No. Telp"))
        self.buttonEdit.setText(_translate("mainWindow", "Edit"))
        self.buttonClear.setText(_translate("mainWindow", "Clear"))
        self.buttonHapus.setText(_translate("mainWindow", "Hapus"))


## untuk menjalankan
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

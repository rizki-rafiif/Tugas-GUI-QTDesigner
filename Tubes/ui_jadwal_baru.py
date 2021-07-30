from PyQt5.QtSql import *
from ui_input_jadwal import *
from PyQt5 import QtCore, QtGui, QtWidgets


class JadwalBaru(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()
        self.setFixedSize(683, 384)
    def setupUi(self):
        self.setWindowTitle("Input atau Edit Jadwal")


        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 683, 384))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.judul = QtWidgets.QLabel(self.frame)
        self.judul.setGeometry(QtCore.QRect(150, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.judul.setFont(font)
        self.judul.setStyleSheet("background-color: rgb(33, 150, 243);border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.judul.setObjectName("judul")
        self.btnKembali = QtWidgets.QToolButton(self.frame)
        self.btnKembali.setGeometry(QtCore.QRect(470, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnKembali.setFont(font)
        self.btnKembali.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(74, 79, 74);")
        self.btnKembali.setObjectName("btnKembali")
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(90, 100, 511, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.btnTambah = QtWidgets.QToolButton(self.frame)
        self.btnTambah.setGeometry(QtCore.QRect(330, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnTambah.setFont(font)
        self.btnTambah.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 0);")
        self.btnTambah.setObjectName("btnTambah")

        self.judul.setText("JADWAL BARU")
        self.btnKembali.setText("Kembali")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("No.")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Judul")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Tanggal")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Jam")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Keterangan")
        self.btnTambah.setText("Tambah")


        self.btnTambah.clicked.connect(self.btnTambahClicked)
        self.btnKembali.clicked.connect(self.btnKembaliClicked)


    def btnKembaliClicked(self):
        self.close()

    def btnTambahClicked(self):
        self.form = InputJadwal()
        print(self.getRowCount())
        #self.form.mode = 0
        if self.form.exec_() == QDialog.Accepted:
            id = self.getRowCount() + 1
            query = QSqlQuery()

            # memasukkan data yang sudah diketikkan pada lineEdit ke dalam database
            query.exec_("INSERT INTO schedule (nomor, judul, tanggal, jam, keterangan) VALUES ('%d', '%s', '%s', '%s', '%s')" %
                        (id, self.form.inputJudul.text(), self.form.inputTanggal.text(), self.form.inputJam.text(),
                         self.form.inputKeterangan.text()))
            self.loadData()

    def loadData(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(self.getRowCount())
        query = QSqlQuery()
        Nomor, Judul, Tanggal, Jam, Keterangan = range(5)
        row = 0
        columnHeaders = ['Nomer', 'Judul', 'Tanggal', 'Jam', 'Keterangan']
        self.tableWidget.setHorizontalHeaderLabels(columnHeaders)
        query.exec_('SELECT * FROM schedule')

        # menampilkan data pada tabel
        while query.next():
            for i in range(5):
                item = QTableWidgetItem()
                item.setText(str(query.value(i)))
                self.tableWidget.setItem(row, i, item)
            row += 1

    def getRowCount(self):
        query = QSqlQuery()
        query.exec_('SELECT COUNT(*) FROM schedule')
        query.next()
        rowCount = query.value(0)
        return rowCount
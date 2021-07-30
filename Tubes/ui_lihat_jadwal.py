from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *


class LihatJadwal(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()
        self.setFixedSize(683, 384)
    def setupUi(self):
        self.setWindowTitle("Lihat jadwal")


        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(0, 0, 683, 384))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.judulLihatJadwal = QLabel(self.frame)
        self.judulLihatJadwal.setGeometry(QRect(150, 20, 381, 61))
        font = QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.judulLihatJadwal.setFont(font)
        self.judulLihatJadwal.setStyleSheet("background-color: rgb(33, 150, 243);border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.judulLihatJadwal.setAlignment(Qt.AlignCenter)
        self.judulLihatJadwal.setObjectName("judulLihatJadwal")
        self.btnKembali = QToolButton(self.frame)
        self.btnKembali.setGeometry(QRect(470, 320, 121, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnKembali.setFont(font)
        self.btnKembali.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(74, 79, 74);")
        self.btnKembali.setObjectName("btnKembali")
        self.tableWidget = QTableWidget(self.frame)
        self.tableWidget.setGeometry(QRect(90, 100, 511, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)

        self.judulLihatJadwal.setText("JADWAL")
        self.btnKembali.setText("Kembali")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("Nomor")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("Judul")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("Tanggal")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("Jam")
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText("Keterangan")

        self.btnKembali.clicked.connect(self.btnKembaliClicked)



    def btnKembaliClicked(self):
        self.close()

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


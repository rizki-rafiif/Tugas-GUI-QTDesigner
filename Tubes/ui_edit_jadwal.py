from PyQt5.QtSql import *
from ui_edit_input_jadwal import *
from PyQt5 import QtCore, QtGui, QtWidgets


class EditJadwal(QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.loadData()
        self.setFixedSize(683, 384)
    def setupUi(self):
        self.setWindowTitle("Mengedit Jadwal")


        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 683, 384))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.judulLihatJadwal = QtWidgets.QLabel(self.frame)
        self.judulLihatJadwal.setGeometry(QtCore.QRect(150, 20, 381, 61))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.judulLihatJadwal.setFont(font)
        self.judulLihatJadwal.setStyleSheet("background-color: rgb(33, 150, 243);border-radius:20px;\n"
"color: rgb(255, 255, 255);")
        self.judulLihatJadwal.setAlignment(QtCore.Qt.AlignCenter)
        self.judulLihatJadwal.setObjectName("judulLihatJadwal")
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
        self.btnEdit = QtWidgets.QToolButton(self.frame)
        self.btnEdit.setGeometry(QtCore.QRect(340, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnEdit.setFont(font)
        self.btnEdit.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(85, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.btnEdit.setObjectName("btnEdit")
        self.btnHapus = QtWidgets.QToolButton(self.frame)
        self.btnHapus.setGeometry(QtCore.QRect(210, 320, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.btnHapus.setFont(font)
        self.btnHapus.setStyleSheet("border-radius:20px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 0, 0);")
        self.btnHapus.setObjectName("btnBatal")

        self.judulLihatJadwal.setText("EDIT JADWAL")
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
        self.btnEdit.setText("Edit")
        self.btnHapus.setText("Hapus")

        self.btnHapus.clicked.connect(self.btnHapusClicked)
        self.btnEdit.clicked.connect(self.btnEditClicked)
        self.btnKembali.clicked.connect(self.btnKembaliClicked)

    def btnHapusClicked(self):
        id = int(self.tableWidget.item(self.tableWidget.currentRow(),0).text())
        query = QSqlQuery()
        query.exec_('DELETE FROM schedule WHERE nomor = %s' % id)
        self.loadData()

    def btnEditClicked(self):
        self.form = EditInputJadwal()

        self.form.inputJudul.setText(self.tableWidget.item(self.tableWidget.currentRow(), 1).text())
        self.form.inputTanggal.setText(self.tableWidget.item(self.tableWidget.currentRow(), 2).text())
        self.form.inputJam.setText(self.tableWidget.item(self.tableWidget.currentRow(), 3).text())
        self.form.inputKeterangan.setText(self.tableWidget.item(self.tableWidget.currentRow(), 4).text())
        # melakukan perubahan data seperti cara menambahkan data
        if self.form.exec_() == QDialog.Accepted:
            id = int(self.tableWidget.item(self.tableWidget.currentRow(),0).text())
            print(id)
            query = QSqlQuery()
            query.exec_('''UPDATE schedule SET judul = '%s', tanggal = '%s', jam = '%s', keterangan = '%s' WHERE nomor = '%d' ''' %
                        (self.form.inputJudul.text(), self.form.inputTanggal.text(), self.form.inputJam.text(), self.form.inputKeterangan.text(), id))

            self.loadData()

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

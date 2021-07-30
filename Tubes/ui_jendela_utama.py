import sys
from PyQt5.QtCore import QTimer, QTime, Qt
#from ui_jadwal_baru import *
from ui_lihat_jadwal import *
#from ui_edit_jadwal import *
from ui_jadwal_baru import *
from ui_edit_jadwal import *

# merupakan window utama
class MainForm(QWidget):
    clicked = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi()
        self.setFixedSize(1024, 640)        # ukuran fix
    def setupUi(self):
        self.setWindowTitle('Aplikasi SCE-Time')

        # membuat frame background utama
        self.frame = QFrame(self)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1024, 640))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("Frame Utama")

        # membuat frame background samping
        self.sideFrame = QtWidgets.QFrame(self)
        self.sideFrame.setEnabled(True)
        self.sideFrame.setGeometry(QtCore.QRect(0, 0, 180, 640))
        self.sideFrame.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sideFrame.setStyleSheet("background-color: rgb(255, 199, 0);")
        self.sideFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.sideFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.sideFrame.setObjectName("sideFrame")

        # layouting frame
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sideFrame)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(-1, 1, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 22, -1, 5)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")


        ## label-label
        # label
        self.judul = QLabel('SCE-Time')
        self.font = QtGui.QFont()
        self.font.setFamily("Century Gothic")
        self.font.setPointSize(24)
        self.font.setBold(True)
        self.font.setItalic(False)
        self.font.setWeight(70)
        self.judul.setFont(self.font)
        self.judul.setStyleSheet("color: #5F4E4E;")
        self.judul.setAlignment(QtCore.Qt.AlignCenter)
        self.judul.setObjectName("judul")
        self.verticalLayout_2.addWidget(self.judul)

        # garis batas
        self.garisBatas = QtWidgets.QFrame(self.sideFrame)
        self.garisBatas.setFrameShape(QtWidgets.QFrame.HLine)
        self.garisBatas.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.garisBatas.setObjectName("garisBatas")

        self.verticalLayout_2.addWidget(self.garisBatas)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(0, 8, -1, 0)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")


        # label button tambah
        self.btnTambah = myLabel()
        # import gambar pakai html
        self.btnTambah.setText('<img src="gambar_plus.png">')
        self.btnTambah.setObjectName("btnTambah")
        self.btnTambah.setAlignment(Qt.AlignCenter)
        self.verticalLayout_3.addWidget(self.btnTambah)

        # label judul button tambah
        self.judulJadwalBaru = myLabel("Jadwal Baru")
        self.fontJdwlBaru = QFont()
        self.fontJdwlBaru.setPointSize(15)
        self.judulJadwalBaru.setFont(self.fontJdwlBaru)
        self.judulJadwalBaru.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.judulJadwalBaru.setObjectName("judulJadwalBaru")

        self.verticalLayout_3.addWidget(self.judulJadwalBaru)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, 8, -1, -1)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")


        # label button lihat jadwal
        self.btnLihat = myLabel()
        # import gambar pakai html
        self.btnLihat.setText('<img src="gambar_view_details.png">')
        self.btnLihat.setAlignment(Qt.AlignCenter)
        self.btnLihat.setObjectName("btnLihat")
        self.verticalLayout_4.addWidget(self.btnLihat)

        # label judul lihat jadwal
        self.judulLihatJadwal = myLabel('Lihat Jadwal')
        self.judulLihatJadwal.setFont(self.fontJdwlBaru)
        self.judulLihatJadwal.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.judulLihatJadwal.setObjectName("judulLihatJadwal")

        self.verticalLayout_4.addWidget(self.judulLihatJadwal)
        self.verticalLayout.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(10, 15, 10, -1)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")


        # label button edit
        self.btnEdit = myLabel()
        # import gambar pakai html
        self.btnEdit.setText('<img src="gambar_edit.png">')
        self.btnEdit.setAlignment(Qt.AlignCenter)
        self.btnEdit.setObjectName("btnEdit")
        self.verticalLayout_5.addWidget(self.btnEdit)

        # label judul edit jadwal
        self.judulEditJadwal = myLabel('Edit Jadwal')
        self.judulEditJadwal.setFont(self.fontJdwlBaru)
        self.judulEditJadwal.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.judulEditJadwal.setObjectName("judulEditJadwal")
        self.verticalLayout_5.addWidget(self.judulEditJadwal)
        self.verticalLayout.addLayout(self.verticalLayout_5)


        # label untuk waktu
        self.waktu = QLabel(self)
        self.waktu.setGeometry(QtCore.QRect(450, 240, 291, 111))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.waktu.setFont(font)
        self.waktu.setStyleSheet("background-color: rgb(33, 150, 243);border-radius:40px;")
        self.waktu.setAlignment(QtCore.Qt.AlignCenter)
        self.waktu.setObjectName("waktu")


        # label untuk tanggal
        self.tanggal = QLabel(self)
        self.tanggal.setGeometry(QtCore.QRect(487, 355, 220, 50))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.tanggal.setFont(font)
        self.tanggal.setStyleSheet("background-color: rgb(33, 150, 243);border-radius:20px;")
        self.tanggal.setAlignment(QtCore.Qt.AlignCenter)
        self.tanggal.setObjectName("tanggal")

        # set timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)

        # set date
        self.date = QDate.currentDate()
        label_tanggal = self.date.toString(Qt.DefaultLocaleLongDate)
        self.tanggal.setText(label_tanggal)

        # label di klik
        self.btnTambah.clicked.connect(self.btnTambahClicked)
        self.judulJadwalBaru.clicked.connect(self.btnTambahClicked)
        self.btnEdit.clicked.connect(self.btnEditClicked)
        self.judulEditJadwal.clicked.connect(self.btnEditClicked)
        self.btnLihat.clicked.connect(self.btnLihatJadwalClicked)
        self.judulLihatJadwal.clicked.connect(self.btnLihatJadwalClicked)


    # buka dialog jadwal baru
    def btnTambahClicked (self):
        self.form = JadwalBaru()
        self.form.show()

    # buka dialog edit jadwal
    def btnEditClicked (self):
        self.form = EditJadwal()
        self.form.show()

    # buka dialog lihat jadwal
    def btnLihatJadwalClicked (self):
        self.form = LihatJadwal()
        self.form.show()

    # fungsi untuk waktu nya biar jalan terus
    def showTime(self):
        self.current_time = QTime.currentTime()
        label_time = self.current_time.toString("hh:mm:ss")
        self.waktu.setText(label_time)

# kelas untuk membuat label dapat di klik
class myLabel(QLabel):
    clicked = pyqtSignal()
    def mouseReleaseEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.clicked.emit()

if __name__ == '__main__':
    a = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('db_schedule')
    if not db.open():
        print('ERROR: ' + db.lastError().text())
        sys.exit(1)
    form = MainForm()
    form.show()
    a.exec_()
from PyQt5.QtWidgets import *

app = QApplication([])

button = QPushButton('Click')
## menambahkan ukuran tombol agar lebih besar
button.resize(300, 200)

def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec_()


button.clicked.connect(on_button_clicked)
button.show()
app.exec_()
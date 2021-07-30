from PyQt5.QtSql import *
# contoh cara membuat database menggunakan python
def connectdb():
    # menerapkan library QtSql dari PyQt5
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('db_schedule')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()

        # membuat tabel
        sql = '''CREATE TABLE schedule (
	    nomor integer not null primary key,
	    judul varchar(50),
	    tanggal varchar(15),
	    jam varchar(15),
	    keterangan varchar(255)
        )'''

        query.exec_(sql)

        # jika berhasil maka akan menampilkan output berhasil
        if (query.exec_):
            print('Berhasil membuat tabel')
    else:
        print('ERROR: ' + db.lastError().text())
connectdb()
# PENGUMPULAN TUGAS BESAR
# Kelompok : 3R
# Anggota :
 1. Rizki Rafiif Amaanullah (19104010)
 2. Novian Dwi Romadon (19104011)
 3. Gracia Rizka Pasfica (19104064)


# 1. Studi Kasus
     Pengguna membutuhkan sistem yang berisi jadwal yang diinputkan oleh pengguna, 
     sehingga pengguna tidak menulisnya secara manual tetapi cukup dengan mengetikkan judul, tanggal, dan jam. 
     Supaya pengguna dapat melihat apakah waktu tersebut sesuai dengan jadwal maka akan ditampilkan waktu yang 
     sedang berlangsung (waktu sekarang).

# 2. Aplikasi 
     Aplikasi yang dibuat bernama "Sce-Time". Aplikasi ini terhubung dengan database sehingga pengguna
     yang menambahkan jadwal baru atau mengedit jadwal lama, seluruh historynya akan tersimpan di dalam
     database
     
# 3. Use Case Diagram

![use_case](https://user-images.githubusercontent.com/58683476/127586995-ad024357-9e25-45cd-b292-b7b32a8891d4.jpg)

# 4. Database

![database](https://user-images.githubusercontent.com/58683476/127587070-edd68eb7-7c28-42db-b8c8-6c778deaf52b.jpg)

# 5. Cara Penggunaan
   1. Buka file ui_jendela_utama.py pada github yang terletak di file Program apabila dijalankan maka muncul tampilan berikut :
        ![1](https://user-images.githubusercontent.com/58683476/127589473-0e032ba8-c0b1-4520-801b-eae13f3941a6.jpg)

      Pada tampilan awal akan terdapat waktu yang sedang berlangsung saat ini dan terdapat beberapa menu seperti jadwal baru, lihat jadwal, dan edit jadwal.
      
   2. Klik menu “Jadwal Baru” untuk menambahkan jadwal. Berikut tampilannya:
        ![2](https://user-images.githubusercontent.com/58683476/127589599-6a7069ab-db5f-431a-98d6-0707735f8c21.jpg)

        Klik button "Tambah" untuk menampilkan form tambah jadwal
        
        ![image](https://user-images.githubusercontent.com/62453385/127587797-1c8dee31-42c9-4876-85ff-7c460a090704.png)
        
        Kemudian isi form tersebut lalu klik "Simpan"
        
        ![image](https://user-images.githubusercontent.com/62453385/127587895-950be678-0e0d-4c4d-a8c4-64dc3851b0df.png)
        
        Jadwal akan otomatis tersimpan ke dalam database.
        
   3. Klik menu "Lihat Jadwal" apabila ingin melihat isi keseluruhan dari jadwal yang sudah diinputkan
        ![image](https://user-images.githubusercontent.com/62453385/127587990-e76ae203-c71d-44bc-80f9-c3af5e7e618b.png)
   
   4. Klik menu "Edit Jadwal" jika ingin mengubah isi jadwal
   
        ![image](https://user-images.githubusercontent.com/62453385/127588049-f88aab34-e998-4a03-9ee2-aef460ed2cc7.png)
        
        Pilih jadwal yang akan di ubah.
        
        ![image](https://user-images.githubusercontent.com/62453385/127588120-b2be61e5-cc2b-4b06-b49b-3a8639ee9cf0.png)
        
        Pilih apakah jadwal tersebut ingin diubah atau dihapus. Apabila diubah maka klik "Edit" dan Isikan form sesuai data yang ingin diubah, jika sudah lalu klik "SIMPAN"
        
        ![image](https://user-images.githubusercontent.com/62453385/127588229-5ae3727c-4539-4fd6-8abc-1845af69f6c0.png)
        
        Apabila ingin menghapus data maka klik "HAPUS" pada jadwal yang dipilih
        
   5. Untuk melihat apakah berhasil atau tidak dalam menginputkan data, dapat dilihat pada menu "Lihat Jadwal" atau database "db_schedule" 

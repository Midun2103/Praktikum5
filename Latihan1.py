print("===================================================================")
print("Nama         :   Midun Hakiki")
print("NIM          :   312210583")
print("Kelas        :   TI.22.B1")
print("Mata Kuliah  :   Bahasa Pemrograman")
print("===================================================================")

# Buat dictionary daftar kontak
print("Buat dictionary nama sebagai key, dan nomor sebagai value")

isi = {'Midun': '081267888', 'Kiki': '087677776'}
print("Nama | Nomor kontak")
print(isi)

print("Tampilkan Kontaknya Midun")
print(isi['Midun'])

print("Tambah kontak baru dengan nama Iki, nomor 087654544")
isi['Iki']= '087654544'
print(isi)

print("Ubah kontak Kiki dengan nomor baru 088999776")
isi['Kiki']= '088999777'
print(isi)

print("Tampilkan semua Nama")
print(isi.keys())

print("Tampilkan semua Nomor")
print(isi.values())

print("Tampilkan daftar Nama dan nomornya")
print(isi.items())

print("Hapus kontak Kiki")
del isi['Kiki']
print(isi)

print("===================================================================")
# CapstoneProject
# Modul 1
# Perpustakaan
# Muhammad Mahardika Renaldi

from tabulate import tabulate
import uuid
import datetime

keranjang_buku = []

buku = [
    {"id": "B01A1", "judul": "Pemrograman Python", "pengarang": "Guido van Rossum", "kategori": "Komputer", "total_buku": 10, "tersedia": 5, "harga": 100000},
    {"id": "B02B2", "judul": "Algoritma dan Struktur Data", "pengarang": "Cormen", "kategori": "Komputer", "total_buku": 8, "tersedia": 3, "harga": 120000},
    {"id": "B01O1", "judul": "One Piece Chapter 1", "pengarang": "Echiro Oda", "kategori": "Komik", "total_buku": 100, "tersedia": 3, "harga": 75000},
    {"id": "B01O2", "judul": "One Piece Chapter 2", "pengarang": "Echiro Oda", "kategori": "Komik", "total_buku": 100, "tersedia": 9, "harga": 75000},
    {"id": "B01O3", "judul": "One Piece Chapter 3", "pengarang": "Echiro Oda", "kategori": "Komik", "total_buku": 100, "tersedia": 1, "harga": 75000},
    {"id": "B01O4", "judul": "One Piece Chapter 4", "pengarang": "Echiro Oda", "kategori": "Komik", "total_buku": 100, "tersedia": 2, "harga": 75000},
    {"id": "B01N1", "judul": "Supernova", "pengarang": "Dee", "kategori": "Novel", "total_buku": 6, "tersedia": 2, "harga": 100000},
    {"id": "B01N2", "judul": "Saman", "pengarang": "Ayu Utami", "kategori": "Novel", "total_buku": 6, "tersedia": 2, "harga": 100000},
    {"id": "B01N3", "judul": "Larung", "pengarang": "Ayu Utami", "kategori": "Novel", "total_buku": 6, "tersedia": 5, "harga": 100000},
    {"id": "B01N4", "judul": "Bilangan Fu", "pengarang": "Ayu Utami", "kategori": "Novel", "total_buku": 6, "tersedia": 0, "harga": 100000},

]

peminjam = [
    {"id_peminjam": "P001", "nama": "Mahardika", "umur": 29, 'alamat': "GPS lt. 25", "buku_dipinjam": [{"id_buku": "B01A1", "tanggal_pinjam": "2024-09-07", "tanggal_kembali": "2024-09-14"}]},
    {"id_peminjam": "P002", "nama": "Dika", "umur": 29, 'alamat': "GPS lt. 4", "buku_dipinjam": [{"id_buku": "B01A1", "tanggal_pinjam": "2024-09-07", "tanggal_kembali": "2024-09-14"}]},
]


def generate_id_buku(judul, pengarang):
    return f"B{judul[0]}{pengarang[0]}{str(uuid.uuid4())[:4]}"

def generate_id_peminjam(nama):
    return f"P{nama[0]}{str(uuid.uuid4())[:4]}"

def daftar_member():
    while True:
        nama = input("Masukkan nama (hanya huruf dan spasi): ").strip()
        valid = True
        huruf_count = 0

        for char in nama:
            if char.isalpha():
                huruf_count += 1

        if huruf_count >= 2 and valid:
            break
        else:
            print("Nama harus minimal 2 karakter huruf dan hanya boleh berisi huruf dan spasi.")

    while True:
        try:
            umur = int(input("Masukkan umur (bilangan bulat): ").strip())
            if umur > 0:
                break
            else:
                print("Umur harus bilangan bulat positif.")
        except ValueError:
            print("Umur harus berupa bilangan bulat.")

    alamat = input("Masukkan alamat: ").strip()
    id_peminjam = generate_id_peminjam(nama)
    peminjam.append({'id_peminjam': id_peminjam, 'nama': nama, 'umur': umur, 'alamat': alamat, 'buku_dipinjam': []})
    print(f"\nAnda berhasil terdaftar sebagai member dengan ID: {id_peminjam}")
    tampilkan_data_diri(id_peminjam)

def tampilkan_daftar_buku(buku_list):
    headers = ["ID Buku", "Judul", "Pengarang", "Kategori", "Total Buku", "Tersedia"]
    data = [[buku['id'], buku['judul'], buku['pengarang'], buku['kategori'], buku['total_buku'], buku['tersedia']] for buku in buku_list]
    
    print(tabulate(data, headers=headers, tablefmt='grid'))

def tampilkan_buku_dipinjam(id_peminjam):
    table=[]
    peminjam_ditemukan = True

    for peminjam_data in peminjam:
        if peminjam_data['id_peminjam'] == id_peminjam:
            if peminjam_data['buku_dipinjam']:
                buku_dipinjam_count = {}
                for b in peminjam_data['buku_dipinjam']:
                    baris_key = (b['id_buku'],b['tanggal_pinjam'], b['tanggal_kembali'])
                    if baris_key in buku_dipinjam_count:
                        buku_dipinjam_count[baris_key] += 1
                    else:
                        buku_dipinjam_count[baris_key] = 1

                for baris_key, jumlah in buku_dipinjam_count.items():
                    id_buku, tanggal_pinjam, tanggal_kembali = baris_key
                    for list_buku in buku:
                        if list_buku['id'] == id_buku:
                            table.append({'id_buku':id_buku, 'jumlah': jumlah, 'judul': list_buku['judul'], 'pengarang': list_buku['pengarang'], 'kategori': list_buku['kategori'], 'tanggal_pinjam': tanggal_pinjam, 'tanggal_kembali': tanggal_kembali})

    if not peminjam_ditemukan:
        print(f"Peminjam dengan ID {id_peminjam} tidak ditemukan.")
    elif not table:
        print(f"Peminjam dengan ID {id_peminjam} tidak memiliki buku yang dipinjam.")
    else:
        headers = ["ID Buku", "Judul", "Pengarang", "Kategori", 'Jumlah', 'Tanggal Peminjaman', 'Tanggal Pengembalian']
        data = [[t['id_buku'], t['judul'], t['pengarang'], t['kategori'], t['jumlah'], t['tanggal_kembali'], t['tanggal_kembali']] for t in table]
        print(tabulate(data, headers=headers, tablefmt='grid'))

def cari_buku():
    while True:
        keyword = input("Masukkan kata kunci pencarian: ").strip()
        keyword_lower = keyword.lower()

        hasil_pencarian = [
            buku for buku in buku if
            keyword_lower in buku['judul'].lower().split() or
            keyword_lower in buku['pengarang'].lower().split() or
            keyword_lower in buku['kategori'].lower().split()
        ]

        if hasil_pencarian:
            tampilkan_daftar_buku(hasil_pencarian)
        else:
            print("Buku tidak ditemukan.")

        while True:
            cari_lagi = input("Apakah Anda ingin mencari buku lain? (y/n): ").strip().lower()
            if cari_lagi in ['y', 'n']:
                break
            else:
                print("Pilihan tidak valid. Silakan pilih y atau n.")

        if cari_lagi == 'n':
            break

def pinjam_buku(id_pengunjung, id_buku, list_buku, list_peminjam):
    pengunjung = None
    for p in list_peminjam:
        if p['id_peminjam'] == id_pengunjung:
            pengunjung = p
            break
    if pengunjung:
        buku = None
        for b in list_buku:
            if b['id'] == id_buku:
                buku = b
                break
        if buku:
            if buku['tersedia'] > 0:
                keranjang_buku.append({'id_buku': id_buku, 'judul': buku['judul']})
                buku['tersedia'] -= 1
                # print(type(keranjang_buku))
                print(f"Buku '{buku['judul']}' berhasil ditambahkan ke keranjang.")
                while True:
                    pinjam_lagi = input("Apakah Anda ingin meminjam buku lain? (y/n): ").strip()
                    if pinjam_lagi.lower() == 'y':
                        id_buku_baru = input("Masukkan ID buku yang ingin dipinjam: ").strip()
                        pinjam_buku(id_pengunjung, id_buku_baru, list_buku, list_peminjam)
                        break
                    elif pinjam_lagi.lower() == 'n':
                        break
                    else:
                        print("Pilihan tidak valid. Silakan pilih y atau n.")
            else:
                print("Maaf, stok buku tidak mencukupi.")
        else:
            print("Buku yang Anda cari tidak ditemukan. Silakan cari buku lain.")
    else:
        print("ID pengunjung tidak ditemukan.")

def kelola_keranjang(keranjang_buku, id_peminjam):
    while True:
        if not keranjang_buku:
            print("Keranjang Anda masih kosong.")
            break
        print("\nKeranjang Buku:")
        for i, list_buku in enumerate(keranjang_buku, start=1):
            print(f"{i}. {list_buku['judul']} (ID: {list_buku['id_buku']})")
        print("\nApa yang ingin Anda lakukan?")
        print("1. Hapus buku dari keranjang")
        print("2. Konfirmasi peminjaman")
        print("3. Kembali ke menu utama")
        pilihan = input("Masukkan pilihan Anda: ")
        if pilihan == '1':
            hapus_buku(keranjang_buku, buku)
        elif pilihan == '2':
            konfirmasi_peminjaman(keranjang_buku, peminjam, id_peminjam)
            break
        elif pilihan == '3':
            break
        else:
            print("Pilihan tidak valid.")

def konfirmasi_peminjaman(keranjang_buku, list_peminjam, id_pengunjung):
    print("\nKeranjang Buku:")
    for i, buku in enumerate(keranjang_buku, start=1):
        print(f"{i}. {buku['judul']} (ID: {buku['id_buku']})")
    while True:
        konfirmasi = input("Apakah Anda yakin ingin meminjam buku-buku di atas? (y/n): ")
        if konfirmasi.lower() == 'y':
            tanggal_sekarang = datetime.datetime.now().date()
            tanggal_kembali = tanggal_sekarang + datetime.timedelta(days=7)
            for buku in keranjang_buku:
                for pengunjung in list_peminjam:
                    if pengunjung['id_peminjam'] == id_pengunjung:
                        pengunjung['buku_dipinjam'].append({'id_buku': buku['id_buku'], 
                                                           'tanggal_pinjam': tanggal_sekarang.strftime('%Y-%m-%d'),
                                                           'tanggal_kembali': tanggal_kembali.strftime('%Y-%m-%d')})
                        break

            for buku_dipinjam in pengunjung['buku_dipinjam']:
                for i, buku in enumerate(keranjang_buku):
                    if buku['id_buku'] == buku_dipinjam['id_buku']:
                        keranjang_buku.pop(i)
                        break
            print("Buku berhasil dipinjam.")
            break
        elif konfirmasi == 'n':
            print("Peminjaman dibatalkan.")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih y atau n.")

def hapus_buku(keranjang_buku, list_buku):
    percobaan = 0
    while percobaan < 3:
        if not keranjang_buku:
            print("Keranjang Anda masih kosong.")
            break

        try:
            index = int(input("Masukkan nomor buku yang ingin dihapus: "))
            if 1 <= index <= len(keranjang_buku):
                id_buku_dihapus = keranjang_buku[index - 1]['id_buku']
                keranjang_buku.pop(index - 1)
                for buku in list_buku:
                    if buku['id'] == id_buku_dihapus:
                        buku['tersedia'] += 1
                        break
                print("Buku berhasil dihapus dari keranjang.")
                break
            else:
                print("Nomor buku tidak valid.")
        except ValueError:
            print("Masukkan harus berupa angka.")

        percobaan += 1
        if percobaan == 3:
            print("Anda telah mencoba 3 kali. Penghapusan buku dibatalkan.")

def tampilkan_data_diri(id_pengunjung):
    for pengunjung in peminjam:
        if pengunjung['id_peminjam'] == id_pengunjung:
            jumlah_buku = len(pengunjung['buku_dipinjam'])
            data = [
                [pengunjung['id_peminjam'], pengunjung['nama'], pengunjung['umur'], pengunjung['alamat'], jumlah_buku]
            ]
            headers = ["ID Pengunjung", "Nama", "Umur", "Alamat", "Jumlah Buku yang Dipinjam"]
            print(tabulate(data, headers=headers, tablefmt="grid"))
            return
    print("Peminjam tidak ditemukan.")

def update_data_diri(id_pengunjung):
    for pengunjung in peminjam:
        if pengunjung['id_peminjam'] == id_pengunjung:
            while True:
                print("\nData Diri Anda:")
                tampilkan_data_diri(id_pengunjung)
                print("\nApa yang ingin Anda ubah?")
                print("1. Nama")
                print("2. Umur")
                print("3. Alamat")
                print("4. Kembali ke menu utama")
                pilihan = input("Masukkan pilihan Anda: ").strip()
                if pilihan == '1':
                    while True:
                        nama_baru = input("Masukkan nama (hanya huruf dan spasi): ").strip()
                        valid = True
                        huruf_count = 0
                        for char in nama_baru:
                            if char.isalpha():
                                huruf_count += 1
                        if huruf_count >= 2 and valid:
                            break
                        else:
                            print("Nama harus minimal 2 karakter huruf dan hanya boleh berisi huruf dan spasi.")
                    pengunjung['nama'] = nama_baru
                elif pilihan == '2':
                    while True:
                        try:
                            umur_baru = int(input("Masukkan umur (bilangan bulat): ").strip())
                            if umur_baru > 0:
                                break
                            else:
                                print("Umur harus bilangan bulat positif.")
                        except ValueError:
                            print("Umur harus berupa bilangan bulat.")
                    pengunjung['umur'] = umur_baru
                elif pilihan == '3':
                    alamat_baru = input("Masukkan alamat baru: ").strip()
                    pengunjung['alamat'] = alamat_baru
                elif pilihan == '4':
                    break
                else:
                    print("Pilihan tidak valid.")
            print("Data diri Anda berhasil diperbarui.")
            return
    print('ID yang Anda masukkan salah atau tidak terdapat di list member.')

def menu_utama_member():
    while True:
        print("\nMenu Utama:")
        print("1. Melihat seluruh buku")
        print("2. Mencari buku tertentu")
        print("3. Menambahkan buku ke dalam keranjang")
        print("4. Kelola keranjang dan Konfirmasi pinjaman")
        print("5. Menampilkan list buku yang sedang dipinjam")
        print("6. Update data diri")
        print("7. Keluar")
        pilihan = input("\n\nPilih menu: ").strip()
        if pilihan == '1':
            tampilkan_daftar_buku(buku)
        elif pilihan == '2':
            cari_buku()
        elif pilihan == '3':
            id_pengunjung = input("Masukkan ID Anda: ").strip()
            id_buku = input("Masukkan ID buku yang ingin dipinjam: ").strip()
            pinjam_buku(id_pengunjung, id_buku, buku, peminjam)
        elif pilihan == '4':
            id_pengunjung = input("Masukkan ID Anda: ").strip()
            kelola_keranjang(keranjang_buku, id_pengunjung)
        elif pilihan == '5':
            id_pengunjung = input("Masukkan ID Anda: ").strip()
            tampilkan_buku_dipinjam(id_pengunjung)
        elif pilihan == '6':
            id_pengunjung = input("Masukkan ID Anda: ").strip()
            update_data_diri(id_pengunjung)
        elif pilihan == '7':
            print('Terima kasih telah mengunjungi Perpustakaan Digital. Sampai jumpa kembali.\n\n')
            break
        else:
            print("Pilihan tidak valid.")

def login_member():
    for percobaan in range(3):
        id_pengunjung = input("Masukkan ID pengunjung: ").strip()
        for p in peminjam:
            if p['id_peminjam'] == id_pengunjung:
                print("Selamat datang, Anda sedang mengunjungi Perpustakaan Digital!")
                menu_utama_member()
                return 
        if percobaan < 2:
            print(f"ID pengunjung tidak ditemukan. Anda memiliki {2 - percobaan} percobaan lagi.")
            daftar = input("Apakah Anda ingin mendaftar? (y/n): ").strip().lower()
            while daftar not in ['y', 'n']:
                print("Pilihan tidak valid. Silakan pilih y atau n.")
                daftar = input("Apakah Anda ingin mendaftar? (y/n): ").strip().lower()

            if daftar == 'y':
                daftar_member()
                menu_utama_member()
                return
            else:
                print("Pendaftaran dibatalkan.")
    print("\n\nID pengunjung tidak ditemukan. Percobaan login gagal. \nAnda telah melakukan 3 kali percobaan. Harap menunggu beberapa saat lagi. \nProgram selesai.")


def mulai_program():
    print("\nSelamat datang di Perpustakaan Digital!\n")
    pilihan = input("\nApakah Anda sudah menjadi anggota? (y/n): ").lower()

    if pilihan == 'y':
        login_member()
    elif pilihan == 'n':
        print('Anda dapat mendaftar dengan mengisi data diri terlebih dahulu:')
        daftar_member()
        login_member()
    else:
        print("Pilihan tidak valid. Silakan pilih 'ya' atau 'tidak'.")

mulai_program()
def display_kontak(daftar_kontak):
    for kontak in daftar_kontak:
        print("=====================================")
        print(f"Nama : {kontak['nama']}")
        print(f"Email : {kontak['email']}")
        print(f"Telepon : {kontak['telepon']}")
        print("=====================================")

def new_kontak():
    nama=input("Nama : ")
    email=input("Email : ")
    telepon=input("telepon : ")
    kontak ={
        "nama" : nama,
        "email" : email,
        "telepon" : telepon
    }
    return kontak

def hapus_kontak(daftar_kontak):
    telepon = input("Masukan nama yang akan di hapus :")

    index=-1

    for i in range(0, len(daftar_kontak)):
        kontak=daftar_kontak[i]
        if telepon == kontak["nama"]:
            index=i
            break
    if index == -1:
        print("Data tidak di temukan")
    else:
         del daftar_kontak[index]
         print("Data Berhasil Di hapus")
   
def   cari_kontak(daftar_kontak):
    nama_dicari = input("Masukan nama yang di cari :")

    for kontak in daftar_kontak:
        nama = kontak["nama"]
        if nama.lower().find(nama_dicari.lower()) != -1:
             print("=====================================")
             print(f"Nama : {kontak['nama']}")
             print(f"Email : {kontak['email']}")
             print(f"Telepon : {kontak['telepon']}")
             print("=====================================")



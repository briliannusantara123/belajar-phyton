def display_makanan(menu_makanan):
    for makanan in menu_makanan:
        print("_______________________________")
        print(f"Nama makanan  : {makanan['nama']}")
        print(f"Harga makanan : {makanan['harga']}")
def new_makanan():
    nama = input("Masukan Nama Makanan : ")
    harga = input("Masukan Harga : ")
    makanan ={
        "nama" : nama,
        "harga" : harga
    }
    return makanan

def hapus_makanan(menu_makanan):
    harga = input("Masukan Nama makanan yang akan di hapus : ")
    index = -1

    for i in range(0, len(menu_makanan)):
        makanan=menu_makanan[i]
        if harga == makanan["nama"]:
            index=i
            break
    if index == -1:
        print("Makanan Tidak di Temukan.")
    else:
        del menu_makanan[index]
        print("Menu Makanan Berhasil di Hapus")

def cari_makanan(menu_makanan):
    nama_dicari = input("Masukan Nama Makanan : ")
    for makanan in menu_makanan:
        nama = makanan["nama"]
        if nama.lower().find(nama_dicari.lower()) != -1:
            print("      Ayam Bakar Ginessa!!     ")
            print("_______________________________")
            print(f"Nama makanan  : {makanan['nama']}")
            print(f"Harga makanan : {makanan['harga']}")
            print("_______________________________")
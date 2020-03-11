import pesan

menu_makanan=[]

while True:
    print("     Ayam Bakar Ginessa     ")
    print("============================")
    print(" 1. Menu Makanan ABG        ")
    print(" 2. Tambah Makanan          ")
    print(" 3. Cari Makanan            ")
    print(" 4. Hapus Menu Makanan      ")
    print(" 0. Keluar dari Aplikasi    ")
    print("============================")
    menu = input("Masukan Menu [1-4] : ")
    if menu == "0":
        break
    elif menu == "1":
        pesan.display_makanan(menu_makanan)
    elif menu == "2":
        makanan = pesan.new_makanan()
        menu_makanan.append(makanan)
    elif menu == "3":
        pesan.cari_makanan(menu_makanan)
    elif menu == "4":
        pesan.hapus_makanan(menu_makanan)
    else:
        print("Menu Tidak tersedia")

print("Keluar Dari aplikasi")
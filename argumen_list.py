def jumlahkan(*List_angka):
    total=0
    for angka in List_angka:
        total = total + angka
    print(f"Total {List_angka} = {total}")

jumlahkan(10,10,10)
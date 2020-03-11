banyak = int(input("Berapa data yang akan di input? "))

nama=[]
umur=[]
hobi=[]
alamat=[]

for i in range(0, banyak):
    print(f"data ke {i}")
    input_nama=input("Nama : ")
    input_umur=int(input("Umur : "))
    input_hobi = input("hobi : ")
    input_alamat = input("alamat : ")

    nama.append(input_nama)
    umur.append(input_umur)
    hobi.append(input_hobi)
    alamat.append(input_alamat)

for i in range(0, banyak):
    data_nama=nama[i]
    data_umur=umur[i]
    data_hobi=hobi[i]
    data_alamat=alamat[i]
    print(f"{data_nama} Berumur {data_umur} Tahun,{data_nama} Memiliki Hobi {data_hobi} dan Dia Tinggal Di {data_alamat}")

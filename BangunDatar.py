
# ini adalah array 
bangunDatar = ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga"]

#fungsi yang kita terapkan menjadi rumus untuk melakukkan perhitungan
def persegi():
    sisi = float(input("Masukkan sisi: "))
    keliling = 4 * sisi
    luas = sisi * sisi
    return keliling, luas

def persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    keliling = 2 * (panjang + lebar)
    luas = panjang * lebar
    return keliling, luas

def lingkaran():
    r = float(input("Masukkan jari-jari: "))
    pi = 3.14
    keliling = 2 * pi * r
    luas = pi * r * r
    return keliling, luas

def segitiga():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    sisi_a = float(input("Masukkan sisi A: "))
    sisi_b = float(input("Masukkan sisi B: "))
    keliling = alas + sisi_a + sisi_b
    luas = 0.5 * alas * tinggi
    return keliling, luas

nama = input("Masukkan nama : ")

# menerapkan loop dengan while
while True:  
    print("\nDaftar Bangun Datar:")
    for i in range(len(bangun_datar)):
        print(f"{i+1}. {bangun_datar[i]}")

    pilihan = int(input("Pilih bangun datar (1-4): "))

    #percabangan 
    if pilihan == 1:
        keliling, luas = persegi()
        nama_bangun = bangun_datar[0]

    elif pilihan == 2:
        keliling, luas = persegi_panjang()
        nama_bangun = bangun_datar[1]

    elif pilihan == 3:
        keliling, luas = lingkaran()
        nama_bangun = bangun_datar[2]

    elif pilihan == 4:
        keliling, luas = segitiga()
        nama_bangun = bangun_datar[3]

    else:
        print("Tidak")
        print("Terima kasih")
        break

    # hasil perhitungan
    print("\n=== HASIL PERHITUNGAN ===")
    print("Nama          :", nama)
    print("Bangun Datar  :", nama_bangun)
    print("Keliling      :", keliling)
    print("Luas          :", luas)

    # mengulang kemabali 
    ulang = input("\nHitung lagi? (y/n): ").lower()
    if ulang != "y":
        print("Terima kasih 🙏")
        break

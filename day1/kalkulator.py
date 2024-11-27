# Muhammad Daffa Rahman
# AERO
# L0124062

# dictionary untuk operator
operator = {
    "tambah":"+",
    "kurang":"-",
    "kali": "*",
    "bagi": "/",
    "bagi floor": "//",
    "pangkat": "**",
    "modulo":"%"
}

# disini kita mengambil keys yang ada di dictionary operator dan mengubahnya ke list
menu = list(operator.keys())

# program akan berjalan selama running = True
running = True
while running:
    # judul program
    print("------------------------")
    print("KalkuDap")
    print("------------------------")

    # menampilkan menu
    for i in range(len(menu)):
        print(str(i + 1) + " -> " + menu[i] + " (" + operator[menu[i]] + ")")

    print("------------------------")

    # meminta user untuk memilih operator apa yang akan digunakan
    pilihan = int(input("pilih nomor berapa? "))

    # pilihan angka menu user harus tidak diluar dari yang ada di menu
    if pilihan >= 1 and pilihan <= len(menu):
        # user memasukkan dua angka yang ingin dihitung
        a = int(input("\nmasukkan nilai a = "))
        b = int(input("masukkan nilai b = "))

        # menghitung hasil berdasarkan masukan user
        hasil = 0
        if pilihan == 1:
            hasil = a + b
        elif pilihan == 2:
            hasil = a - b
        elif pilihan == 3:
            hasil = a * b
        elif pilihan == 4:
            hasil = a / b
        elif pilihan == 5:
            hasil = a // b
        elif pilihan == 6:
            hasil = a**b
        elif pilihan == 7:
            hasil = a % b

        # menampilkan hasil
        print("\nHasil dari a", operator[menu[pilihan - 1]], "b =", hasil)

    # eksekusi ini apabila pilihan user tidak valid
    else:
        print("\nTidak ada pilihan itu")

    # user dapat melakukan perhitungan lagi atau keluar dari program
    lanjut = input("\nlagi? (y/n) ")
    # apabila user tidak memilih untuk lanjut, running = False dan while loop berhenti
    if lanjut != "y":
        running = False

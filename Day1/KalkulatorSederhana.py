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

    pilihan = int(input("pilih nomor berapa? "))
    if pilihan >= 1 and pilihan <= len(menu):
        a = int(input("\nmasukkan nilai a = "))
        b = int(input("masukkan nilai b = "))
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

        print("\nHasil dari a", operator[menu[pilihan - 1]], "b =", hasil)

    else:
        print("\nTidak ada pilihan itu")
    
    lanjut = input("\nlagi? (y/n) ")
    if lanjut != "y":
        running = False

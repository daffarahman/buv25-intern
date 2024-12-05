# Tugas 1 Intern Bengawan UV Aero
# Nama    : Muhammad Daffa Rahman
# NIM     : L0124062
# Prodi   : Informatika
# Program : Digital Vending Machine Sederhana

import os

def clearScreen():
    os.system("cls")
    
# list menu dan dictionary menyimpan nama, harga, dan stok
menu = [    
    {"nama":"Le Minerale", "harga": 3000, "stok":100},
    {"nama":"Ultra Milk Full Cream", "harga": 8000, "stok":20},
    {"nama":"Teh Kotak", "harga": 6000, "stok":40},
    {"nama":"Larutan Penyegar", "harga": 9000, "stok":10},
    {"nama":"Coca-cola", "harga": 5000, "stok":30},
    {"nama":"Oat Milk", "harga": 6500, "stok":15},
    {"nama":"Buavita Leci", "harga": 7500, "stok":25},
    {"nama":"Fruit Tea", "harga": 4000, "stok":40},
    {"nama":"Yakult", "harga": 2000, "stok":50}
]

# looping yang akan terus berjalan hingga mengeksekusi perintah "break"
while True:
    clearScreen()

    print("\n========== Digital Vending Machine ==========")
    
    # menampilkan list menu
    for i in range(0, len(menu) + 1):
        
        # pilihan keluar dari program
        if i == len(menu):
            print(f'({i+1}) -> Keluar')
        
        # pilihan menu
        else:
            print(f'({i + 1}) -> {menu[i]["nama"]}')

    print("=============================================")
    
    # meminta user untuk memilih nomor berapa
    try:
        pilihan_menu = int(input("Pilihan -> "))
    except:
        continue

    # validasi input dari user
    if not (pilihan_menu > 0 and pilihan_menu <= len(menu) + 1) :
        print("Pilihan tidak valid!!!")
        continue
    elif pilihan_menu == len(menu) + 1:
        break

    # menampilkan data produk yang dipilih
    clearScreen()
    print("\n========== Pilihan Produk ==========")

    print(f"Produk : {menu[pilihan_menu - 1]['nama']}")
    print(f"Harga  : Rp{menu[pilihan_menu - 1]['harga']}")
    print(f"Stok   : {menu[pilihan_menu - 1]['stok']}")
    print("======================================")
    
    # Beritahu user apabila stok habis
    if menu[pilihan_menu - 1]['stok'] <= 0:
        print("Stok habis!!!!")
        continue
    
    # apabila tidak tanya ke user ingin beli atau tidak
    pilihan_beli = input("Beli? (y/n) -> ").lower().strip()

    # jika iya tanya user ingin beli berapa
    if pilihan_beli == "y":
        jumlah_beli = int(input("Beli berapa? "))
        
        # jika jumlah yang diinginkan user tidak valid, kembali ke menu
        if jumlah_beli <= 0 or jumlah_beli > menu[pilihan_menu - 1]['stok']:
            print("Stok tidak memadai!")
            continue
        
        # kurangi stok yang ada dengan jumlah yang dibeli user
        menu[pilihan_menu - 1]['stok'] -= jumlah_beli

        # hitung harga total yang harus dibayar user
        total_harga = jumlah_beli * menu[pilihan_menu - 1]['harga']
        print(f"Total harga: Rp{total_harga}")

        # user membayar uang
        uang = int(input("Masukkan uang anda: "))

        # apabila uang tidak cukup
        if uang < total_harga:
            print("Uang tidak cukup!")
            continue
        
        # hitung kembalian dan terimakasih
        kembali = uang - total_harga
        print(f"\nKembalian anda Rp{kembali} Terimakasih sudah membeli!\n")
        
        # tanya ke user ingin beli lagi atau tidak
        pilihan_lanjut = input("Beli lagi (y/n) ? ")
        if pilihan_lanjut == "y":
            continue
        else:
            break

    # kembali ke menu apabila user tidak ingin beli produk yang dipilih
    else:
        continue

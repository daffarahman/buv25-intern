print("Selamat datang di Warung Soto")

nama = input("Hai! siapa km? ")

data_produk = {
    "soto":  8000,
    "es teh": 3000,
    "gorengan" : 1500
}

print("\nMenu Kami:")
print(data_produk)

produk = input("\nBeli apa? ")

if produk in data_produk:
    jumlah = int(input("Mau beli berapa? "))
    total_bayar = data_produk[produk] * jumlah
    print("\nTotal harga: Rp", total_bayar)
else:
    print("produknya gada mas")

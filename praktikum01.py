while True:
    print("kalkulator sederhana")
    print("1. penjumlahan :")
    print("2. pengurangan :")
    print("3. perkalian :")
    print("4. pembagian :")
    pilihan = input("Masukan Pilihan Operasi(1/2/3/4) :" ).lower()
    if pilihan == "q":
        break
    bil1 = int(input("Masukan Bilangan 1 :"))
    bil2 = int(input("Masukan Bilangan 2 :"))
    if pilihan == '1' :
        pertambahan = bil1 + bil2
        hasil = bil1 + bil2
        print("Hasilny adalah ", hasil)
    elif pilihan == '2' :
        pengurangan = bil1 - bil2
        hasil = bil1 - bil2
        print("Hasilny adalah ", hasil)
    elif pilihan == '3' :
        perkalian = bil1 * bil2
        hasil = bil1 * bil2
        print("Hasilny adalah ", hasil)
    elif pilihan == '4' :
        pembagian = bil1 / bil2
        hasil = bil1 / bil2
        print("Hasilny adalah ", hasil)
    elif pilihan == "q" or "Q":
        print()

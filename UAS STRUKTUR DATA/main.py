# menyimpan data penjual dan diamond
sellers = []  # List utama untuk menyimpan data penjual dan diamond

# Fungsi untuk menambahkan data penjual dan diamond
def add_seller_and_diamond():
    global sellers  # Menyatakan sellers sebagai global
    name = input("Masukkan Nama Penjual: ")
    email = input("Masukkan Email Penjual: ")
    nama_game = input("Masukkan Nama Game: ")
    jumlah = int(input("Masukkan Jumlah Diamond yang diminta: "))

    # Mencari apakah penjual sudah ada
    for seller in sellers:
        if seller['name'] == name and seller['email'] == email:
            # Jika penjual sudah ada, cari diamond
            for diamond in seller['diamonds']:
                if diamond['name'].lower() == nama_game.lower():
                    diamond['jumlah'] += jumlah  # Tambahkan jumlah diamond
                    print("Jumlah diamond berhasil diperbarui!")
                    return
            # Jika diamond belum ada, tambahkan diamond baru
            seller['diamonds'] += [{
                'name': nama_game,
                'jumlah': jumlah
            }]
            print("Diamond baru berhasil ditambahkan!")
            return
    # Jika penjual belum ada, buat entri baru
    seller_data = {
        'name': name,
        'email': email,
        'diamonds': [
            {
                'name': nama_game,
                'jumlah': jumlah
            }
        ]
    }
    sellers.append(seller_data)  # data berhasil ditambahkan ke list sellers
    print("Penjual dan Diamond berhasil ditambahkan!")

# Fungsi bubble sort mengurutkan berdasarkan nama penjual
def bubble_sort(sellers_list):
    n = len(sellers_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sellers_list[j]['name'] > sellers_list[j + 1]['name']:
                sellers_list[j], sellers_list[j + 1] = sellers_list[j + 1], sellers_list[j]

# Fungsi untuk menampilkan semua data diurutkan berdasarkan nama penjual
def list_sellers_and_diamonds():
    print("\nDaftar Penjual dan Diamond:")
    bubble_sort(sellers)  # memanggil bubble_sort
    
    if not sellers:
        print("Tidak ada data penjual atau diamond yang tersedia.")
        return
    for seller in sellers:
        print(f"Penjual: {seller['name']}, Email: {seller['email']}")
        for diamond in seller['diamonds']:
            print(f"  - Diamond: {diamond['name']}, Jumlah: {diamond['jumlah']}")

# Fungsi linear search untuk mencari penjual berdasarkan nama
def search_seller(name):
    found = False
    print(f"\nHasil Pencarian untuk Penjual: {name}")    
    for seller in sellers:
        if seller['name'].lower() == name.lower():
            print(f"Penjual: {seller['name']}, Email: {seller['email']}")
            for diamond in seller['diamonds']:
                print(f"  - Diamond: {diamond['name']}, Jumlah: {diamond['jumlah']}")
            found = True
    if not found:
        print("Penjual tidak ditemukan")

# Fungsi untuk memberi diamond kepada penjual
def give_diamond():
    list_sellers_and_diamonds()
    email = input("\nMasukkan Email Penjual yang ingin diberi diamond: ")
    nama_game = input("Masukkan Nama Game: ")
    jumlah = int(input("Masukkan Jumlah Diamond yang ingin diberikan: "))
    
    # Mencari penjual berdasarkan email
    for seller in sellers:
        if seller['email'] == email:
            # Mencari diamond berdasarkan nama
            for diamond in seller['diamonds']:
                if diamond['name'].lower() == nama_game.lower():
                    if diamond['jumlah'] >= jumlah:
                        diamond['jumlah'] -= jumlah  # Kurangi jumlah diamond
                        print(f"Berhasil memberi {jumlah} diamond kepada {seller['name']} untuk diamond {nama_game}!")
                        return
                    else:
                        print("Error: Jumlah diamond tidak cukup.")
                        return
            print("Error: Diamond tidak ditemukan.")
            return
    
    print("Error: Penjual tidak ditemukan.")

# Fungsi menu utama
while True:
    print("\n--- Menu ---")
    print("1. Tambah Penjual dan Diamond")
    print("2. Lihat Penjual dan Diamond")
    print("3. Cari Penjual")
    print("4. Beri Diamond kepada Penjual")
    print("5. Keluar")
    
    choice = input("Pilih opsi (1-5): ")
    
    if choice == '1':
        add_seller_and_diamond()
    elif choice == '2':
        list_sellers_and_diamonds()
    elif choice == '3':
        name = input("Masukkan Nama Penjual yang dicari: ")
        search_seller(name)
    elif choice == '4':
        give_diamond()
    elif choice == '5':
        print("Terima kasih! Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
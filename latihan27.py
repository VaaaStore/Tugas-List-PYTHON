mahasiswa = ["Andi", "Budi", "Citra", "Dewi"]
mahasiswa_lower = [m.lower() for m in mahasiswa]
while True:
    find = input("Masukkan nama yang dicari: ").lower()
    if find in mahasiswa_lower:
        idx = mahasiswa_lower.index(find)
        print(f"Data ditemukan pada urutan ke-{idx + 1}")
    else:
        print("Data tidak ditemukan")
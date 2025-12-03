Angka = int(input('Silahkan isi match hero : '))
persentase = float(input('Silahkan isi wr hero (%): ')) / 100
target = float(input('Silahkan isi target wr (%): ')) / 100

# total menang & kalah sekarang
hasil = Angka * persentase
kalah = Angka - hasil

# rumus mencari tambahan match untuk capai target
match = (target * Angka - hasil) / (1 - target)

print("Menang sekarang :", hasil)
print("Kalah sekarang  :", kalah)
print("Butuh menang berturut-turut sekitar:", int(match), "match")
